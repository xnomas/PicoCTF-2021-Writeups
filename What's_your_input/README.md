# What's your input

**Disclaimer! I do not own any of the challenge files!**

```
nc mercury.picoctf.net 39137 in.py
```

## in.py

Looking at the `in.py` file that was provided we see this:
```py
#!/usr/bin/python2 -u
import random

cities = open("./city_names.txt").readlines()
city = random.choice(cities).rstrip()
year = 2018

print("What's your favorite number?")
res = None
while not res:
    try:
        res = input("Number? ")
        print("You said: {}".format(res))
    except:
        res = None

if res != year:
    print("Okay...")
else:
    print("I agree!")

print("What's the best city to visit?")
res = None
while not res:
    try:
        res = input("City? ")
        print("You said: {}".format(res))
    except:
        res = None

if res == city:
    print("I agree!")
    flag = open("./flag").read()
    print(flag)
else:
    print("Thanks for your input!")
```
What happens is, that we have to enter `2018` as our first input to pass the check, and then a random city is picked... which we somehow have to guess. Hmmm. But that shouldn't be possible right? Well check out this part `print("You said: {}".format(res))`. 

## Testing

I alawys open a python terminal to test my theory, so here it goes:
```py
city = 'London'
res = input('City? ')
print("You said: {}".format(res))
```

Running this piece of code in a python 2.7 interpreter (online [here](https://replit.com/languages/python) ). I run it and enter the following:
```
City? city
You said: London
```
Great! This confirms my suspicion. In python 2 we can just input the name of a variable, and it will be interpreted as the variable! 

## The solution

This is how my connection went:
```
nc mercury.picoctf.net 32114
What's your favorite number?
Number? 2018
You said: 2018
I agree!
What's the best city to visit?
City? city
You said: Burlington
I agree!
picoCTF{v4lua4bl3_1npu7_6269606}
```
Great!