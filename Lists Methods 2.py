#!/usr/bin/env python
# coding: utf-8

# <h3 align="center">Lists Methods 2</h3>

# In[ ]:


li = ['a','b','c','d','e','d']
print(li.index('d')) # if that value is not there in the list, then it will throw an error and program will stop running.

# lookup:start:stop
print(li.index('d',0,6))

print('a' in li) # we use this to avoid the error.
print('x' in li)

name = 'imran'
print('r' in name) # we can use this with strings as well

print(li.count('d'))

