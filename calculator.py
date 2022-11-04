{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "9655f85c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter number 1:3\n",
      "Enter number 2:4\n",
      "Enter your choice\n",
      "1.ADD\n",
      "2.SUBTRACT\n",
      "3.MULTIPLY\n",
      "4.DIVISION\n",
      "5.MOD\n",
      "6.POWER\n",
      "1\n",
      "Result= 7\n"
     ]
    }
   ],
   "source": [
    "num1= int(input(\"Enter number 1:\"))\n",
    "num2= int(input(\"Enter number 2:\"))\n",
    "ch=input(\"Enter your choice\\n1.ADD\\n2.SUBTRACT\\n3.MULTIPLY\\n4.DIVISION\\n5.MOD\\n6.POWER\\n\")\n",
    "if(ch=='1'):\n",
    "    print(\"Result=\",num1+num2)\n",
    "elif(ch=='2'):\n",
    "    print(\"Result=\",num1-num2)\n",
    "elif(ch=='3'):\n",
    "    print(\"Result=\",num1*num2)   \n",
    "elif(ch=='4'):\n",
    "    print(\"Result=\",num1/num2)\n",
    "elif(ch=='5'):\n",
    "    print(\"Result=\",num1%num2)\n",
    "elif(ch=='6'):\n",
    "    print(\"Result=\",num1**num2)\n",
    "else:\n",
    "    print(\"invalid choice\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2b47405d",
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
