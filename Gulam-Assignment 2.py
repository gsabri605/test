#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1.What are the two values of the Boolean data type? How do you write them');get_ipython().run_line_magic('pinfo', 'them')

Ans:   
      The value of Boolean data types are "True & False" in binary format it is consider as "0 & 1"
      
     a=True
     b=False
     type(a)
     type(b)
     


# In[1]:


a=True
b=False
type(a)
type(b)


# In[ ]:


get_ipython().set_next_input('2. What are the three different types of Boolean operators');get_ipython().run_line_magic('pinfo', 'operators')

Ans:  
     The three different types of Boolean oprators are
     
      1) AND
      2) Or
      3) NOT or AND NOT


# In[ ]:


3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).

Ans:
 
       True       True       
       True       False
       False      True
       False      False
       
       
       
       AND Operator          OR Operator         NOT Operator
         
         True                 True                False    False
         False                True                False    True
         False                True                True     False
         False                False               True     True


# In[ ]:


get_ipython().set_next_input('4. What are the values of the following expressions');get_ipython().run_line_magic('pinfo', 'expressions')
1) (5 > 4) and (3 == 5)
2) not (5 > 4)
3) (5 > 4) or (3 == 5)
4) not ((5 > 4) or (3 == 5))
5) (True and True) and (True == False)
6) (not False) or (not True)

Ans :

      1) False
      2) False
      3) True
      4) False
      5) False
      6) True


# In[ ]:


get_ipython().set_next_input('5. What are the six comparison operators');get_ipython().run_line_magic('pinfo', 'operators')

Ans :
    
      1) >
      2) ==
      3) <
      4) >=
      5) <=
      6) and 
      7) or
      8) not
         


# In[ ]:


6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.

Ans:

      "=" It is a assignment operator which is denoted as equal to symbol
      This is used to assign the value to a variable
      
      "==" It is a equal to operator which is used to compare the opreands 
        It compare two values , if values are same return True if not return False.


# In[ ]:


7. Identify the three blocks in this code:
spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
    print('bacon')
else:
    print('ham')
    print('spam')
    print('spam')


Ans :   


       1) if
       2) if
       3) else


# In[2]:


spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
else:
    print('ham')
    print('spam')
    print('spam')


# In[ ]:


8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.


Ans:

     


# In[3]:


spam=1
spam=2
if spam==1:
    print("Hello")
elif spam==2:
        print("Howdy")
else:
    print("Greetings")


# In[ ]:


get_ipython().set_next_input('9.If your programme is stuck in an endless loop, what keys you’ll press');get_ipython().run_line_magic('pinfo', 'press')

Ans:
     
       If we stuck in an endless loop just simply press CTRL + C to exit from the endless loop.


# In[ ]:


get_ipython().set_next_input('10. How can you tell the difference between break and continue');get_ipython().run_line_magic('pinfo', 'continue')

Ans:
    
     using break keyword in the programme we can treminate the condition at some point,
        
     using continue keyword we can continue to the next iteration whether the condition is true or false.


# In[ ]:


11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

Ans: python for loop  range (start,stop,step)


# In[7]:


for i in range(10):
    print(i)


# In[8]:


for i in range(0,10):
    print(i)


# In[11]:


for i in range(0,10,1):
    print(i)


# In[ ]:


12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

Ans:

     


# In[12]:


i=1
while(i<=10):
    print(i)
    i+=1


# In[ ]:


get_ipython().set_next_input('13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam');get_ipython().run_line_magic('pinfo', 'spam')

Ans :
    
      if we have function bacon then we can called with spam.bacon()

