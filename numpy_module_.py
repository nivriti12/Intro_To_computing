def numpy_module_1():

    import ipywidgets as widgets
    from IPython.display import display

    message = """
    <div style="line-height: 1.3;">

        <p>Welcome to the first NumPy module! Here, we will learn about arrays in Python.</p>

        <p>NumPy (Numerical Python) is a Python library designed for working with numerical data.
        It is widely used in scientific computing, data analysis, and machine learning.</p>

        <p>Using Python, you can create N-dimensional arrays, which have a fixed size (<b> immutable </b>) and
         contain elements of a single data type (<b> homogenous </b>). For example, you could have an
        array containing only strings or one containing only integers, rather than mixing
        strings and integers in a standard numerical array. In contrast, Python lists can
        change in size (<b> mutable </b> and can contain different data types (<b> heterogenous </b>). Tuples have a fixed size (<b> immutable </b>) but
        can also contain different data types (<b> heterogenous </b>).</p>

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

    # Create a 1-D NumPy array
    values = np.array([4, 6, 8, 10, 12])

    # Generate the array boxes
    boxes = ""

    for value in values:
        boxes += f"""
        <div style="
            width: 70px;
            height: 55px;
            border: 2px solid gray;
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

    # Combine everything inside one border
    message = f"""
    <div style="
        border: 2px solid black;
        border-radius: 6px;
        padding: 12px;
        line-height: 1.5;
        font-family: Arial, sans-serif;
    ">

        <p>Below is an example of a 1-D array. Let's explore its characteristics.</p>

        <div style="
            display: flex;
            gap: 5px;
            margin: 15px 0;
        ">
            {boxes}
        </div>

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

        <p>The nummpy commands used to identify these characteristics are:</p>

        <p>
            <strong>Size:</strong> <code>array_name.size</code><br>
            <strong>Dimension Size:</strong> <code>array_name.ndim</code><br>
            <strong>Shape:</strong> <code>array_name.shape</code><br>
            <strong>Type:</strong> <code>array_name.dtype</code>
        </p>

        <p><strong>Example:</strong> Print the size of the array below.</p>

        <div style="
            font-family: monospace;
            line-height: 1.6;
        ">
            <p>v1 = np.array([7, 2, 9, 10])</p>
            <p>print(v1.size)</p>
        </div>

        <div style="
            color: #B8860B;
            font-weight: bold;
            margin-top: 5px;
        ">
            4 </div>
    </div>
    """

    display(widgets.HTML(value=message))

    
