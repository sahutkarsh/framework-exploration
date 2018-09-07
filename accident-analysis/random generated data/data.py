
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd


# In[2]:

columns = ['Incident Type', 'Primary Cause', 'Cause Class', 'Cause Type', 'Working Condition', 'Machine Condition',
           'SOP Requirement', 'SOP Availability', 'SOP Adequacy', 'SOP Compliance']


# In[3]:

data_dict = {}


# In[4]:

data_dict['Incident Type'] = ['Injury', 'Near Miss', 'Property Damage']
data_dict['Primary Cause'] = ['Dashing/Collision', 'Derailment', 'Energy Isolation', 'Road Incident', 'Slip/Trip/Fall',
                              'Process Incidents', 'Occupational Illness', 'Equipment Machinery Damage', 'Material Handling',
                              'Lifting Tool Tackles', 'Structural Integrity', 'Working at Height']
data_dict['Cause Class'] = ['Behaviour', 'Process']
data_dict['Cause Type'] = ['Unsafe Act', 'Unsafe Act & Unsafe Condition', 'Unsafe Act by Other', 'Unsafe Condition']
data_dict['Working Condition'] = ['Group Working', 'Single Working', 'Not a Working Place']
data_dict['Machine Condition'] = ['M/C Idle', 'M/C Working', 'Not Applicable']
data_dict['SOP Requirement'] = ['SOP Required', 'SOP Not Required', 'Not Known']
data_dict['SOP Availability'] = ['SOP Available', 'SOP Not Available', 'Not Known']
data_dict['SOP Adequacy'] = ['SOP Adequate', 'SOP Not Adequate', 'Not Known']
data_dict['SOP Compliance'] = ['SOP Followed', 'SOP Not Followed', 'Not Known']


# In[5]:

data_df = pd.DataFrame()
size = 1000


# In[6]:

for column in columns:
    n_class = len(data_dict[column])
    data_df[column] = np.random.randint(n_class, size=size)
    data_df[column] = data_df[column].map(lambda item: data_dict[column][item])


# In[7]:

data_df.to_csv('data.csv', index=False)

