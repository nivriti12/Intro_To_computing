import base64 as _b64
import urllib.request
import numpy as np
import ipywidgets as widgets
from IPython.display import display

SENSORS_URL = "https://raw.githubusercontent.com/nivriti12/Intro_To_computing/refs/heads/main/sensors.dat"
MAX_ATTEMPTS = 3

# Keeps track of how many tries each question has used
_attempts = {}
_solved = {}


def _load_sensors():
    lines = urllib.request.urlopen(SENSORS_URL).read().decode().splitlines()
    return np.loadtxt(lines, delimiter=",")


def _show(message, border):
    result = widgets.HTML()
    result.value = f"""
    <div style="padding:10px; border:2px solid {border}; border-radius:6px;">
        {message}
    </div>
    """
    display(result)


def numpy_module_q1():
    message = """
    <div style="line-height: 1.3;">
    <p>
    Q2) Using the sensor data you loaded into <code>data</code>, calculate the
    <b>mean voltage</b> across all of the measurements and sensors.
    Store your result in a variable called <code>mean_value</code>.
    </p>
    <p>
    Then run <code>check_q2(mean_value)</code> to check your answer.
    You have <b>3 attempts</b>.
    </p>
    </div>
    """
    _show(message, "black")


def _check_q1(answer):
    _code = _b64.b64decode(
        "YXNzZXJ0IG5wLmFsbGNsb3NlKG5wLmFzYXJyYXkoYW5zd2VyLCBkdHlwZT1mbG9hdCksIG5wLm1lYW4oZGF0YSwgYXhpcz0wKSwgYXRvbD0xZS02KQo="
    )
    data = _load_sensors()
    exec(_code.decode(), {"np": np, "answer": answer, "data": data})


def run_check_limited(question_id, check_function, answer, hint=""):
    """Runs a check with a limited number of attempts per question."""

    # Already solved: don't use up attempts
    if _solved.get(question_id):
        _show("✅ <b>You already got this one right!</b>", "green")
        return

    used = _attempts.get(question_id, 0)

    # Out of attempts
    if used >= MAX_ATTEMPTS:
        _show(
            f"🔒 <b>No attempts left.</b> You've used all {MAX_ATTEMPTS} attempts "
            "for this question. Ask your instructor or TA for help.",
            "gray",
        )
        return

    # The answer must be 4 numbers (one per sensor) before it counts as an attempt
    try:
        arr = np.asarray(answer, dtype=float)
        if arr.shape != (4,):
            raise ValueError
    except (TypeError, ValueError):
        _show(
            "⚠️ <b>Your answer should contain 4 numbers, one mean per sensor.</b> "
            f"Your variable has shape <code>{np.shape(answer)}</code>. "
            "This did not use an attempt.",
            "orange",
        )
        return

    try:
        check_function(answer)
        _solved[question_id] = True
        _show("✅ <b>Correct!</b>", "green")

    except AssertionError:
        used += 1
        _attempts[question_id] = used
        left = MAX_ATTEMPTS - used

        if left > 0:
            _show(
                f"❌ <b>Incorrect.</b> {hint} "
                f"You have <b>{left}</b> attempt{'s' if left != 1 else ''} left.",
                "red",
            )
        else:
            _show(
                f"❌ <b>Incorrect.</b> You've used all {MAX_ATTEMPTS} attempts "
                "for this question. Ask your instructor or TA for help.",
                "red",
            )

    except Exception as e:
        _show(f"⚠️ <b>Grader error:</b> {type(e).__name__}: {e}", "orange")


def check_q1(mean_value):
    """What students call: check_q2(mean_value)"""
    run_check_limited(
        "q2",
        _check_q2,
        mean_value,
        hint="Think about which axis runs down the rows (measurements) for each sensor.",
    )
