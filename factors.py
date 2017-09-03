# A and B are strings of space delimmited numbers
# n and m are the size of A and B 1 - 10
# components of A and B are 1 - 100
# elements of A are all factors of x while x is a factor of all elements of B
# output is a count of xs
import random
import time

def sample_given():
    sample_ouput = []
    length_line = '2 3'
    sample_ouput.append(length_line)
    A_line = ['2','4']
    sample_ouput.append(A_line)
    B_line = ['16', '32', '96']
    sample_ouput.append(B_line)
    return sample_ouput

def generate_random():
    length_line = str(random.randint(1,10)) + ' ' + str(random.randint(1,10))
    random_output=[]
    random_output.append(length_line)
    line_length = int(length_line.split()[0])
    A_list = []
    B_list = []
    for item in range(line_length):
        A_list.append(str(random.randint(1,100)))
    random_output.append(A_list)
    a_max = int(max(A_list))
    line_length = int(length_line.split()[1])
    for item in range(line_length):
        B_list.append(str(random.randint(a_max,100)))
    random_output.append(B_list)
    return random_output
    
def solve(input_list):
    output_text = ''
    if int(max(input_list[1])) <= int(min(input_list[2])):
        #print('possible')
        #find denominators of B
        denom_list = []
        final_list = []
        #for every number in our second list, find the common denominators
        for a_number in range(1, int(min(input_list[2]))+1):
            denom_bool = True
            #this could be shortened by someone smarter than me
            #once a number is found to not be a common denominator
            #this loop should be abandon
            for other_number in input_list[2]:
                #print (other_number + ' % ' + str(a_number) +  ' = ' + str(int(other_number)%a_number))
                if int(other_number )% a_number != 0:
                    denom_bool = False
            #if no number failed the test, add it to the list of potentials
            if denom_bool == True:
                denom_list.append(a_number)
        #printing list for testing
        #print(denom_list)
        #print(input_list[1])
        #now tht I have all the common denominators of B
        #I want to test them against A
        #begin by throwing out everything less than the max of A
        #removing causes weirdness to happen so I'm building a
        # new list
        valid_denoms = []
        for denom in denom_list:
            #print(denom_list)
            #print(denom)
            if denom >= int(max(input_list[1])):
                valid_denoms.append(denom)
        #print(valid_denoms)
        #now test what remains
        for denom_item in valid_denoms:
            factor_bool = True
            for input_item in input_list[1]:
                if denom_item % int(input_item) != 0:
                    factor_bool = False
            if factor_bool == True:
                final_list.append(denom_item)
        #print(final_list)
        output_text = len(final_list)

    else:
        output_text = 'not possible'
    return output_text

def getTotalX(a, b):
    lis1 = []
    finalCount = 0
    #print('for loop mins', min(a), min(b))
    for elem in range(min(a), min(b)+1):
        #print('elem: ', elem)
        countFirst = 0
        countSecond = 0
        #print('for loop i: ', range(0,len(a)))
        for i in range(0, len(a)):
            #print('elem % a[i]: ', elem,' % ', a[i],' = ',elem % a[i])
            #print('countfirst = ', countFirst)
            if elem % a[i] == 0:
                #print('got mod 0')
                countFirst +=1
        if countFirst == len(a):
            for el in range(0, len(b)):
                #print('b[el] % elem: ', b[el],' % ', elem,' = ',b[el] % elem)
                if b[el] % elem == 0:
                    #print('got mod2 again')
                    countSecond +=1
            if countSecond == len(b):
                #print('thats a keeper', elem)
                finalCount +=1
    return finalCount

def rebuild_to_be_faster(input_list):
    a_list = list(map(int,input_list[1]))
    b_list = list(map(int,input_list[2]))
    range_of_factors = [max(a_list),min(b_list)]
    possible_factors = []
    currect_factor = range_of_factors[0]
    multiplier = 1
    #print('A list: ', a_list, ' B list: ', b_list, ' range: ',range_of_factors)
    while currect_factor <= range_of_factors[1]:
        possible_factors.append(currect_factor)
        multiplier = multiplier + 1
        currect_factor = range_of_factors[0] * multiplier
        #print('possible factors: ',possible_factors,)
    #possible factor list built, now test against list A
    passed_test_a = []
    for possibility in possible_factors:
        in_the_running = True
        for a_item in a_list:
            #print('test a: ', possibility,' % ', a_item, ' = ', possibility % a_item )
            if possibility % a_item != 0:
                in_the_running = False
        if in_the_running == True:
            passed_test_a.append(possibility)
    #print('passed test a: ', passed_test_a)
    if len(passed_test_a) > 0:
        factors = []
        for still_possible in passed_test_a:
            in_the_running = True
            for b_item in b_list:
                #print('test b: ', b_item , ' % ', still_possible, ' = ', b_item%still_possible)
                if b_item % still_possible != 0:
                    in_the_running = False
            if in_the_running == True:
                factors.append(still_possible)
        #print(factors)
    else:
        factors = []
    return len(factors)

time_keeper = [[],[],[],[]]
#slot 0 is data, slot 1 is Ardy,
#sot 2 is Mike's first attempt, slow 3 is Mike's second attempt
foo = sample_given()
time_keeper[0].append(foo)
temp_time_keeper = time.time()
getTotalX(list(map(int,foo[1])),list(map(int,foo[2])))
time_keeper[1].append(time.time() - temp_time_keeper)
temp_time_keeper = time.time()
solve(foo)
time_keeper[2].append(time.time() - temp_time_keeper)
temp_time_keeper = time.time()
rebuild_to_be_faster(foo)
time_keeper[3].append(time.time() - temp_time_keeper)
counter = 1 #0 was test data

while counter < 10000:
    foo = generate_random()
    time_keeper[0].append(foo)
    temp_time_keeper = time.time()
    getTotalX(list(map(int,foo[1])),list(map(int,foo[2])))
    time_keeper[1].append(time.time() - temp_time_keeper)
    temp_time_keeper = time.time()
    solve(foo)
    time_keeper[2].append(time.time() - temp_time_keeper)
    temp_time_keeper = time.time()
    rebuild_to_be_faster(foo)
    time_keeper[3].append(time.time() - temp_time_keeper)
    counter = counter + 1

#print(time_keeper)

#ardy_time = 0
#for a_time in time_keeper[1]:
#    ardy_time = ardy_time + a_time
#print(ardy_time)

print('Ardys total time was: ' , sum(time_keeper[1]))
print('Mikes first attempt total time was: ' , sum(time_keeper[2]))
print('Mikes second attempt total time was: ' , sum(time_keeper[3]))

