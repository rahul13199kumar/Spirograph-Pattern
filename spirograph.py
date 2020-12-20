#!/usr/bin/env python
# coding: utf-8

# In[5]:


import turtle

turtle.bgcolor("black") 
turtle.pensize(2)
turtle.speed(0)

for i in range(6):
    for colours in ["red","magenta","blue","cyan","green","green","white","grey"]:
        turtle.color(colours)
        turtle.star(100)
        turtle.left(10)
        
turtle.hideturtle()


# In[ ]:





# In[ ]:




