#!/usr/bin/env python
# coding: utf-8

# In[2]:


num = int(input("enter a number"))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //=10
if num == sum:
    print(num,"is armstrong")
else:
    print(num,"is not armstrong")


# In[ ]:




