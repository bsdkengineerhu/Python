#!/usr/bin/env python
# coding: utf-8

# <h3 align="center">For Loops Dictionary</h3>

# In[ ]:


user = {
        'age': 45,
        'name': "john",
        'size': 10        
        }

for i in user:
    print(i)

for i in user.keys():
    print(i)

for i in user.values():
     print(i)

for i in user.items():  #it stores each pair as tuple, in a list (in a dict_items class).
     print(i)

print(user.items())
print(type(user.items()))
print(list(user.items()))

for k,v in user.items():
     print(k,v)

for i in user.items():
     k,v=i
     print(k,v)

