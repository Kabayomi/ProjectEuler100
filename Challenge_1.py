'''
Challenge 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

'''
# My Solution
multiples = []
for num in range(0,1000,1):
    if num%3==0 or num%5==0:
        multiples.append(num)
answer = sum(multiples)
print ("The answer is ", answer) #233168




# Pythonic Solution from the Internet
x = sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0)
print(x)