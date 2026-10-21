#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#numpy module 

import ipywidgets as widgets
from IPython.display import display

def numpy_module_p1():
    message = """
    
    <div style="line-height: 1.3;">
    
    <p> Welcome to the first numpy module! Here, we will learn about arrays represented in python.</p> 

    <p> NumPy (Numerical Python) is a Python library designed for working with numerical data 
    in Python. It is widely used in scientific computing, data analysis, and machine learning.</p>

    <p>Using Python, you can create N-Dimensional arrays, which have a fixed size, and are homogenous 
    (meaning that they only contain a singular data type). For example, you could have an array of only string 
    objects, or one of only integers, but not one containing both. On the other hand, lists do not have a fixed size, and can be heterogenous (while tuples 
    have a fixed size, and are heterogenous). </p> 

    <p>The numpy module also offers powerful mathematical functions for operating on arrays containing numbers.</p> 

    <p>In this course, we will focus on only 1-Dimensional and 2-Dimensional arrays.</p>

    </div>
    
    """

    border = 'black'
    
    result = widgets.HTML()
    
    result.value = f"""
    <div style="padding:10px; border:2px solid {border}; border-radius:6px;">
        {message}
    </div>
    """

    display(result)

import base64 as _b64


def numpy_module_q1():

    message = """
    <p>
    <div style="line-height: 1.3;">
    Q1) Imagine that you are working in a neuroscience lab, and have been asked
    to store numerical neural spike information to do analysis on. You will not
    have to change the information once you store the data. What should you
    store it with?
    </p>
    
    Choose your answer from the dropdown menu, but do <b> not </b> re run the previous cell again, or it will remove your answer.
    </div>
    """

    result = widgets.HTML()

    result.value = f"""
    <div style="
        padding:10px;
        border:2px solid black;
        border-radius:6px;
    ">
        {message}
    </div>
    """

    display(result)

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

    return answer

def check_q1(answer):
    _64 = _b64.b64decode(
        "YXNzZXJ0IGFuc3dlciA9PSAiYXJyYXkiCg=="
    )
    exec(_64.decode())

def numpy_module_p2():
    
    message = """

    <div style="line-height: 1.3;">

    <p> Now, let's look at an actual array, and explore its characteristics. </p> 

    <p> This is an example of a 1-D array. Its <b> size </b> is the number of elements the array contains, in this case, five. 
    The <b> dimension size </b> is the number of axes it has, which would be one, being a 1-D array. The <b> shape </b> specifies the number of elements
    per each axis, written in the form rows x columns (therefore applying to 2-D arrays). Lastly, its <b> type </b> is the type of elements in the 
    array. </p>

    </div>
    """

    border = 'black'
    
    result = widgets.HTML()
    
    result.value = f"""
    <div style="padding:10px; border:2px solid {border}; border-radius:6px;">
        {message}
    </div>
    """

    display(result)
    
    values = [4, 6, 8, 10, 12]

    boxes = []
    
    for value in values:
        box = widgets.HTML(
            value=f"""
            <div style="
                width: 70px;
                height: 55px;
                border: 1px solid gray;
                display: flex;
                align-items: center;
                justify-content: center;
                color: red;
                font-weight: bold;
                font-size: 18px;
            ">
                {value}
            </div>
            """
        )
        boxes.append(box)

    array_display = widgets.HBox(boxes)

    display(array_display)

    message_2 = """ <p> Size: 5 </p> 
    <p> Dimension Size: 1 </p>
    <p> Shape: (5,) </p>
    <p> Type: int64 (meaning that it is an integer) </p>
    """

    display(widgets.HTML(value=message_2))

def numpy_module_p3():
    message = """
    <div style="line-height: 1.3;">

    <p>

    Brainstorm some potential applications of arrays, and write them down here (specifically where you would use an array over a list/tupple).

    </p>
    </div> 

    """
    import ipywidgets as widgets
    from IPython.display import display
    
    result = widgets.HTML()

    result.value = f"""
    <div style="
        padding:10px;
        border:2px solid black;
        border-radius:6px;
    ">
        {message}
    </div>
    """
    

    response = widgets.Textarea(
        placeholder="Enter your response here...",
        layout=widgets.Layout(width="100%", height="150px")
    )

    submit = widgets.Button(
        description="Save Answer"
    )

    saved_answer = widgets.Output()

    def save_answer(b):
        with saved_answer:
            saved_answer.clear_output()
            print(response.value)

    submit.on_click(save_answer)

    display(response, submit, saved_answer)


def numpy_module_p4():
    message = """
    <div style="line-height: 1.3;">

    <p>

    Now we will look at two dimensional arrays. They look as follows (below),
    and this example has almost the one dimensional one, except for its
    dimension size (which is two).
    </div>

    <p>
    """

    values = [[4, 6, 8, 10, 12],
          [4, 5, 2, 1, 5]]

    rows = []

    for value in values:
        boxes = []

        for i in value:
            box = widgets.HTML(
            value=f"""
            <div style="
                width: 70px;
                height: 55px;
                border: 1px solid gray;
                display: flex;
                align-items: center;
                justify-content: center;
                color: red;
                font-weight: bold;
                font-size: 18px;
            ">
                {i}
            </div>
            """
            )

            boxes.append(box)

        row = widgets.HBox(boxes)
        rows.append(row)

    
    message_2 = """ <p> Size: 10 </p> 
    <p> Dimension Size: 2 </p>
    <p> Shape: (2, 5) </p>
    <p> Type: int64 (meaning that it is an integer) </p>
    """

    display(widgets.HTML(value=message_2))


    
def numpy_module_p5():
    import ipywidgets as widgets
    from IPython.display import display
    
    message = """

    <div style="line-height: 1.3;">

    <p>

    Upload a pdf of a diagram showing the axes for a two dimensional array. 

    </p>
    </div>

    """

    upload = widgets.FileUpload(
        accept='.pdf',
        multiple=False
    )

    display(upload)
    
    

    
