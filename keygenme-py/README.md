# keygenme-py

AUTHOR: SYREAL

**Disclaimer! I do not own any of the challenge files**

## Looking at the keygenme-trial.py

Instead of running the script right away, it is best practice to read the source code, right?
```py
# GLOBALS --v
arcane_loop_trial = True
jump_into_full = False
full_version_code = ""

username_trial = "FREEMAN"
bUsername_trial = b"FREEMAN"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
```
These are all the global variables. What is really important to us though? 
```py
username_trial = "FREEMAN"
bUsername_trial = b"FREEMAN"
```
This will be obvious later, next ofcourse the flag! Or here it is called the `key`. It is comprised of two static parts, and a dynamic part:
```py
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
```
Great... maybe we can have a look at how the dynamic part is generated? 

### Dynamic key

To check the validity of the dynamic key, the following function is used (I split it):
```py
def check_key(key, username_trial):

    global key_full_template_trial

    if len(key) != len(key_full_template_trial):
        return False
    else:
        # Check static base key part --v
        i = 0
        for c in key_part_static1_trial:
            if key[i] != c:
                return False

            i += 1
```
First, check if the key is even long enough! After that check if we have the 1st static part correct (we can copy and paste, right?). Now the iterator `i` is at our dynamic part, and here is the `if tree` that checks our dynamic key:
```py
if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
    return False
else:
    i += 1

if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
    return False
else:
    i += 1

if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
    return False
else:
    i += 1

if key[i] != hashlib.sha256(username_trial).hexdigest()[6]:
    return False
else:
    i += 1

if key[i] != hashlib.sha256(username_trial).hexdigest()[2]:
    return False
else:
    i += 1

if key[i] != hashlib.sha256(username_trial).hexdigest()[7]:
    return False
else:
    i += 1

if key[i] != hashlib.sha256(username_trial).hexdigest()[1]:
    return False
else:
    i += 1

if key[i] != hashlib.sha256(username_trial).hexdigest()[8]:
    return False
```
So notice the following, we have a bunch of indexes: `4,5,3,6,2,7,1,8`. How do we use these? Well first a `sha256` hash of the username is `FREEMAN` calculated and then we pick the corresponding character. This is pretty easy to script.

## solve.py

```py
import hashlib
import base64


key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

username_trial = b"FREEMAN"

potential_dynamic_key = ""

# where our input begins:
offset = 23

# positions in username_trial
positions = [4,5,3,6,2,7,1,8]

for p in positions:
	potential_dynamic_key += hashlib.sha256(username_trial).hexdigest()[p]

key = key_part_static1_trial + potential_dynamic_key + key_part_static2_trial
print(key)
print(len(key))
```
We have a hardocded offset, out positions and then we just calculate the hashes one by one, and add to the key. After running the script, here is the result:
```
picoCTF{1n_7h3_|<3y_of_0d208392}
32 
```
Great! 