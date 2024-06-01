#!/usr/bin/env python
# coding: utf-8

# <h1>Data Science Tools and Ecosystem</h1>

# In this notebook, Data Science tools and Ecosystem are summarized. 

# In[ ]:


#Objectives


# Objectives:    
# * Learn Python basics    
# * Learn R basics    
# * Learn GitHub basics
# 
# <h2>Author</h2>
# 
# Rebecca Miyagishima

# #Some of the popular languages that Data Scientists use are:

# In[8]:


languages = ["Python", "Scala", "Julia", "Java", "R"]
for number, letter in enumerate(languages,start=1):
    print(number, letter)


# In[9]:


#Some of the commonly used libraries used by Data Scientists include:


# In[11]:


libraries = ["Matplotlib", "TensorFlow", "scikit-learn", "Keras", "Pandas"]
for number, letter in enumerate(libraries,start=1):
    print(number, letter)


# In[12]:


#Data Science Tools


# In[14]:


pip install py-markdown-table


# In[18]:


from py_markdown_table.markdown_table import markdown_table
data = [
    {
        "Tools": "TensorFlow"
    },
    {
        "Tools":"Jupyter Notebook"
    },
    {
        "Tools":"Scikit-learn"
    },
    {
        "Tools":"SAS"
    }
]
markdown = markdown_table(data).get_markdown()
print(markdown)


# <h3>Below are a few examples of evaluating arithmetic expressions in Python.</h3>

# In[23]:


#This is a simple arithmetic expression to multiply then add integers


# In[24]:


x=3
y=4
z=5
print((x*y)+z)


# In[25]:


#This will convert 200 minutes to hours by dividing by 60


# In[26]:


min=int(input("Enter time in minutes"))
h=min//60
m=min%60
print("Hours=",h)
print("Minutes=",m)


# In[ ]:




