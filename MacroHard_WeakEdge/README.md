# MacroHard WeakEdge

Category: Forensics </br>
AUTHOR: MADSTACKS

**Diclaimer! None of the challenge files are mine!**

## Description
```
I've hidden a flag in this file. Can you find it? Forensics is fun.pptm
```

## PowerPoint

Now, here's the thing. If you've done `Weird File` (writeup [here](https://github.com/xnomas/PicoCTF-2021-Writeups/tree/main/Weird_File)) you already know that a PowerPoint file can be unzipped and it's contents looked through! Also, we have a big hint in the name of this challenge `Macro`. And to prove this, just run `binwalk`:
```
root@kali:~/CTFs/Picoctf-2021/macrohard_weakedge-solved# binwalk Forensics\ is\ fun.pptm 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Zip archive data, at least v2.0 to extract, compressed size: 674, uncompressed size: 10660, name: [Content_Types].xml
1243          0x4DB           Zip archive data, at least v2.0 to extract, compressed size: 259, uncompressed size: 738, name: _rels/.rels
2063          0x80F           Zip archive data, at least v2.0 to extract, compressed size: 951, uncompressed size: 5197, name: ppt/presentation.xml
3064          0xBF8           Zip archive data, at least v2.0 to extract, compressed size: 189, uncompressed size: 311, name: ppt/slides/_rels/slide46.xml.rels
3316          0xCF4           Zip archive data, at least v2.0 to extract, compressed size: 688, uncompressed size: 1740, name: ppt/slides/slide1.xml
4055          0xFD7           Zip archive data, at least v2.0 to extract, compressed size: 657, uncompressed size: 1681, name: ppt/slides/slide2.xml
4763          0x129B          Zip archive data, at least v2.0 to extract, compressed size: 659, uncompressed size: 1681, name: ppt/slides/slide3.xml
5473          0x1561          Zip archive data, at least v2.0 to extract, compressed size: 657, uncompressed size: 1682, name: ppt/slides/slide4.xml
6181          0x1825          Zip archive data, at least v2.0 to extract, compressed size: 658, uncompressed size: 1682, name: ppt/slides/slide5.xml
...
...
43914         0xAB8A          Zip archive data, at least v2.0 to extract, compressed size: 657, uncompressed size: 1681, name: ppt/slides/slide58.xml
44623         0xAE4F          Zip archive data, at least v2.0 to extract, compressed size: 189, uncompressed size: 311, name: ppt/slides/_rels/slide47.xml.rels
...
47899         0xBB1B          Zip archive data, at least v2.0 to extract, compressed size: 189, uncompressed size: 311, name: ppt/slides/_rels/slide13.xml.rels
48151         0xBC17          Zip archive data, at least v2.0 to extract, compressed size: 646, uncompressed size: 8783, name: ppt/_rels/presentation.xml.rels
49122         0xBFE2          Zip archive data, at least v2.0 to extract, compressed size: 192, uncompressed size: 311, name: ppt/slides/_rels/slide1.xml.rels
...
59700         0xE934          Zip archive data, at least v2.0 to extract, compressed size: 189, uncompressed size: 311, name: ppt/slides/_rels/slide45.xml.rels
59952         0xEA30          Zip archive data, at least v2.0 to extract, compressed size: 2063, uncompressed size: 13875, name: ppt/slideMasters/slideMaster1.xml
62078         0xF27E          Zip archive data, at least v2.0 to extract, compressed size: 1281, uncompressed size: 4678, name: ppt/slideLayouts/slideLayout1.xml
...
75061         0x12535         Zip archive data, at least v2.0 to extract, compressed size: 1187, uncompressed size: 4200, name: ppt/slideLayouts/slideLayout11.xml
76312         0x12A18         Zip archive data, at least v2.0 to extract, compressed size: 277, uncompressed size: 1991, name: ppt/slideMasters/_rels/slideMaster1.xml.rels
76663         0x12B77         Zip archive data, at least v2.0 to extract, compressed size: 188, uncompressed size: 311, name: ppt/slideLayouts/_rels/slideLayout1.xml.rels
...
79284         0x135B4         Zip archive data, at least v2.0 to extract, compressed size: 188, uncompressed size: 311, name: ppt/slideLayouts/_rels/slideLayout11.xml.rels
79547         0x136BB         Zip archive data, at least v2.0 to extract, compressed size: 1732, uncompressed size: 8399, name: ppt/theme/theme1.xml
81329         0x13DB1         Zip archive data, at least v1.0 to extract, compressed size: 2278, uncompressed size: 2278, name: docProps/thumbnail.jpeg
83660         0x146CC         Zip archive data, at least v2.0 to extract, compressed size: 2222, uncompressed size: 7168, name: ppt/vbaProject.bin
85930         0x14FAA         Zip archive data, at least v2.0 to extract, compressed size: 397, uncompressed size: 818, name: ppt/presProps.xml
86374         0x15166         Zip archive data, at least v2.0 to extract, compressed size: 387, uncompressed size: 811, name: ppt/viewProps.xml
86808         0x15318         Zip archive data, at least v2.0 to extract, compressed size: 172, uncompressed size: 182, name: ppt/tableStyles.xml
87029         0x153F5         Zip archive data, at least v2.0 to extract, compressed size: 342, uncompressed size: 666, name: docProps/core.xml
87682         0x15682         Zip archive data, at least v2.0 to extract, compressed size: 556, uncompressed size: 3784, name: docProps/app.xml
88548         0x159E4         Zip archive data, at least v2.0 to extract, compressed size: 81, uncompressed size: 99, name: ppt/slideMasters/hidden
100071        0x186E7         End of Zip archive, footer length: 22

```
The output is really big, so I shortened it. Hmm... notice anything peculiar? 

### Extracting and snooping
```bash
root@kali:~/CTFs/Picoctf-2021/macrohard_weakedge-solved/writeup# ls
'Forensics is fun.pptm'
root@kali:~/CTFs/Picoctf-2021/macrohard_weakedge-solved/writeup# 7z x Forensics\ is\ fun.pptm 

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,3 CPUs Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 100093 bytes (98 KiB)

Extracting archive: Forensics is fun.pptm
--
Path = Forensics is fun.pptm
Type = zip
Physical Size = 100093

Everything is Ok

Files: 153
Size:       237329
Compressed: 100093
```
Awesome! Now we can just look through it.
```bash
root@kali:~/CTFs/Picoctf-2021/macrohard_weakedge-solved/writeup# ls -la *
-rw-r--r-- 1 root root  10660 Dec 31  1979 '[Content_Types].xml'
-rw-r--r-- 1 root root 100093 Mar 30 12:59 'Forensics is fun.pptm'

docProps:
total 20
drwx------ 2 root root 4096 Mar 30 12:59 .
drwxr-xr-x 5 root root 4096 Mar 30 12:59 ..
-rw-r--r-- 1 root root 3784 Dec 31  1979 app.xml
-rw-r--r-- 1 root root  666 Dec 31  1979 core.xml
-rw-r--r-- 1 root root 2278 Dec 31  1979 thumbnail.jpeg

ppt:
total 56
drwx------ 7 root root 4096 Mar 30 12:59 .
drwxr-xr-x 5 root root 4096 Mar 30 12:59 ..
-rw-r--r-- 1 root root 5197 Dec 31  1979 presentation.xml
-rw-r--r-- 1 root root  818 Dec 31  1979 presProps.xml
drwx------ 2 root root 4096 Mar 30 12:59 _rels
drwx------ 3 root root 4096 Mar 30 12:59 slideLayouts
drwx------ 3 root root 4096 Mar 30 12:59 slideMasters
drwx------ 3 root root 4096 Mar 30 12:59 slides
-rw-r--r-- 1 root root  182 Dec 31  1979 tableStyles.xml
drwx------ 2 root root 4096 Mar 30 12:59 theme
-rw-r--r-- 1 root root 7168 Dec 31  1979 vbaProject.bin
-rw-r--r-- 1 root root  811 Dec 31  1979 viewProps.xml

_rels:
total 12
drwx------ 2 root root 4096 Mar 30 12:59 .
drwxr-xr-x 5 root root 4096 Mar 30 12:59 ..
-rw-r--r-- 1 root root  738 Dec 31  1979 .rels

```
Just confirming the file structure that `binwalk` provided. Now! What did you see in tha big output? I saw this: `ppt/vbaProject.bin`, `ppt/slideMasters/hidden`. Time to check these out! 

## Macro (Hard)

```bash
root@kali:~/CTFs/Picoctf-2021/macrohard_weakedge-solved/writeup# strings ppt/vbaProject.bin 
VBAProje
stdole>
*\G{00
020430-
6}#2.0#0
#C:\Wind
ows\Syst em32\
tlb#OLE 
Automati
EOffDic
2DF8D04C
-5BFA-10
1B-BDE5
gram Fil
es\Commo
Micros
oft Shar
ed\OFFIC
E16\MSO.0DLL#
M 1@6.0 Ob
Library
ule1G
sorry_but_this_isn't_it
...
```
Oh? It's not? Well no worries, we still have the second file to look through.

## Weak (Edge)

```bash
root@kali:~/CTFs/Picoctf-2021/macrohard_weakedge-solved/writeup# cat ppt/slideMasters/hidden 
Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q
```
Riiiight.. well looking at it, this string looks like base64.

## Flag

I just replaced the spaces with nothing in SublimeText. `ZmxhZzogcGljb0NURntEMWRfdV9rbjB3X3BwdHNfcl96MXA1fQ` looks even more like base64, doesn't it?

```bash
echo ZmxhZzogcGljb0NURntEMWRfdV9rbjB3X3BwdHNfcl96MXA1fQ | base64 -d
flag: picoCTF{D1d_u_kn0w_ppts_r_z1p5}base64: invalid input
```
Awesome! 
