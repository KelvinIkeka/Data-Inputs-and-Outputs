#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'><img src='../Pierian_Data_Logo.png'/></a>
# ___
# <center><em>Copyright by Pierian Data Inc.</em></center>
# <center><em>For more information, visit us at <a href='http://www.pieriandata.com'>www.pieriandata.com</a></em></center>

# # Inputs and Outputs
# 
# **NOTE: Typically we will just be either reading csv files directly or using pandas-datareader to pull data from the web. Consider this lecture just a quick overview of what is possible with pandas (we won't be working with SQL or Excel files in this course)**

# ## Data Input and Output
# 
# This notebook is the reference code for getting input and output, pandas can read a variety of file types using its pd.read_ methods. Let's take a look at the most common data types:

# In[1]:


import numpy as np
import pandas as pd


# ## Check out the references here! 
# 
# **This is the best online resource for how to read/write to a variety of data sources!**
# 
# https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html
# 
# ----
# ----

# <table border="1" class="colwidths-given docutils">
# <colgroup>
# <col width="12%" />
# <col width="40%" />
# <col width="24%" />
# <col width="24%" />
# </colgroup>
# <thead valign="bottom">
# <tr class="row-odd"><th class="head">Format Type</th>
# <th class="head">Data Description</th>
# <th class="head">Reader</th>
# <th class="head">Writer</th>
# </tr>
# </thead>
# <tbody valign="top">
# <tr class="row-even"><td>text</td>
# <td><a class="reference external" href="https://en.wikipedia.org/wiki/Comma-separated_values">CSV</a></td>
# <td><a class="reference internal" href="#io-read-csv-table"><span class="std std-ref">read_csv</span></a></td>
# <td><a class="reference internal" href="#io-store-in-csv"><span class="std std-ref">to_csv</span></a></td>
# </tr>
# <tr class="row-odd"><td>text</td>
# <td><a class="reference external" href="https://www.json.org/">JSON</a></td>
# <td><a class="reference internal" href="#io-json-reader"><span class="std std-ref">read_json</span></a></td>
# <td><a class="reference internal" href="#io-json-writer"><span class="std std-ref">to_json</span></a></td>
# </tr>
# <tr class="row-even"><td>text</td>
# <td><a class="reference external" href="https://en.wikipedia.org/wiki/HTML">HTML</a></td>
# <td><a class="reference internal" href="#io-read-html"><span class="std std-ref">read_html</span></a></td>
# <td><a class="reference internal" href="#io-html"><span class="std std-ref">to_html</span></a></td>
# </tr>
# <tr class="row-odd"><td>text</td>
# <td>Local clipboard</td>
# <td><a class="reference internal" href="#io-clipboard"><span class="std std-ref">read_clipboard</span></a></td>
# <td><a class="reference internal" href="#io-clipboard"><span class="std std-ref">to_clipboard</span></a></td>
# </tr>
# <tr class="row-even"><td>binary</td>
# <td><a class="reference external" href="https://en.wikipedia.org/wiki/Microsoft_Excel">MS Excel</a></td>
# <td><a class="reference internal" href="#io-excel-reader"><span class="std std-ref">read_excel</span></a></td>
# <td><a class="reference internal" href="#io-excel-writer"><span class="std std-ref">to_excel</span></a></td>
# </tr>
# <tr class="row-odd"><td>binary</td>
# <td><a class="reference external" href="http://www.opendocumentformat.org">OpenDocument</a></td>
# <td><a class="reference internal" href="#io-ods"><span class="std std-ref">read_excel</span></a></td>
# <td>&#160;</td>
# </tr>
# <tr class="row-even"><td>binary</td>
# <td><a class="reference external" href="https://support.hdfgroup.org/HDF5/whatishdf5.html">HDF5 Format</a></td>
# <td><a class="reference internal" href="#io-hdf5"><span class="std std-ref">read_hdf</span></a></td>
# <td><a class="reference internal" href="#io-hdf5"><span class="std std-ref">to_hdf</span></a></td>
# </tr>
# <tr class="row-odd"><td>binary</td>
# <td><a class="reference external" href="https://github.com/wesm/feather">Feather Format</a></td>
# <td><a class="reference internal" href="#io-feather"><span class="std std-ref">read_feather</span></a></td>
# <td><a class="reference internal" href="#io-feather"><span class="std std-ref">to_feather</span></a></td>
# </tr>
# <tr class="row-even"><td>binary</td>
# <td><a class="reference external" href="https://parquet.apache.org/">Parquet Format</a></td>
# <td><a class="reference internal" href="#io-parquet"><span class="std std-ref">read_parquet</span></a></td>
# <td><a class="reference internal" href="#io-parquet"><span class="std std-ref">to_parquet</span></a></td>
# </tr>
# <tr class="row-odd"><td>binary</td>
# <td><a class="reference external" href="https://msgpack.org/index.html">Msgpack</a></td>
# <td><a class="reference internal" href="#io-msgpack"><span class="std std-ref">read_msgpack</span></a></td>
# <td><a class="reference internal" href="#io-msgpack"><span class="std std-ref">to_msgpack</span></a></td>
# </tr>
# <tr class="row-even"><td>binary</td>
# <td><a class="reference external" href="https://en.wikipedia.org/wiki/Stata">Stata</a></td>
# <td><a class="reference internal" href="#io-stata-reader"><span class="std std-ref">read_stata</span></a></td>
# <td><a class="reference internal" href="#io-stata-writer"><span class="std std-ref">to_stata</span></a></td>
# </tr>
# <tr class="row-odd"><td>binary</td>
# <td><a class="reference external" href="https://en.wikipedia.org/wiki/SAS_(software)">SAS</a></td>
# <td><a class="reference internal" href="#io-sas-reader"><span class="std std-ref">read_sas</span></a></td>
# <td>&#160;</td>
# </tr>
# <tr class="row-even"><td>binary</td>
# <td><a class="reference external" href="https://docs.python.org/3/library/pickle.html">Python Pickle Format</a></td>
# <td><a class="reference internal" href="#io-pickle"><span class="std std-ref">read_pickle</span></a></td>
# <td><a class="reference internal" href="#io-pickle"><span class="std std-ref">to_pickle</span></a></td>
# </tr>
# <tr class="row-odd"><td>SQL</td>
# <td><a class="reference external" href="https://en.wikipedia.org/wiki/SQL">SQL</a></td>
# <td><a class="reference internal" href="#io-sql"><span class="std std-ref">read_sql</span></a></td>
# <td><a class="reference internal" href="#io-sql"><span class="std std-ref">to_sql</span></a></td>
# </tr>
# <tr class="row-even"><td>SQL</td>
# <td><a class="reference external" href="https://en.wikipedia.org/wiki/BigQuery">Google Big Query</a></td>
# <td><a class="reference internal" href="#io-bigquery"><span class="std std-ref">read_gbq</span></a></td>
# <td><a class="reference internal" href="#io-bigquery"><span class="std std-ref">to_gbq</span></a></td>
# </tr>
# </tbody>
# </table>

# -----
# ----

# # Reading in a  CSV
# Comma Separated Values files are text files that use commas as field delimeters.<br>
# Unless you're running the virtual environment included with the course, you may need to install <tt>xlrd</tt> and <tt>openpyxl</tt>.<br>
# In your terminal/command prompt run:
# 
#     conda install xlrd
#     conda install openpyxl
# 
# Then restart Jupyter Notebook.
# (or use pip install if you aren't using the Anaconda Distribution)
# 
# ## Understanding File Paths
# 
# You have two options when reading a file with pandas:
# 
# 1. If your .py file or .ipynb notebook is located in the **exact** same folder location as the .csv file you want to read, simply pass in the file name as a string, for example:
#     
#         df = pd.read_csv('some_file.csv')
#         
# 2. Pass in the entire file path if you are located in a different directory. The file path must be 100% correct in order for this to work. For example:
# 
#         df = pd.read_csv("C:\\Users\\myself\\files\\some_file.csv")

# #### Print your current directory file path with pwd

# In[53]:


pwd


# #### List the files in your current directory with ls

# In[54]:


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
