#!/usr/bin/env python
# coding: utf-8

# <h3 align="center">Function Return</h3>

# In[ ]:


def sum1(num1, num2):
    def another_func(n1,n2):
        return n1 + n2
    return another_func

def sum2(num1, num2):
    def another_func2(n1,n2):
        return n1 + n2
    return another_func2(num1, num2) 

print(sum1(10,5))    # this will just return the address of the function
print(sum1(10,5)(5,8))    # this will give arguments to the another_func

# above is same as doing:
total = sum1(10,5)
print(total)
print(total(5,8))


print(sum2(10,5))

# print(another_func(45, 55))   # this will give error, because the function is actually undefined
                                # , and to call this function, first we will have to call the 
                                # parent function. So we can get the memory location of the 
                                # function.

