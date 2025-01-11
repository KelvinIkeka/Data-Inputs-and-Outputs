

import numpy as np
import pandas as pd


pwd


# #### List the files in your current directory with ls




ls


# -----
# #### NOTE! Common confusion point! Take note that all read input methods are called directly from pandas with pd.read_  , all output methods are called directly off the dataframe with df.to_
# 
# -------

# ### CSV Input

# In[55]:


df = pd.read_csv('example.csv')


# In[56]:


df


# In[57]:


df = pd.read_csv('example.csv',index_col=0)


# In[58]:


df


# In[59]:


df = pd.read_csv('example.csv')


# In[60]:


df


# ### CSV Output
# 
# Set index=False if you do not want to save the index , otherwise it will add a new column to the .csv file that includes your index and call it "Unnamed: 0" if your index did not have a name. If you do want to save your index, simply set it to True (the default value).

# In[61]:


df.to_csv('new_file.csv',index=False)


# ## HTML
# 
# Pandas can read table tabs off of HTML. This only works if your firewall isn't blocking pandas from accessing the internet!
# 
# Unless you're running the virtual environment included with the course, you may need to install <tt>lxml</tt>, <tt>htmllib5</tt>, and <tt>BeautifulSoup4</tt>.<br>
# In your terminal/command prompt run:
# 
#     conda install lxml
#     
#     or
#     
#     pip install lxml
#     
# Then restart Jupyter Notebook (you may need to restart your computer).
# (or use pip install if you aren't using the Anaconda Distribution)

# ## read_html
# 
# ### HTML Input
# 
# Pandas read_html function will read tables off of a webpage and return a list of DataFrame objects. NOTE: This only works with well defined <table> objects in the html on the page, this can not magically read in tables that are images on a page.

# In[62]:


tables = pd.read_html('https://en.wikipedia.org/wiki/World_population')


# In[63]:


len(tables) #tables


# ### Not Useful Tables
# Pandas found 26 tables on that page. Some are not useful:

# In[64]:


tables[0]


# ### Tables that need formatting

# Some will be misaligned, meaning you need to do extra work to fix the columns and rows:

# In[65]:


tables[1]


# In[66]:


world_pop = tables[1]


# In[67]:


world_pop.columns


# In[68]:


world_pop = world_pop['World population (millions, UN estimates)[14]'].drop('#',axis=1)


# In[69]:


world_pop.columns


# In[70]:


world_pop.columns = ['Countries', '2000', '2015', '2030 Est.']
world_pop = world_pop.drop(11,axis=0)


# In[71]:


world_pop


# ### Tables that are intact

# In[72]:


tables[6]


# ## Write to html Output
# 
# If you are working on a website and want to quickly output the .html file, you can use to_html

# In[73]:


df.to_html('simple.html',index=False)


# **read_html** is not perfect, but its quite powerful for such a simple method call!

# # Excel Files
# 
# Pandas can read in basic excel files (it will get errors if there are macros or extensive formulas relying on outside excel files), in general, pandas can only grab the raw information from an .excel file.
# 
# #### NOTE: Requires the openpyxl and xlrd library! Its provided for you in our environment, or simply install with:
# 
#     pip install openpyxl
#     pip install xlrd
#     
# Heavy excel users may want to check out this website: https://www.python-excel.org/
# 
# You can think of an excel file as a Workbook containin sheets, which for pandas means each sheet can be a DataFrame.
# 
# ## Excel file input with read_excel()

# In[74]:


df = pd.read_excel('my_excel_file.xlsx',sheet_name='First_Sheet')


# In[75]:


df


# ### What if you don't know the sheet name? Or want to run a for loop for certain sheet names? Or want every sheet?
# 
# Several ways to do this: https://stackoverflow.com/questions/17977540/pandas-looking-up-the-list-of-sheets-in-an-excel-file

# In[76]:


# Returns a list of sheet_names
pd.ExcelFile('my_excel_file.xlsx').sheet_names


# #### Grab all sheets

# In[77]:


excel_sheets = pd.read_excel('my_excel_file.xlsx',sheet_name=None)


# In[78]:


type(excel_sheets)


# In[79]:


excel_sheets.keys()


# In[80]:


excel_sheets['First_Sheet']


# ### Write to Excel File

# In[81]:


df.to_excel('example.xlsx',sheet_name='First_Sheet',index=False)


# # SQL Connections
# 
# #### NOTE: Highly recommend you explore specific libraries for your specific SQL Engine. Simple search for your database+python in Google and the top results should hopefully include an API.
# 
# * [MySQL](https://www.google.com/search?q=mysql+python)
# * [PostgreSQL](https://www.google.com/search?q=postgresql+python)
# * [MS SQL Server](https://www.google.com/search?q=MSSQLserver+python)
# * [Orcale](https://www.google.com/search?q=oracle+python)
# * [MongoDB](https://www.google.com/search?q=mongodb+python)
# 
# Let's review pandas capabilities by using SQLite, which comes built in with Python.
# 
# ## Example SQL Database (temporary in your RAM)
# 
# You will need to install sqlalchemy with:
# 
#     pip install sqlalchemy
#     
# to follow along. To understand how to make a connection to your own database, make sure to review: https://docs.sqlalchemy.org/en/13/core/connections.html

# In[82]:


from sqlalchemy import create_engine


# In[83]:


temp_db = create_engine('sqlite:///:memory:')


# ### Write to Database

# In[85]:


tables[6]


# In[86]:


pop = tables[6]


# In[87]:


pop.to_sql(name='populations',con=temp_db)


# ### Read from SQL Database

# In[89]:


# Read in an entire table
pd.read_sql(sql='populations',con=temp_db)


# In[92]:


# Read in with a SQL Query
pd.read_sql_query(sql="SELECT Country FROM populations",con=temp_db)


# It is difficult to generalize pandas and SQL, due to a wide array of issues, including permissions,security, online access, varying SQL engines, etc... Use these ideas as a starting off point, and you will most likely need to do your own research for your own situation.
