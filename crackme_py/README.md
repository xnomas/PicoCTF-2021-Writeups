# crackme-py

Category: Reverse Engineering </br>
AUTHOR: SYREAL

## Solving

Open up the source code:
```py
# Hiding this really important number in an obscure piece of code is brilliant!
# AND it's encrypted!
# We want our biggest client to know his information is safe with us.
bezos_cc_secret = "A:4@r%uL`M-^M0c0AbcM-MFE067d3eh2bN"

# Reference alphabet
alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
```
Wow, okay. Jess Bezos! Now look a little lower:
```py
def decode_secret(secret):
    """ROT47 decode

    NOTE: encode and decode are the same operation in the ROT cipher family.
    """
```
So a ROT47, we can just use [cyberchef](https://gchq.github.io/CyberChef/) and decode the secret:
```
picoCTF{1|\/|_4_p34|\|ut_ef5b69a3}
```
Here we go.