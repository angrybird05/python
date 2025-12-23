# printing 1 to 10 numbsers
for i in range (1,100):
    print(i)

# sum of 1 to 100
sum = 0
for i in range (1,101):
    sum = sum + i
print("Sum of 1 to 100 is:", sum)

   # creating functions 
def add(a,b):
    return a+b
print(add(8,8))

#function for max of 2 numbesrs
def max_num(a,b):
    if a > b:
        return a
    else:
        return b      

print(max_num(3,5))

#function for checking if a number is prime or not 

def prime(a):
    if a%2==0:
       return a
    else:
        return "a is not prime"
    

print(prime(11))

#function for reversing a number 

name = "ajay"

rev_name = name [::-1]

print(rev_name)

# couting vowels in a string
def count_vowels(s):
    count = 0
    vowels = "aeiouAEIOU"
    for char in s:
        if char in vowels:
            count += 1
    return count
string = "Hello World"
vowel_count = count_vowels(string)  
print("Number of vowels in the string:", vowel_count)

# factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))