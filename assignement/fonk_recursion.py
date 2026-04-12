# n = int(input("Lütfen bir sayı giriniz\t:"))

# def fibonacci(n):

#    if n <= 1:
#        return n
#    else:
#        return(fibonacci(n-1) + fibonacci(n-2))

# x = n
# print("Fibonacci dizisi:")
# for i in range(x):
#     print(fibonacci(i))

#################################################################

# def yarila(cc):

#     print(cc)
#     cc//=2
#     if cc >= 4 : yarila(cc)
    
# yarila(125)

##################################################################

import turtle
turtle.speed(10)
def yarila(xx):
    # print(xx)
    turtle.forward(xx)
    turtle.right(90)
    xx -= 10  
    if xx>50 : yarila(xx)


yarila(500)


input()