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
   "id": "c5425f18-7944-46ec-bf86-eccee7b11cfa",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "invalid literal for int() with base 10: '5.6'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "File \u001b[1;32mc:\\Users\\AM\\Downloads\\assignment_2 (2).py:24\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[39m'''\u001b[39;00m\n\u001b[0;32m      7\u001b[0m \u001b[39mBecause these are variables, we can modify their values!\u001b[39;00m\n\u001b[0;32m      8\u001b[0m \n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m     20\u001b[0m \n\u001b[0;32m     21\u001b[0m \u001b[39m'''\u001b[39;00m\n\u001b[0;32m     23\u001b[0m name \u001b[39m=\u001b[39m \u001b[39minput\u001b[39m(\u001b[39m'\u001b[39m\u001b[39mPlease enter a name: \u001b[39m\u001b[39m'\u001b[39m)\n\u001b[1;32m---> 24\u001b[0m age \u001b[39m=\u001b[39m \u001b[39mint\u001b[39;49m(\u001b[39minput\u001b[39;49m(\u001b[39m'\u001b[39;49m\u001b[39mPlease enter an age: \u001b[39;49m\u001b[39m'\u001b[39;49m))\n\u001b[0;32m     25\u001b[0m height \u001b[39m=\u001b[39m \u001b[39mfloat\u001b[39m(\u001b[39minput\u001b[39m(\u001b[39m'\u001b[39m\u001b[39mPlease enter a height: \u001b[39m\u001b[39m'\u001b[39m))\n\u001b[0;32m     26\u001b[0m is_student \u001b[39m=\u001b[39m \u001b[39mbool\u001b[39m(\u001b[39minput\u001b[39m(\u001b[39m'\u001b[39m\u001b[39mPlease enter whether or not you are a student: \u001b[39m\u001b[39m'\u001b[39m))\n",
      "\u001b[1;31mValueError\u001b[0m: invalid literal for int() with base 10: '5.6'"
     ]
    }
   ],
   "source": [
    "# Variable Manipulation\n",
    "\n",
    "##### ASSIGNMENT STARTS HERE #####\n",
    "\n",
    "'''\n",
    "Because these are variables, we can modify their values!\n",
    "\n",
    "Please enter in whatever values you'd like to display. \n",
    "\n",
    "What does it output?\n",
    "\n",
    "They can be real or fake, it does not matter!\n",
    "\n",
    "That said - what happens when you input the same values?\n",
    "\n",
    "ASSIGNMENT GOAL:\n",
    "- Make \"Variable Manipulation\" cell output types match first cell\n",
    "\n",
    "\n",
    "'''\n",
    "\n",
    "name = input('Please enter a name: ')\n",
    "age = int(input('Please enter an age: '))\n",
    "height = float(input('Please enter a height: '))\n",
    "is_student = bool(input('Please enter whether or not you are a student: '))\n",
    "\n",
    "\n",
    "\n",
    "displayValues(name,age,height,is_student)\n",
    "\n",
    "##### ASSIGNMENT ENDS HERE #####"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "819b4c91-e024-4ccb-b7d9-f50debfd9289",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'displayValues' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "File \u001b[1;32mc:\\Users\\AM\\Downloads\\assignment_2 (2).py:30\u001b[0m\n\u001b[0;32m     25\u001b[0m height \u001b[39m=\u001b[39m \u001b[39mfloat\u001b[39m(\u001b[39minput\u001b[39m(\u001b[39m'\u001b[39m\u001b[39mPlease enter a height: \u001b[39m\u001b[39m'\u001b[39m))\n\u001b[0;32m     26\u001b[0m is_student \u001b[39m=\u001b[39m \u001b[39mbool\u001b[39m(\u001b[39minput\u001b[39m(\u001b[39m'\u001b[39m\u001b[39mPlease enter whether or not you are a student: \u001b[39m\u001b[39m'\u001b[39m))\n\u001b[1;32m---> 30\u001b[0m displayValues(name,age,height,is_student)\n\u001b[0;32m     32\u001b[0m \u001b[39m##### ASSIGNMENT ENDS HERE #####\u001b[39;00m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'displayValues' is not defined"
     ]
    }
   ],
   "source": [
    "# Variable Manipulation\n",
    "\n",
    "##### ASSIGNMENT STARTS HERE #####\n",
    "\n",
    "'''\n",
    "Because these are variables, we can modify their values!\n",
    "\n",
    "Please enter in whatever values you'd like to display. \n",
    "\n",
    "What does it output?\n",
    "\n",
    "They can be real or fake, it does not matter!\n",
    "\n",
    "That said - what happens when you input the same values?\n",
    "\n",
    "ASSIGNMENT GOAL:\n",
    "- Make \"Variable Manipulation\" cell output types match first cell\n",
    "\n",
    "\n",
    "'''\n",
    "\n",
    "name = input('Please enter a name: ')\n",
    "age = int(input('Please enter an age: '))\n",
    "height = float(input('Please enter a height: '))\n",
    "is_student = bool(input('Please enter whether or not you are a student: '))\n",
    "\n",
    "\n",
    "\n",
    "displayValues(name,age,height,is_student)\n",
    "\n",
    "##### ASSIGNMENT ENDS HERE #####"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "58a0f9bc-0a60-4a81-a36b-6d9ec03fb6ce",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name: Caleb  | Type: <class 'str'>\n",
      "Age: 17  | Type: <class 'int'>\n",
      "Height: 5.6  | Type: <class 'float'>\n",
      "Is Student: True  | Type: <class 'bool'>\n"
     ]
    }
   ],
   "source": [
    "# Variable Manipulation\n",
    "\n",
    "##### ASSIGNMENT STARTS HERE #####\n",
    "\n",
    "'''\n",
    "Because these are variables, we can modify their values!\n",
    "\n",
    "Please enter in whatever values you'd like to display. \n",
    "\n",
    "What does it output?\n",
    "\n",
    "They can be real or fake, it does not matter!\n",
    "\n",
    "That said - what happens when you input the same values?\n",
    "\n",
    "ASSIGNMENT GOAL:\n",
    "- Make \"Variable Manipulation\" cell output types match first cell\n",
    "\n",
    "\n",
    "'''\n",
    "def displayValues(name,age,height,is_student):\n",
    "\n",
    "    # Print the variables and their types\n",
    "    print(\"Name:\", name, \" | Type:\", type(name))\n",
    "    print(\"Age:\", age, \" | Type:\", type(age))\n",
    "    print(\"Height:\", height, \" | Type:\", type(height))\n",
    "    print(\"Is Student:\", is_student, \" | Type:\", type(is_student))\n",
    "\n",
    "\n",
    "name = str (input('Please enter a name: '))\n",
    "age = int (input('Please enter an age: '))\n",
    "height = float (input('Please enter a height: '))\n",
    "is_student = bool (input('Please enter whether or not you are a student: '))\n",
    "\n",
    "\n",
    "\n",
    "displayValues(name,age,height,is_student)\n",
    "\n",
    "##### ASSIGNMENT ENDS HERE #####"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "No kernel connected"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "No kernel connected"
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
