{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Connected to Python 3.9.9"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a243a742-8dc0-4348-8a96-b696936fff61",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 is even!\n",
      "1 is an odd number!\n",
      "2 is even!\n",
      "3 is an odd number!\n",
      "4 is even!\n",
      "5 is an odd number!\n",
      "6 is even!\n",
      "7 is an odd number!\n",
      "8 is even!\n",
      "9 is an odd number!\n",
      "Done!\n"
     ]
    }
   ],
   "source": [
    "# Looping Function\n",
    "\n",
    "def loop_function(x):\n",
    "\n",
    "    # Here is an example of a \"for\" loop\n",
    "    for i in range(x):\n",
    "\n",
    "        # Here is an example of a conditional statement\n",
    "        # If hte remainder of i divided by 2 is 0, then it is an even number\n",
    "        if i % 2 == 0:\n",
    "            print(i, \"is even!\")\n",
    "        else:\n",
    "            print(i, \"is an odd number!\")\n",
    "\n",
    "    print(\"Done!\")\n",
    "\n",
    "\n",
    "number_of_loops = 10\n",
    "\n",
    "loop_function(number_of_loops)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.9.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
