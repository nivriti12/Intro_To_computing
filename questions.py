
import numpy as np
import ipywidgets as widgets
from IPython.display import display
from IPython.utils.io import capture_output
from html import escape

MAX_ATTEMPTS = 3

# Preserve attempt history when the setup cell is rerun
if "_question_state" not in globals():
    _question_state = {}

if "_student_submissions" not in globals():
    _student_submissions = {}


def numpy_module_q1():

    message = """
    <div style="
        padding: 10px;
        border: 2px solid black;
        border-radius: 6px;
        line-height: 1.5;
    ">
        <strong>Q1.</strong> Create a 1-D array with
        the following fruits: apples, pears, bananas
        (in that order). Print the array.

        <p>
            Store your array in a variable named
            <code>fruits</code>.
            You have three attempts to answer correctly.
        </p>
    </div>
    """

    display(widgets.HTML(value=message))


# Cell magic to execute the student's real Python code
# and capture its printed output
def student_q1(line, cell):

    namespace = get_ipython().user_ns

    # Prevent an earlier answer from being reused
    namespace.pop("fruits", None)

    error = None

    with capture_output() as captured:
        try:
            exec(compile(cell, "<student_q1>", "exec"),
                 namespace, namespace)
        except Exception as e:
            error = e

    # Display the actual output to the student
    captured.show()

    if error is not None:
        print(f"{type(error).__name__}: {error}")

    _student_submissions["q1"] = {
        "stdout": captured.stdout,
        "error": error
    }


get_ipython().register_magic_function(
    student_q1, "cell", "student_q1"
)



def check_q1():

    from IPython import get_ipython
    import numpy as np

    # Access the student's Jupyter notebook namespace
    notebook = get_ipython().user_ns

    # Check that the student created the variable
    assert "fruits" in notebook

    fruits = notebook["fruits"]

    # Check that it is a NumPy array
    assert isinstance(fruits, np.ndarray)

    # Check dimensions and shape
    assert fruits.ndim == 1
    assert fruits.shape == (3,)

    # Check contents and order
    expected = np.array(["apples", "pears", "bananas"])

    assert np.array_equal(fruits, expected)

    # Retrieve the output captured by the student's code cell
    submissions = notebook.get("_student_submissions", {})
    submission = submissions.get("q1")

    assert submission is not None
    assert submission["error"] is None

    # Check the actual printed output
    expected_output = np.array2string(expected)

    assert submission["stdout"].strip() == expected_output



def run_check(check_function):

    question_id = (
        check_function.__module__,
        check_function.__name__
    )

    if question_id not in _question_state:
        _question_state[question_id] = {
            "attempts": 0,
            "finished": False,
            "correct": False
        }

    state = _question_state[question_id]

    result = widgets.HTML()

    if state["finished"]:

        if state["correct"]:
            message = "✅ <b>You already answered this correctly.</b>"
            border = "green"
        else:
            message = "⛔ <b>No attempts remaining.</b>"
            border = "gray"

    else:

        try:
            check_function()

            message = "✅ <b>Correct!</b>"
            border = "green"

            state["finished"] = True
            state["correct"] = True

        except AssertionError:

            state["attempts"] += 1
            remaining = MAX_ATTEMPTS - state["attempts"]

            if remaining > 0:
                message = (
                    f"❌ <b>Incorrect.</b> "
                    f"{remaining} attempt"
                    f"{'s' if remaining != 1 else ''} remaining."
                )
            else:
                message = (
                    "❌ <b>Incorrect. "
                    "No attempts remaining.</b>"
                )
                state["finished"] = True

            border = "red"

        except Exception as e:

            message = (
                f"⚠️ <b>Grader error:</b> "
                f"{escape(type(e).__name__)}"
            )
            border = "orange"

    result.value = f"""
    <div style="
        padding: 10px;
        border: 2px solid {border};
        border-radius: 6px;
    ">
        {message}
    </div>
    """

    display(result)
