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

"""
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
"""