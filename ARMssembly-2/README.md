# ARMssembly 2

Category: Reverse Engineering </br>
AUTHOR: DYLAN MCGUIRE

**Disclaimer! I do not own any of the challenge files!**

## Description
```
What integer does this program print with argument 2403814618? File: chall_2.S 
Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
```

## Function analysis

If you've read my previous ARMssembly writeups, you know the drill. It's time to delv deep into the functions.
```
func1:
	sub	sp, sp, #32
	str	w0, [sp, 12]  
	str	wzr, [sp, 24] 
	str	wzr, [sp, 28] 
	b	.L2
.L3: 
+-->ldr	w0, [sp, 24]           
|	add	w0, w0, 3               
|	str	w0, [sp, 24]           
|	ldr	w0, [sp, 28]           
|	add	w0, w0, 1              
|	str	w0, [sp, 28]           
.L2:                           
|	ldr	w1, [sp, 28]            
|	ldr	w0, [sp, 12]            
|	cmp	w1, w0                  
+---bcc	.L3          
	ldr	w0, [sp, 24] 
	add	sp, sp, 32
	ret
	.size	func1, .-func1
	.section	.rodata
	.align	3
``` 
These are the most important functions for us. And I added an `r2` style loop indicator for myself. Time for `.func1`.

### .func1
```
func1:
	sub	sp, sp, #32
	str	w0, [sp, 12]  
	str	wzr, [sp, 24] 
	str	wzr, [sp, 28] 
	b	.L2
```
By now, this should be obvious to you. But we see one peculiar register. `wzr` is a special register, and it holds the value `0`. This allows us to quickly store a 0. 
```
stack + 12 = 2403814618
stack + 24 = 0
stack + 28 = 0
```
And finally just `branch` (jmp in x86) to `.L2`! 

### .L2
```
.L2:                           
	ldr	w1, [sp, 28]            
	ldr	w0, [sp, 12]            
	cmp	w1, w0                  
    bcc	.L3          
	ldr	w0, [sp, 24] 
	add	sp, sp, 32
	ret
	.size	func1, .-func1
	.section	.rodata
	.align	3
```
Now `load 0 into w1` and `load 2403814618 into w0` and compare them. (Which is just a `sub` without storing the value) And most importantly `bcc` branch if the carry flag is set (it is set when w1 < w0)! This is our loop! We could maybe imagine it like this:
```py
while w1 >= w0:
	L3()
```
After the loop ends `load a value from stack + 24 into w0`. Return. 

### .L3
```
.L3: 
    ldr	w0, [sp, 24]            
	add	w0, w0, 3                
	str	w0, [sp, 24]            
	ldr	w0, [sp, 28]            
	add	w0, w0, 1               
	str	w0, [sp, 28]  
```
This is what happens every loop, `Load the value from stack + 24 into w0` and add 3 to it. `Store this value in stack + 24`. Next `load the value from stack + 28 into w0` and add 1 to it. `Store this value in stack + 28`. And we will do this, until  `stack + 28 > stack + 12`. 

## Solving it

So what do we actually need to do? Well think about it... we just want to loop. But can we do this without looping? `2403814618` loops is quite a lot.... How about we just calculate `2403814618 * 3`, since we know that 3 will be added everytime and this is what will be printed. What is the result? `7211443854` Great! Just turn into hex and... Well not so fast. It needs to be a 32bit number, here's how we convert:
```py
>>> result = int(hex(7211443854),16) & 0xffffffff
>>> f'{result:08x}'
'add5e68e'
>>>
```
There we go! Wrapped it in `picoCTF{add5e68e}` and done.