def numpy_module_3():

    import numpy as np
    import ipywidgets as widgets
    from IPython.display import display

    # Create a 2-D NumPy array
    values = np.array([
        [4, 6, 8, 10, 12],
        [14, 16, 18, 20, 22]
    ])

    # Generate the array boxes
    rows = ""

    for row in values:
        boxes = ""

        for value in row:
            boxes += f"""
            <div style="
                width: 70px;
                height: 55px;
                border: 2px solid gray;
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

        rows += f"""
        <div style="display: flex; gap: 5px;">
            {boxes}
        </div>
        """

    # Combine everything inside one border
    message = f"""
    <div style="
        border: 2px solid black;
        border-radius: 6px;
        padding: 12px;
        line-height: 1.5;
        font-family: Arial, sans-serif;
    ">

        <p>
            Now, let's look at two-dimensional arrays.
            As shown below, a 2-D array is similar to a
            1-D array, but it has two dimensions instead
            of one. Notice how its shape and dimension
            size differ from those of a 1-D array.
            NumPy also supports arrays with more than
            two dimensions, although they become harder
            to visualize beyond three dimensions.
        </p>

        <div style="
            display: flex;
            flex-direction: column;
            gap: 5px;
            margin: 15px 0;
        ">
            {rows}
        </div>

        <p>
            <strong>Size:</strong> {values.size}<br>
            <strong>Dimension Size:</strong> {values.ndim}<br>
            <strong>Shape:</strong> {values.shape}<br>
            <strong>Type:</strong> {values.dtype}
        </p>

    </div>
    """

    display(widgets.HTML(value=message))


def numpy_module_4():

    import ipywidgets as widgets
    from IPython.display import display
    from html import escape

    # Format Python code without changing comment colors
    def code(text):
        return f"""
        <div style="
            font-family: monospace;
            white-space: pre-wrap;
            line-height: 1.6;
            margin: 8px 0;
            color: black;
        ">{escape(text)}</div>
        """

    # Format outputs in golden-brown
    def output(text):
        return f"""
        <div style="
            font-family: monospace;
            white-space: pre-wrap;
            line-height: 1.6;
            color: #B8860B;
            font-weight: bold;
            margin: 5px 0 12px 0;
        ">{escape(text)}</div>
        """

    message = f"""
    <div style="
        border: 2px solid black;
        border-radius: 6px;
        padding: 12px;
        line-height: 1.5;
        font-family: Arial, sans-serif;
    ">

        <p>
            Now let's look at how to create an array using numpy. In order to make an array, you have to
            import NumPy as follows:
        </p>

        {code("import numpy as np")}

        <p>
            Following this, you can create one
            with the following command:
        </p>

        {code("np.array([elements])")}

        <p>Here are a few examples of array creation:</p>

        <p><strong>1. Using a list to make an array:</strong></p>

        {code("L1=[7.2,2,9,10]\nv1=np.array(L1)\nprint(v1)")}

        {output("[ 7.2  2.   9.  10. ]")}

        <p><strong>2. Attempting to make a homogeneous array:</strong></p>

        {code("L1=[7.2,2,9,10,'pop']\nv1=np.array(L1)\nprint(v1)")}

        {output("['7.2' '2' '9' '10' 'pop']")}

        {code("print(v1.dtype)")}

        {output("<U32")}

        {code("# Unicode string: all elements were converted to strings instead of some remaining floats.")}

        <p><strong>3. Using the range function to make an array:</strong></p>

        {code("L1=list(range(10))")}

        {output("[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]")}

        {code("v1=np.arange(10)")}

        {output("[0 1 2 3 4 5 6 7 8 9]")}

        <p><strong>4. Using list comprehension to make an array:</strong></p>

        {code("L2=[i**3 for i in L1]\nprint(L2)")}

        {output("[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]")}

        <p><strong>5. Creating a 2-D array with two lists:</strong></p>

        {code("L2=[[5.2,3,4],[9.1,0.1,0.3]]\nM=np.array(L2) #converts a list of lists to a 2D array\nprint(M)")}

        {output("[[5.2 3.  4. ]\n [9.1 0.1 0.3]]")}

    </div>
    """

    display(widgets.HTML(value=message))


def numpy_module_5():

    import ipywidgets as widgets
    from IPython.display import display

    values = [
        [4, 6, 8, 10, 12],
        [4, 5, 2, 1, 5]
    ]

    # Introduction and explanation
    message = """
    <div style="
        font-family: Arial, sans-serif;
        line-height: 1.5;
    ">

        <p>
            The next concept to learn is <strong>indexing</strong>,
            which allows you to access individual elements
            within an array.
        </p>

        <p>
            In a two-dimensional (2D) array, the elements
            are arranged in <strong>rows and columns</strong>.
            To access a specific element, you need to specify
            its row position and column position.
        </p>

        <p>The general format is:</p>

        <p style="font-family: monospace;">
            array_name[row_position, column_position]
        </p>

        <p>
            The first value identifies the <strong>row</strong>,
            and the second identifies the <strong>column</strong>.
        </p>

        <p>
            Take another look at the same 2D array from the
            previous example. Click on each element to reveal
            its index and see how its row and column positions
            identify its location within the array.
        </p>

    </div>
    """

    introduction = widgets.HTML(value=message)

    rows = []
    all_buttons = []

    # Output for the selected index
    index_output = widgets.HTML(
        value="<div style='min-height:25px;'></div>"
    )

    def button_clicked(button):

        # Reset all button colors
        for b in all_buttons:
            b.style.button_color = "white"

        # Highlight selected button
        button.style.button_color = "yellow"

        row_index, col_index = button.index

        index_output.value = f"""
        <div style="
            color: #B8860B;
            font-weight: bold;
            font-family: monospace;
            font-size: 16px;
            margin-top: 12px;
        ">
            Index: ({row_index}, {col_index})
        </div>
        """

    # Generate the interactive 2-D array
    for row_index, row_values in enumerate(values):

        boxes = []

        for col_index, value in enumerate(row_values):

            button = widgets.Button(
                description=str(value),
                layout=widgets.Layout(
                    width="70px",
                    height="55px",
                    border="2px solid gray",
                    margin="0 5px 0 0"
                )
            )

            button.style.button_color = "white"
            button.style.font_weight = "bold"
            button.style.text_color = "red"

            button.index = (row_index, col_index)

            button.on_click(button_clicked)

            boxes.append(button)
            all_buttons.append(button)

        row = widgets.HBox(
            boxes,
            layout=widgets.Layout(
                margin="0 0 5px 0"
            )
        )

        rows.append(row)

    array_display = widgets.VBox(
        rows,
        layout=widgets.Layout(
            margin="10px 0"
        )
    )

    # Put everything inside one border
    content = widgets.VBox(
        [
            introduction,
            array_display,
            index_output
        ],
        layout=widgets.Layout(
            border="2px solid black",
            padding="12px",
            width="100%"
        )
    )

    display(content)



