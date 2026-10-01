#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#numpy module 

import ipywidgets as widgets
from IPython.display import display

def numpy_module():
    message = """

    Welcome to the first numpy module! Here, we will learn about arrays represented in python. 

    NumPy (Numerical Python) is a Python library designed for working with numerical data 
    in Python. It is widely used in scientific computing, data analysis, and machine learning.

    Using Python, you can create N-Dimensional arrays, which have a fixed size, and are homogenous 
    (meaning that they only contain a singular data type). For example, you could have an array of only string 
    objects, or one of only integers, but not one containing both. 

    The numpy module also offers powerful mathematical functions for operating on arrays containing numbers. 

    In this course, we will focus on only 1-Dimensional and 2-Dimensional arrays.

    """

    border = 'black'

     result.value = f"""
    <div style="padding:10px; border:2px solid {border}; border-radius:6px;">
        {message}
    </div>
    """



