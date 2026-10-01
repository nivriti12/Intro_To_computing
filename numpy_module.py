#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#numpy module 

import ipywidgets as widgets
from IPython.display import display

def numpy_module_p1():
    message = """

    <p> Welcome to the first numpy module! Here, we will learn about arrays represented in python.</p> 

    <p> NumPy (Numerical Python) is a Python library designed for working with numerical data 
    in Python. It is widely used in scientific computing, data analysis, and machine learning.</p>

    <p>Using Python, you can create N-Dimensional arrays, which have a fixed size, and are homogenous 
    (meaning that they only contain a singular data type). For example, you could have an array of only string 
    objects, or one of only integers, but not one containing bothOn the other hand, lists do not have a fixed size, and can be heterogenous (while tuples 
    have a fixed size, and are heterogenous). </p> 

    <p>The numpy module also offers powerful mathematical functions for operating on arrays containing numbers.</p> 

    <p>In this course, we will focus on only 1-Dimensional and 2-Dimensional arrays.</p>

    """

    border = 'black'
    
    result = widgets.HTML()
    
    result.value = f"""
    <div style="padding:10px; border:2px solid {border}; border-radius:6px;">
        {message}
    </div>
    """

    display(result)

def numpy_module_q1():
    import ipywidgets as widgets
    from IPython.display import display

    answer = widgets.Dropdown(
    options=[
        ("Select an answer", None),
        ("List", "list"),
        ("Tuple", "tuple"),
        ("Array", "array")
    ],
    value=None,
    description="Answer:"
    )

    display(answer)



    
    



