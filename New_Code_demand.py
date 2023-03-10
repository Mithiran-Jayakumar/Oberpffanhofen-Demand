#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import sys
import os
from tkinter import Tk
from tkinter.filedialog import askdirectory, askopenfilename

basis_file = pd.read_csv(r'https://github.com/Mithiran-Jayakumar/Oberpffanhofen-Demand/blob/main/basis_data.csv')
#basis_file

pt_network = pd.read_csv(r'https://github.com/Mithiran-Jayakumar/Oberpffanhofen-Demand/blob/main/pt_network_shuttle_reduced.csv')
pt_network = pt_network[['stat_name', 'stat_id', 'lat', 'lon', 'route']]
#pt_network

Bus_stops = pt_network['stat_name']
bus_stops_1 = []
for i in Bus_stops:
    word = i.split(',')[0]
    X = word.split('.')[0]
    bus_stops_1.append(X)
bus_stops_1

pt_network ['bus_stops_1'] = bus_stops_1
pt_network["Mean_Munich_U6"] = 0
pt_network["Mean_Munich_S8"] = 0
pt_network["Mean_FFB"] = 0
pt_network["Mean_Starnberg"] = 0
pt_network["Mean_Gauting"] = 0
pt_network["Mean_Herrsching"] = 0
#pt_network

column = pt_network.columns
df_result = pd.DataFrame(columns=column)
for x in range(0,10):
    stop_name = basis_file['Zone'][x]
    mean_munich_U6 = basis_file['Mean_Munich_U6'][x]
    mean_munich_S8 = basis_file['Mean_Munich_S8'][x]
    mean_FFB = basis_file['Mean_FFB'][x]
    mean_Starnberg = basis_file['Mean_Starnberg'][x]
    mean_Gauting = basis_file['Mean_Gauting'][x]
    mean_Herrsching = basis_file['Mean_Herrsching'][x]
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
        max_sum = mean_munich_U6*num
        mean = mean_munich_U6
        values = random_distribution(num_values, max_sum, mean)
        
        df_pt_network["Mean_Munich_U6"] = values
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
        max_sum = mean_munich_S8*num
        mean = mean_munich_S8
        values = random_distribution(num_values, max_sum, mean)
        
        df_pt_network["Mean_Munich_S8"] = values
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
        
        def random_distribution(num_values, max_sum, mean):
            values = []
            for i in range(num_values):
                value = random.uniform(0, (max_sum - sum(values))/(num_values-i))
                values.append(value)
            scale = mean * num_values / sum(values)
            values = [value * scale for value in values]
            return values
    
        num_values = df_pt_network.shape[0]
        max_sum = mean_Gauting*num
        mean = mean_Gauting
        values = random_distribution(num_values, max_sum, mean)
        
        df_pt_network["Mean_Gauting"] = values
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
        max_sum = mean_Herrsching*num
        mean = mean_Herrsching
        values = random_distribution(num_values, max_sum, mean)
        
        df_pt_network["Mean_Herrsching"] = values
        df_pt_network
        
        df_result = pd.concat([df_result,df_pt_network],axis=0,join="inner",ignore_index=True)

df_result
demand_data = df_result.to_csv()
#print (demand_data)
