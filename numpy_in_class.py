def numpy_module_in_class_activity():
    message = """
    <div style="line-height: 1.3;">

    <p>

    Download sensors.dat from Canvas. 
    This activitiy will use file sensors.dat,
    which contains 32 simulated voltage measurements (V) from four vibration sensors: each row is a measurement and each column is a sensor.​
    </div>

    <p>
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
    display(result)

    
