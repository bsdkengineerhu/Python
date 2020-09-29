#!/usr/bin/env python
# coding: utf-8

# <h3 align="center">Lists Unpacking</h3>

# In[ ]:


a,b,c,*other,d = [1,2,3,4,5,6,7,8,9,0] # this will work with set, tuple and normal (as in 1,2,3,4,5)
                                       # also. and it always store the variables as list, if more 
                                       # than one item, otherwise as int.

print(type(a))
print(b)
print(c)
print(other)
print(type(other))
print(d)

