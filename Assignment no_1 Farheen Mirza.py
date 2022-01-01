#!/usr/bin/env python
# coding: utf-8

# In[5]:



print("Twinkle, twinkle, little star,\n",
                "\t How I wonder what you are!\n",
                        "\t\t Up above the world so high,\n",
                        "\t\t Like a diamond in the sky.\n",
      "Twinkle, twinkle, little star,\n",
                "\t How I wonder what you are\n")


# In[8]:


from platform import python_version

print(python_version())


# In[12]:


from datetime import date

today = date.today()
print("Today's date:", today)


# In[14]:


from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)	


# In[16]:


from math import pi

r = float(input ("Enter radius of circle : "))

print ("Area of the circle is: " + str(pi * r**2))


# In[29]:


FirstName = input("Input your First Name : ")
LastName = input("Input your Last Name : ")
print ("Hey  " + LastName + " " + FirstName)


# In[19]:


# Store input numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

# Add two numbers
sum = int(num1) + int(num2)

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


# In[ ]:




