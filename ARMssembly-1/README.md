# ARMssembly 1

Category: Reverse Engineering </br>
AUTHOR: PRANAY GARG

**Disclaimer! I do not own the challenge file!**

## Description
```
For what argument does this program print `win` with variables 68, 2 and 3? File: chall_1.S 
Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
```

## Going through the functions

Yet again we have a `chall_1.S` arm assembly file, so time to look at the functions and go through it. 
```
func:
	sub	sp, sp, #32
	str	w0, [sp, 12] 
	mov	w0, 68
	str	w0, [sp, 16] 
	mov	w0, 2
	str	w0, [sp, 20] 
	mov	w0, 3
	str	w0, [sp, 24] 
	ldr	w0, [sp, 20] 
	ldr	w1, [sp, 16] 
	lsl	w0, w1, w0   
	str	w0, [sp, 28] 
	ldr	w1, [sp, 28] 
	ldr	w0, [sp, 24] 
	sdiv	w0, w1, w0 
	str	w0, [sp, 28] 
	ldr	w1, [sp, 28] 
	ldr	w0, [sp, 12] 
	sub	w0, w1, w0   
	str	w0, [sp, 28] 
	ldr	w0, [sp, 28] 
	add	sp, sp, 32
	ret
	.size	func, .-func
	.section	.rodata
	.align	3
```
Right, well that is pretty big. Maybe we can go through it piece by piece, like start with the stores.
```
	sub	sp, sp, #32
	str	w0, [sp, 12] 
	mov	w0, 68
	str	w0, [sp, 16] 
	mov	w0, 2
	str	w0, [sp, 20] 
	mov	w0, 3
	str	w0, [sp, 24]
```
So first we make space on the stack for the variables. Our user input is stored on the `stack at offset 12`, next the `mov` instruction is called. 
```
mov w0, 68
```
The value `68` is moved into `w0`. This is a very easy and straight forward instruction. Going on this value is stored on the `stack at offset 16`. So going on like this, we get:
```
stack + 12 = user input
stack + 16 = 68
stack + 20 = 2
stack + 24 = 3
```
Now that we know where everything on the stack is, we can move on.
```
	ldr	w0, [sp, 20] 
	ldr	w1, [sp, 16] 
	lsl	w0, w1, w0   
	str	w0, [sp, 28] 
```
Now `load the number 2 into w0` and `load 68 into w1`. Then the `lsl` instruction is called, which is a left bit shift and store, with the following syntax:
```
lsl x,y,z
```
Shift the value in `y` by `z` and store the result in `x`. A demonstration of the bit shift ( >> or << in most languages):
```
12 in binary is 00001100 (padded to 8bits)

now 00001100 << 2 (logical left shift 2)

take 00001100 move it two bits to the left like so:

00001100 << 2 = 00110000

Convert to decimal = 48
```
Now that we know all this, we can yet again move on.
```
	ldr	w1, [sp, 28] 
	ldr	w0, [sp, 24] 
	sdiv	w0, w1, w0 
	str	w0, [sp, 28] 
```
Start by `loading the value 272 from stack + 28 into w0` (the result of the bit shift!) and `load 3 from stack + 24 into w1`. Next up, the `sdiv` instruction. 
```
sdiv x,y,z
```
Divide `y` by `z` and store in `x`. So in our case `272 // 3 = 90`. And store `90 on the stack + 28`. To keep track of values, here's another listing:
```
stack + 12 = user input
stack + 16 = 68
stack + 20 = 2
stack + 24 = 3
stack + 28 = 90
```
Good, moving on:
```
	ldr	w1, [sp, 28] 
	ldr	w0, [sp, 12] 
	sub	w0, w1, w0   
	str	w0, [sp, 28] 
	ldr	w0, [sp, 28] 
	add	sp, sp, 32
	ret
```
And finally `load 90 into w1`, `load the user input into w0` and `substract 90 - user input`. Store the result of this in `stack + 28` and `load that result back into w0`. Return.

## Going into main
```
main:
	stp	x29, x30, [sp, -48]!
	add	x29, sp, 0
	str	w0, [x29, 28]
	str	x1, [x29, 16]
	ldr	x0, [x29, 16]
	add	x0, x0, 8
	ldr	x0, [x0]
	bl	atoi
	str	w0, [x29, 44]
	ldr	w0, [x29, 44]
	bl	func 
	cmp	w0, 0  <----------  
	bne	.L4
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	bl	puts
	b	.L6
```
Notice the `cmp` instruction. We want the `w0` variable to be `0`! If it's not, we branch to `.L4` which branches to `.L1`, and we don't want the result to be `.L1` but `.L0`:
```
.LC0:
	.string	"You win!"
	.align	3
.LC1:
	.string	"You Lose :("
	.text
	.align	2
	.global	main
	.type	main, %function
``` 

## Solving

So what is the important part? Where does our input come into play?
```
sub	w0, w1, w0
```
Here. We want the result of this substraction to be `0`. And since `w1` is 90, we want to input 90! Convert that to hex and make it 32 bits.
```
picoCTF{0000005a}
``` 