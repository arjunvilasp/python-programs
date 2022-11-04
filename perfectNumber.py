{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1c1d85f2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a nhumber:7\n",
      "7 is not a perfect number\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"Enter a nhumber:\"))\n",
    "sum=0\n",
    "for i in range(1,num):\n",
    "    if(num%i==0):\n",
    "        sum+=i\n",
    "if num == sum :\n",
    "    print(num, \"is a perfect number\")\n",
    "else:\n",
    "    print(num, \"is not a perfect number\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ded5db91",
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
