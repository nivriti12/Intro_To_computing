
import base64 as _b64
import numpy as np
import ipywidgets as widgets
from IPython.display import display

def check_q1(mean_value, data):
    _64 = _b64.b64decode(
        "CmFzc2VydCBtZWFuX3ZhbHVlID09IG5wLm1lYW4oZGF0YSksICJOb3QgcXVpdGUg4oCUIHRyeSBhZ2Fpbi4iCnByaW50KCLinJMgQ29ycmVjdCEiKQo="
    )
    exec(_64.decode())

def run_check(mean_value, data):
    global _attempts, _finished

    result = widgets.HTML()

    # Don't allow more checks after correct answer or 3 failed attempts
    if _finished:
        if _attempts >= MAX_ATTEMPTS:
            message = "⛔ <b>No attempts remaining.</b>"
            border = "gray"
        else:
            message = "✅ <b>You already answered this correctly.</b>"
            border = "green"

        result.value = f"""
        <div style="padding:10px; border:2px solid {border}; border-radius:6px;">
            {message}
        </div>
        """
        display(result)
        return

    try:
        check_q1(mean_value, data)

        message = "✅ <b>Correct!</b>"
        border = "green"
        _finished = True

    except AssertionError:
        _attempts += 1
        remaining = MAX_ATTEMPTS - _attempts

        if remaining > 0:
            message = (
                f"❌ <b>Incorrect.</b> "
                f"{remaining} attempt{'s' if remaining != 1 else ''} remaining."
            )
            border = "red"
        else:
            message = "❌ <b>Incorrect. No attempts remaining.</b>"
            border = "red"
            _finished = True

    except Exception as e:
        # Grader bugs do NOT use up an attempt
        message = f"⚠️ <b>Grader error:</b> {type(e).__name__}: {e}"
        border = "orange"

    result.value = f"""
    <div style="padding:10px; border:2px solid {border}; border-radius:6px;">
        {message}
    </div>
    """

    display(result)

