{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "cee26a35",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number:3\n",
      "3 is a prime number\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"Enter a number:\"))\n",
    "flag= False\n",
    "for i in range(2,num):\n",
    "    if(num%i==0):\n",
    "        flag=True\n",
    "        break\n",
    "if flag:\n",
    "    print(num, \"is not a prime number\")\n",
    "else:\n",
    "    print(num, \"is a prime number\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5fcccdbd",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
