#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 15:17:17 2021

@author: pendar
"""

#With a given integral number n,
#write a program to generate a dictionary that contains (i, i x i) such
#that is an integral number between 1 and n (both included).
#and then the program should print the dictionary.


n = int(input("enter a number :"))

dict = {}
#or d = dict()

for i in range(1 , n+1):
    dict[i] = i**2

print(dict)

