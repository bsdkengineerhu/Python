#!/usr/bin/env python
# coding: utf-8

# <h3 align="center">Sets Methods</h3>

# In[ ]:


my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

# .difference()
# .discard()
# .difference_update()
# .intersection()
# .isdisjoint()
# .issubset()
# .issuperset()
# .union()

print("\ndifference")
print(my_set.difference(your_set)) # returns unique in my_set
print(my_set)

print("\ndiscard")
print(my_set.discard(5)) # returns None
print(my_set)

print("\ndifference_update")
print(my_set.difference_update(your_set)) # returns None and updates my set with unique difference values
print(my_set)

my_set = {1,2,3,4,5}

print("\nintersection")
print(my_set.intersection(your_set))
print(my_set & your_set)

print("\nisdisjoint")
print(my_set.isdisjoint(your_set)) # returns False since 4,5 is common in both
my_set = {1,2,3}
print(my_set.isdisjoint(your_set))

print("\nissubset")
print(my_set.issubset(your_set)) # returns False since 1,2,3 in my_set is not in your_set
my_set = {4,6,8}
print(my_set.issubset(your_set)) # returns True since all elements of my_set is in your_set.

print("\nissuperset")
print(my_set.issuperset(your_set))
print(your_set.issuperset(my_set))

print("\nunion")
my_set = {1,2,3,4,5}
print(my_set.union(your_set))
# or
print(my_set | your_set)

