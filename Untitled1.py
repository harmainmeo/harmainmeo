#!/usr/bin/env python
# coding: utf-8

# # LCM OF TWO NUMBERS

# In[1]:


x,y=15,20
if (x>y):
    max=x
else:
    max=y
while(True):
    if (max%x==0 and max%y==0):
        print(max)
        break;
    max=max+1

