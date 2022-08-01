import os
os.system('clear')

#Write a program to input a number and display the factors of a number

# a = int(input('Please enter a number.'))
# for x in range (1,a+1) :
#     if (a%x==0) :
#         print(x)

#Write a program to input a number and count the number of factors
# a = int(input('Please enter a number.'))
# count = 0
# for x in range (1,a+1) :
#     if (a%x==0) :
#         count = count +1
# print(count)
#WAP to input a number and check if it is prime
# a = int(input('Please enter a number.'))
# count = 0
# for x in range (1,a+1) :
#     if (a%x==0) :
#         count = count +1
# if (count == 2) :
#     print('Prime')
# else:
#     print('Not Prime')
#WAP to input a number and check if it is composite
# a = int(input('Please enter a number.'))
# count = 0
# for x in range (1,a+1) :
#     if (a%x==0) :
#         count = count +1
# if (count >=3) :
#     print('Composite')
# else:
#     print('Prime')
#WAP to display all the prime numbers from 1 to 100
for a in range (1,101) :
    count = 0
    for x in range(1,a+1) :
        if (a%x==0) :
            count = count + 1
    if (count == 2) :
        print(a)