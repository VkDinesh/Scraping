#!/usr/bin/env python
# coding: utf-8

# In[1]:


import urllib


# In[2]:


import urllib.request


# In[3]:


wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"


# In[4]:


page=urllib.request.urlopen(wiki)


# In[5]:


pip install BeautifulSoup4


# In[6]:


from bs4 import BeautifulSoup


# In[7]:


soup = BeautifulSoup(page)


# In[8]:


print (soup.prettify())


# In[9]:


print(soup.title)


# In[10]:


soup.find_all('a')


# In[11]:


all_tables=soup.find_all('table')


# In[12]:


right_table=soup.find('table', class_='wikitable sortable plainrowheaders')
right_table


# In[13]:


#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') #To store second column data
    if len(cells)==6: #Only extract table body not heading
        A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))


# In[14]:


#import pandas to convert list to data frame
import pandas as pd
df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']=F
df['Former_Capital']=G
df


# In[ ]:




