{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5ee03734-c72d-4179-a046-c78410538ab1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import ipywidgets as widgets\n",
    "from IPython.display import display\n",
    "\n",
    "def run_check(check_function, *args):\n",
    "    result = widgets.HTML()\n",
    "\n",
    "    try:\n",
    "        check_function(*args)\n",
    "        message = \"✅ <b>Correct!</b>\"\n",
    "        border = \"green\"\n",
    "\n",
    "    except AssertionError:\n",
    "        message = \"❌ <b>Incorrect. Try again.</b>\"\n",
    "        border = \"red\"\n",
    "\n",
    "    except Exception as e:\n",
    "        message = f\"⚠️ <b>Grader error:</b> {type(e).__name__}: {e}\"\n",
    "        border = \"orange\"\n",
    "\n",
    "    result.value = f\"\"\"\n",
    "    <div style=\"padding:10px; border:2px solid {border}; border-radius:6px;\">\n",
    "        {message}\n",
    "    </div>\n",
    "    \"\"\"\n",
    "\n",
    "    display(result)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
