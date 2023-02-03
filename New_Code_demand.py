#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import numpy as np
import sys
import os
from tkinter import Tk
from tkinter.filedialog import askdirectory, askopenfilename



# In[80]:


basis_file = pd.read_excel(r"C:\Users\mithi\Desktop\TUM Lecture notes\Sem 3 (WiSe 22-23)\Project Seminar\MVV Data\Basis data.xlsx")
basis_file


# In[77]:


pt_network = pd.read_csv(r'C:\Users\mithi\Downloads\for-m-demand.csv')
pt_network = pt_network[['stat_name', 'stat_id', 'lat', 'lon', 'route']]
pt_network


# In[88]:


Bus_stops = pt_network['stat_name']
bus_stops_1 = []
for i in Bus_stops:
    word = i.split(',')[0]
    X = word.split('.')[0]
    bus_stops_1.append(X)
bus_stops_1


# In[89]:


pt_network ['bus_stops_1'] = bus_stops_1
pt_network


# In[90]:


basis_file


# In[91]:


pt_network ['bus_stops_1'] = bus_stops_1
pt_network["Mean_Munich"] = 0
pt_network["Mean_FFB"] = 0
pt_network["Mean_Starnberg"] = 0
#pt_network


# In[85]:


pt_network


# In[92]:


column = pt_network.columns
df_result = pd.DataFrame(columns=column)
for x in range(0,10):
    stop_name = basis_file['Zone'][x]
    mean_munich = basis_file['Mean_Munich'][x]
    mean_FFB = basis_file['Mean_FFB'][x]
    mean_Starnberg = basis_file['Mean_Starnberg'][x]
    df_pt_network = pt_network[pt_network['bus_stops_1']== stop_name]
    num = df_pt_network.shape[0]
    if df_pt_network.shape!=0:
        
        import random

        def random_distribution(num_values, max_sum, mean):
            values = []
            for i in range(num_values):
                value = random.uniform(0, (max_sum - sum(values))/(num_values-i))
                values.append(value)
            scale = mean * num_values / sum(values)
            values = [value * scale for value in values]
            return values
    
        num_values = df_pt_network.shape[0]
        max_sum = mean_munich*num
        mean = mean_munich
        values = random_distribution(num_values, max_sum, mean)
        
        df_pt_network["Mean_Munich"] = values
        df_pt_network
        
        
        def random_distribution(num_values, max_sum, mean):
            values = []
            for i in range(num_values):
                value = random.uniform(0, (max_sum - sum(values))/(num_values-i))
                values.append(value)
            scale = mean * num_values / sum(values)
            values = [value * scale for value in values]
            return values
    
        num_values = df_pt_network.shape[0]
        max_sum = mean_FFB*num
        mean = mean_FFB
        values = random_distribution(num_values, max_sum, mean)
        
        df_pt_network["Mean_FFB"] = values
        df_pt_network
        
        def random_distribution(num_values, max_sum, mean):
            values = []
            for i in range(num_values):
                value = random.uniform(0, (max_sum - sum(values))/(num_values-i))
                values.append(value)
            scale = mean * num_values / sum(values)
            values = [value * scale for value in values]
            return values
    
        num_values = df_pt_network.shape[0]
        max_sum = mean_Starnberg*num
        mean = mean_Starnberg
        values = random_distribution(num_values, max_sum, mean)
        
        df_pt_network["Mean_Starnberg"] = values
        df_pt_network
        
        df_result = pd.concat([df_result,df_pt_network],axis=0,join="inner",ignore_index=True)


# In[87]:


df_result


# In[98]:


demand_data = df_result.to_csv()
print (demand_data)


# In[61]:


import random

def random_distribution(num_values, max_sum, mean):
    values = []
    for i in range(num_values):
        value = random.uniform(0, (max_sum - sum(values))/(num_values-i))
        values.append(value)
    scale = mean * num_values / sum(values)
    values = [value * scale for value in values]
    return values

num_values = 12
max_sum = 1242.98
mean = 138.11
values = random_distribution(num_values, max_sum, mean)
print(values)


# In[10]:


pt_network['Mean_Munich'] = values
pt_network


# In[62]:


import random

def random_distribution(num_values, max_sum, mean):
    values = []
    for i in range(num_values):
        value = random.uniform(0, (max_sum - sum(values))/(num_values-i))
        values.append(value)
    scale = mean * num_values / sum(values)
    values = [value * scale for value in values]
    return values

num_values = 12
max_sum = 1242.98
mean = 138.11
values = random_distribution(num_values, max_sum, mean)
print(values)


# In[65]:


pt_network['Mean_FFB'] = values
pt_network


# In[64]:


import random

def random_distribution(num_values, max_sum, mean):
    values = []
    for i in range(num_values):
        value = random.uniform(0, (max_sum - sum(values))/(num_values-i))
        values.append(value)
    scale = mean * num_values / sum(values)
    values = [value * scale for value in values]
    return values

num_values = 12
max_sum = 74.07
mean = 8.23
values = random_distribution(num_values, max_sum, mean)
print(values)


# In[57]:


pt_network['Mean_Starnberg'] = values
pt_network_Gilching = pt_network


# In[56]:


pt_network_Gilching


# In[ ]:




