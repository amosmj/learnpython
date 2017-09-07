# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 11:20:01 2017

@author: mjamos
"""
import random

def create_random():
        list_of_birds = []
        number_of_birds = random.randint(1,10)
        for bird in range(number_of_birds):
            list_of_birds.append(random.randint(1,5))
        return list_of_birds

def tally_birds(array_of_birds):
    bird_of_birds = [array_of_birds.count(1),
                     array_of_birds.count(2),
                     array_of_birds.count(3),
                     array_of_birds.count(4),
                     array_of_birds.count(5),]
    print(array_of_birds)
    print(bird_of_birds)
    print(bird_of_birds.index(max(bird_of_birds))+1)
    return 0

#scripted inputs
bird_count = 6
bird_array = [1,4,5,4,5,3]
bird_array = create_random()

tally_birds(bird_array)