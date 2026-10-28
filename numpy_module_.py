def numpy_module_1():

    import ipywidgets as widgets
    from IPython.display import display

    message = """
    <div style="line-height: 1.3;">

        <p>Welcome to the first NumPy module! Here, we will learn about arrays in Python.</p>

        <p>NumPy (Numerical Python) is a Python library designed for working with numerical data.
        It is widely used in scientific computing, data analysis, and machine learning.</p>

        <p>Using Python, you can create N-dimensional arrays, which have a fixed size and
        typically contain elements of a single data type. For example, you could have an
        array containing only strings or one containing only integers, rather than mixing
        strings and integers in a standard numerical array. In contrast, Python lists can
        change in size and can contain different data types. Tuples have a fixed size but
        can also contain different data types.</p>

        <p>NumPy also offers powerful mathematical functions for operating on arrays
        containing numbers.</p>

        <p>In this course, we will focus on one-dimensional (1-D) and
        two-dimensional (2-D) arrays.</p>

    </div>
    """

    border = "black"

    result = widgets.HTML(
        value=f"""
        <div style="padding:10px; border:2px solid {border}; border-radius:6px;">
            {message}
        </div>
        """
    )

    display(result)


def numpy_module_2():

    import numpy as np
    import ipywidgets as widgets
    from IPython.display import display

    message = """
    <div style="line-height: 1.3;">
        <p>Below is an example of a 1-D array. Let's explore its characteristics.</p>
    </div>
    """

    display(widgets.HTML(value=message))

    # Create a 1-D NumPy array
    values = np.array([4, 6, 8, 10, 12])

    # Display each array element
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
                box-sizing: border-box;
            ">
                {value}
            </div>
            """
        )
        boxes.append(box)

    array_display = widgets.HBox(boxes)
    display(array_display)

    # Display the array characteristics
    message_2 = f"""
    <div style="line-height: 1.5;">

        <p>
        An array's <strong>size</strong> is the total number of elements it contains,
        which in this case is five. Its <strong>number of dimensions</strong> is the
        number of axes it has, which is one for a 1-D array. The <strong>shape</strong>
        specifies the number of elements along each axis. For a 1-D array, the shape
        contains one value, while for a 2-D array, it is written as (rows, columns).
        Lastly, the <strong>data type</strong> identifies the type of elements stored
        in the array.
        </p>

        <p>
            <strong>Size:</strong> {values.size}<br>
            <strong>Dimension Size:</strong> {values.ndim}<br>
            <strong>Shape:</strong> {values.shape}<br>
            <strong>Type:</strong> {values.dtype}
        </p>

        <p>The NumPy attributes used to identify these characteristics are:</p>

        <p>
            <strong>Size:</strong> <code>array_name.size</code><br>
            <strong>Dimension Size:</strong> <code>array_name.ndim</code><br>
            <strong>Shape:</strong> <code>array_name.shape</code><br>
            <strong>Type:</strong> <code>array_name.dtype</code>
        </p>

        <p><strong>Example:</strong> Print the size of the array below.</p>

        <div style="font-family: monospace; line-height: 1.6;">
            <p>v1 = np.array([7, 2, 9, 10])</p>
            <p>print(v1.size)</p>
        </div>

        <div style="
            color: #B8860B;
            font-family: monospace;
            line-height: 1.6;
            margin-top: 5px;
        ">
            <strong>Output:</strong> 4
        </div>

    </div>
    """

    border = "black"

    result = widgets.HTML(
        value=f"""
        <div style="padding:10px; border:2px solid {border}; border-radius:6px;">
            {message_2}
        </div>
        """
    )

    display(result)
