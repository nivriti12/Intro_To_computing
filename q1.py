
import base64 as _b64
import numpy as np
import ipywidgets as widgets
from IPython.display import display

def check_q1(mean_value, data):
    _64 = _b64.b64decode(
        "CmFzc2VydCBtZWFuX3ZhbHVlID09IG5wLm1lYW4oZGF0YSksICJOb3QgcXVpdGUg4oCUIHRyeSBhZ2Fpbi4iCnByaW50KCLinJMgQ29ycmVjdCEiKQo="
    )
    exec(_64.decode())

def run_check(check_q1, data):
    result = widgets.HTML()

    try:
        check_q1(*args)
        message = "✅ <b>Correct!</b>"
        border = "green"

    except AssertionError:
        message = "❌ <b>Incorrect. Try again.</b>"
        border = "red"

    except Exception as e:
        message = f"⚠️ <b>Grader error:</b> {type(e).__name__}: {e}"
        border = "orange"

    result.value = f"""
    <div style="padding:10px; border:2px solid {border}; border-radius:6px;">
        {message}
    </div>
    """

    display(result)

