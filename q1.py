MAX_ATTEMPTS = 3

# Stores attempts/status separately for each question
_question_state = {}

import base64 as _b64
import numpy as np
import ipywidgets as widgets
from IPython.display import display

def run_check(check_function, *args):
    from numpy_module.py import *args
    
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

    # Don't allow more checks after correct answer
    # or after 3 failed attempts
    if state["finished"]:

        if state["correct"]:
            message = "✅ <b>You already answered this correctly.</b>"
            border = "green"

        else:
            message = "⛔ <b>No attempts remaining.</b>"
            border = "gray"

        result.value = f"""
        <div style="
            padding:10px;
            border:2px solid {border};
            border-radius:6px;
        ">
            {message}
        </div>
        """

        display(result)
        return

    try:
        # Run whichever checker was passed into run_check
        *args()

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

            border = "red"

        else:

            message = "❌ <b>Incorrect. No attempts remaining.</b>"
            border = "red"

            state["finished"] = True

    except Exception as e:

        # Grader errors do NOT use an attempt
        message = (
            f"⚠️ <b>Grader error:</b> "
            f"{type(e).__name__}: {e}"
        )

        border = "orange"

    result.value = f"""
    <div style="
        padding:10px;
        border:2px solid {border};
        border-radius:6px;
    ">
        {message}
    </div>
    """

    display(result)

