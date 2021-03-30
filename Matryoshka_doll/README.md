# Matryoshka Doll

Category: Forensics </br>
AUTHOR: SUSIE/PANDU

## Description
```
Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another.
What's the final one? Image: this
```

## The file

What's inside? By now you should know the gist of it: `file`, `binwalk`, `strings` (maybe), `hexeditor`
```bash
root@kali:~/CTFs/Picoctf-2021/matryoshka_doll-solved# file dolls.jpg 
dolls.jpg: PNG image data, 594 x 1104, 8-bit/color RGBA, non-interlaced
root@kali:~/CTFs/Picoctf-2021/matryoshka_doll-solved# binwalk dolls.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 594 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378952, uncompressed size: 383937, name: base_images/2_c.jpg
651610        0x9F15A         End of Zip archive, footer length: 22

```
Right, so we can stop right here... There is a zip archive hidden inside the image! 

## Extracting

```bash
root@kali:~/CTFs/Picoctf-2021/matryoshka_doll-solved# 7z x dolls.jpg

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,3 CPUs Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 651632 bytes (637 KiB)

Extracting archive: dolls.jpg
--
Path = dolls.jpg
Type = zip
Offset = 272492
Physical Size = 379140

Everything is Ok

Size:       383937
Compressed: 651632
```
Great, we extracted it! What's inside?
```bash
root@kali:~/CTFs/Picoctf-2021/matryoshka_doll-solved/base_images# ls
2_c.jpg
root@kali:~/CTFs/Picoctf-2021/matryoshka_doll-solved/base_images# binwalk 2_c.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 526 x 1106, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
187707        0x2DD3B         Zip archive data, at least v2.0 to extract, compressed size: 196042, uncompressed size: 201444, name: base_images/3_c.jpg
383804        0x5DB3C         End of Zip archive, footer length: 22
383915        0x5DBAB         End of Zip archive, footer length: 22

```
Oh lovely... another one. To be expected with matryoshka dolls.
```bash
root@kali:~/CTFs/Picoctf-2021/matryoshka_doll-solved/base_images/base_images# ls base_images
3_c.jpg
```
Now instead of going through it manually, I wrote a bash script. 

## Bash script

```bash
#!/bin/bash

check_dir(){
	if [ -d "base_images" ]; then
		cd "base_images"
		return 0
	else
			return 1
	fi
}

check_for_zip() {
	if binwalk "$1" | grep "Zip" > /dev/null ; then
		7z x "$1"
		return 0
	fi
	return 1
}

check_for_zip "$1"

check_dir

for i in {2..20}
do 
	if check_for_zip $i"_c.jpg"; then
		if check_dir; then
			echo "in" $i"_c.jpg"
		else
			echo "done"
			cat flag.txt
			break
		fi
	fi
done
```
Now run and watch it finish:
```bash
root@kali:~/CTFs/Picoctf-2021/matryoshka_doll-solved# ./solve.sh dolls.jpg 

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,3 CPUs Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 651632 bytes (637 KiB)

Extracting archive: dolls.jpg
--
Path = dolls.jpg
Type = zip
Offset = 272492
Physical Size = 379140

Everything is Ok

Size:       383937
Compressed: 651632

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,3 CPUs Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 383937 bytes (375 KiB)

Extracting archive: 2_c.jpg
--
Path = 2_c.jpg
Type = zip
Offset = 187707
Physical Size = 196230

Everything is Ok

Size:       201444
Compressed: 383937
in 2_c.jpg

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,3 CPUs Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 201444 bytes (197 KiB)

Extracting archive: 3_c.jpg
--
Path = 3_c.jpg
Type = zip
Offset = 123606
Physical Size = 77838

Everything is Ok

Size:       79807
Compressed: 201444
in 3_c.jpg

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,3 CPUs Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 79807 bytes (78 KiB)

Extracting archive: 4_c.jpg
--
Path = 4_c.jpg
Type = zip
Offset = 79578
Physical Size = 229

Everything is Ok

Size:       81
Compressed: 79807
done
picoCTF{96fac089316e094d41ea046900197662}
```
That was fun! 