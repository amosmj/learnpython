# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 09:41:02 2017
sock Merchant - hacker rank
https://hackerrank-challenge-pdfs.s3.amazonaws.com/25168-sock-merchant-English?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1505489916&Signature=GYay43GEa%2BmevA7qoAZp5f7ON48%3D&response-content-disposition=inline%3B%20filename%3Dsock-merchant-English.pdf&response-content-type=application%2Fpdf

n = number of loose socks
i = a sock
j = a differnt sock
Ci = sock i's color
if Ci = Cj then a customer will buy both

inputs 
'n' = number of socks
'C0 C1 C2 ..Cn-1' = sock colors

output how many socks can be sold 

@author: mjamos
"""
from collections import Counter
import random

def pairSocks(sock_string):
    cnt = Counter()
    pair_count = 0
    for sock in sock_string.split():
        cnt[sock] +=1
    for count_thing, count_of_count_thing in dict(cnt).items():
        pair_count += int(count_of_count_thing / 2)
    return pair_count

def generateRandomSocks():
    sock_string = ''
    socks = random.randint(1,100)
    for sock in range(socks):
        sock_string += (str(random.randint(1,100)) + ' ')
    sock_string = sock_string[:-1]
    return sock_string

#print(pairSocks('10 20 20 10 10 30 50 10 20'))
print(pairSocks(generateRandomSocks()))