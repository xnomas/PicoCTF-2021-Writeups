# Transformation

Category: Reverse Engineering </br>
AUTHOR: MADSTACKS

## Description
```
I wonder what this really is... enc ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```

## Solution

You could simply use [cyberchef]() on the `magic` setting, and get the flag `picoCTF{16_bits_inst34d_of_8_e141a0f7}`</br>.

Or use this:
```py
decode = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥ㄴㅡて㝽'
print(decode.encode('utf-16-be'))
```