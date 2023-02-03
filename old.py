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

pt_network['Mean_Munich'] = values
pt_network

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

pt_network['Mean_FFB'] = values
pt_network

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

pt_network['Mean_Starnberg'] = values
pt_network_Gilching = pt_network

pt_network_Gilching
