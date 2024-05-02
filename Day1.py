#!/usr/bin/env python
# coding: utf-8

# In[3]:


#accept a number and display its table.           
number = int(input("Enter a number to display its multiplication table: "))
for i in range(1, 11):
   print(number, '*', i, '=', number * i)
 


# In[4]:


# 2: using switch ….case   display whether accepted character is vowel or not.
vowel = input("Enter character: ")
match vowel:
    case 'a':
        print("Value is vowel")
    case 'e':
        print("Value is vowel")
    case 'i':
        print("Value is vowel")
    case 'o':
        print("Value is vowel")
    case 'u':
        print("Value is vowel")
    case _:
        print("value is not a vowel")

# In[10]:


#Display numbers  1 to 10 using  While loop
i = 1
while i <= 10:
    print(i)
    i += 1


# In[11]:


#Display numbers from 3 to 30 except number 24  using while loop.
number = 3
while number <= 30:
    if number != 24:
        print(number)
    number += 1 


# In[14]:


def result(student_mark):
    if 90 <= student_mark <= 100:
        print("1st division")
    elif 70 <= student_mark <= 89:
        print("2nd division")
    elif 45 <= student_mark <= 69:
        print("3rd division")
    else:
        print("fail")
student_mark = int(input("Enter the student's marks: "))
result(student_mark)


# In[ ]:





# In[ ]:




