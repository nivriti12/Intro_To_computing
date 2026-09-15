# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
#notebook with defined functions

# %%
# interactive plots: clicking 

# %matplotlib widget

import matplotlib.pyplot as plt
import numpy as np

def point_clicking():
    import matplotlib.pyplot as plt
    import numpy as np

    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 5, 3, 8, 6])

    fig, ax = plt.subplots()
    points = ax.scatter(x, y, s=80, picker=True)

    ax.set_title("Click a data point")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    message = ax.text(
        0.05, 0.95,
        "Click any point",
        transform=ax.transAxes,
        va="top"
    )

    def clicked(event):
        i = event.ind[0]

        message.set_text(
            f"You selected point {i+1}\n"
            f"x = {x[i]}, y = {y[i]}"
        )

        fig.canvas.draw_idle()

    fig.canvas.mpl_connect("pick_event", clicked)

    plt.show()



# %%
# %matplotlib widget

def click_on_plot():
    # %matplotlib widget

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_title("Click anywhere on the plot")

    point, = ax.plot([], [], "o", markersize=10)

    def onclick(event):
        if event.inaxes == ax:
            point.set_data([event.xdata], [event.ydata])
            fig.canvas.draw_idle()

    fig.canvas.mpl_connect("button_press_event", onclick)

    plt.show()


# %%
def select_region():

    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.widgets import RectangleSelector

    x = np.random.randn(100)
    y = np.random.randn(100)

    fig, ax = plt.subplots()
    ax.scatter(x, y)

    ax.set_title("Click and drag to select a region")

    def onselect(start, end):
        print(
            f"Selected region: "
            f"x = {start.xdata:.2f} to {end.xdata:.2f}, "
            f"y = {start.ydata:.2f} to {end.ydata:.2f}"
        )

    selector = RectangleSelector(
        ax,
        onselect,
        interactive=True,
        button=[1]
    )
    fig.selector = selector

    plt.show()


# %%

def show_outlier_animation():
    
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation
    from IPython.display import HTML
    
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    y = np.array([1, 2, 3, 4, 5, 6, 7, 8])

    moving_y = np.linspace(9, 18, 40)

    fig, ax = plt.subplots()

    ax.scatter(x, y)

    point, = ax.plot([9], [9], "o")
    line, = ax.plot([], [])

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 20)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Effect of an Outlier on a Regression Line")

    line_x = np.linspace(0, 10, 100)

    def update(i):

        all_x = np.append(x, 9)
        all_y = np.append(y, moving_y[i])

        slope, intercept = np.polyfit(all_x, all_y, 1)

        point.set_data([9], [moving_y[i]])
        line.set_data(line_x, slope * line_x + intercept)

        return point, line

    anim = FuncAnimation(
        fig,
        update,
        frames=len(moving_y),
        interval=100
    )

    plt.close(fig)

    return HTML(anim.to_jshtml())
