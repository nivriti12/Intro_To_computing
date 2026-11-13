def numpy_module_in_class_activity():
    import numpy as np
    import ipywidgets as widgets
    from IPython.display import display

    # ---- Load the data ----
    import urllib.request
    url = "https://raw.githubusercontent.com/nivriti12/Intro_To_computing/refs/heads/main/sensors.dat"
    lines = urllib.request.urlopen(url).read().decode().splitlines()
    data = np.loadtxt(lines, delimiter=",")
    n_rows, n_cols = data.shape

    # How many rows to show at the top and bottom
    n_head = 3
    n_tail = 3

    # ---- Small styles for the grid ----
    cell_style = """
        width:72px; height:30px;
        border:2px solid gray; border-radius:4px;
        display:flex; align-items:center; justify-content:center;
        font-family:monospace; font-size:12px; color:#d22;
    """
    header_style = """
        width:72px; height:24px;
        display:flex; align-items:center; justify-content:center;
        font-weight:bold; font-size:12px;
    """
    row_label_style = """
        width:60px; height:30px;
        display:flex; align-items:center; justify-content:flex-end;
        padding-right:6px; font-weight:bold; font-size:12px;
    """
    ellipsis_style = """
        width:72px; height:20px;
        display:flex; align-items:center; justify-content:center;
        font-size:14px; color:gray;
    """
    row_style = "display:flex; gap:4px; margin-bottom:4px;"

    def make_row(r):
        cells = f'<div style="{row_label_style}">Row {r}</div>'
        for c in range(n_cols):
            cells += f'<div style="{cell_style}">{data[r, c]:.3f}</div>'
        return f'<div style="{row_style}">{cells}</div>'

    # Column headings
    header = f'<div style="{row_label_style}"></div>'
    for c in range(n_cols):
        header += f'<div style="{header_style}">Sensor {c + 1}</div>'
    grid = f'<div style="{row_style}">{header}</div>'

    # First few rows
    for r in range(n_head):
        grid += make_row(r)

    # "..." row to show rows are skipped
    dots = f'<div style="{row_label_style} height:20px;">&#8942;</div>'
    for c in range(n_cols):
        dots += f'<div style="{ellipsis_style}">&#8942;</div>'
    grid += f'<div style="{row_style}">{dots}</div>'

    # Last few rows
    for r in range(n_rows - n_tail, n_rows):
        grid += make_row(r)

    message = f"""
    <div style="line-height: 1.3;">

    <p>

    In Class Activity 18: 
    This activity will use file sensors.dat,
    which contains 32 simulated voltage measurements (V) from 
    four vibration sensors: each row is a measurement and each column is a sensor. The data can be seen below.
    </p>
    <p>
    The file sensors.dat has already been loaded into a variable called data, which you should use for the rest of the activity.  

    {grid}

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

def numpy_2():
        message = f"""
    <div style="line-height: 1.3;">

    <p>

    Q1) Use np.mean() and np.std() to calculate the mean and 
    standard deviation for each sensor. Store the results in mean_voltage and std_voltage, and print both arrays. Use the appropriate axis.​  
    </p>
    
    {grid}

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

    
