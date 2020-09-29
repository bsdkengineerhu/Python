#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Data Hiding: An objects attributes may or may not be visible outside the class definition. You
# need to name attributes with a double underscore prefix, and those attributes then are not be
# directly visible to outsiders.

class car():
    __maxspeed = 0
    __name = ''
    
    def __init__(self):
        self.__show()
    
    def __show(self):
        self.__maxspeed=200
        self.__name='supercar'
    
    def drive(self):
        print('driving')
        print(self.__maxspeed)
        print(self.__name)
    
    def setspeed(self,speed):
        self.__maxspeed = speed
        
redcar = car()
redcar.drive()
redcar.setspeed(100)
redcar.drive()

