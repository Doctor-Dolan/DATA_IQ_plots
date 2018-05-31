
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np

data=pd.read_csv('/users/robert/Documents/LEAP_Core clinical variables_09-03-18-withvalues.csv')


# In[5]:


print data.head


# In[6]:


newdata = data[['subjects','piq','fsiq','viq','group']]

newdata = newdata[newdata.piq != 999]
newdata = newdata[newdata.viq != 999]
newdata = newdata[newdata.fsiq != 999]

ASD_reg = newdata[newdata.group==2]
ASD_ID = newdata[newdata.group==4]

asdframes = [ASD_reg, ASD_ID]
ASD_All = pd.concat(asdframes)

TD_reg = newdata[newdata.group==1]
TD_ID = newdata[newdata.group==3]

frames = [TD_reg, TD_ID]
TD_All = pd.concat(frames)


# In[7]:


from numpy.random import normal
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

Piq_TD_reg=TD_reg[['piq']]
Piq_TD_reg_list=Piq_TD_reg.values.T.tolist()

Piq_TD_ID=TD_ID[['piq']]
Piq_TD_ID_list=Piq_TD_ID.values.T.tolist()

Piq_TD_All=TD_All[['piq']]
Piq_TD_All_list=Piq_TD_All.values.T.tolist()


#plt.hist(Piq_TD_reg_list, bins=40)
#plt.hist(Piq_TD_ID_list, bins=30)
plt.hist(Piq_TD_All_list, bins=50)


# In[8]:


Piq_ASD_reg=ASD_reg[['piq']]
Piq_ASD_reg_list=Piq_ASD_reg.values.T.tolist()

Piq_ASD_ID=ASD_ID[['piq']]
Piq_ASD_ID_list=Piq_ASD_ID.values.T.tolist()

Piq_ASD_All=ASD_All[['piq']]
Piq_ASD_All_list=Piq_ASD_All.values.T.tolist()


#plt.hist(Piq_ASD_reg_list, bins=40, color='red')
plt.hist(Piq_ASD_ID_list, bins=30, color='red')
#plt.hist(Piq_ASD_All_list, bins=50, color='red')


# In[9]:


fsiq_TD_reg=TD_reg[['fsiq']]
fsiq_TD_reg_list=fsiq_TD_reg.values.T.tolist()

fsiq_TD_ID=TD_ID[['fsiq']]
fsiq_TD_ID_list=fsiq_TD_ID.values.T.tolist()

fsiq_TD_All=TD_All[['fsiq']]
fsiq_TD_All_list=fsiq_TD_All.values.T.tolist()

fsiq_ASD_reg=ASD_reg[['fsiq']]
fsiq_ASD_reg_list=fsiq_ASD_reg.values.T.tolist()

fsiq_ASD_ID=ASD_ID[['fsiq']]
fsiq_ASD_ID_list=fsiq_ASD_ID.values.T.tolist()

fsiq_ASD_All=ASD_All[['fsiq']]
fsiq_ASD_All_list=fsiq_ASD_All.values.T.tolist()




# In[10]:


plt.hist(fsiq_TD_All_list, bins=50, color='green')
plt.hist(fsiq_TD_reg_list, bins=50, color='blue')


# In[11]:


viq_TD_reg=TD_reg[['viq']]
viq_TD_reg_list=viq_TD_reg.values.T.tolist()

viq_TD_ID=TD_ID[['viq']]
viq_TD_ID_list=viq_TD_ID.values.T.tolist()

viq_TD_All=TD_All[['viq']]
viq_TD_All_list=viq_TD_All.values.T.tolist()

viq_ASD_reg=ASD_reg[['viq']]
viq_ASD_reg_list=viq_ASD_reg.values.T.tolist()

viq_ASD_ID=ASD_ID[['viq']]
viq_ASD_ID_list=viq_ASD_ID.values.T.tolist()

viq_ASD_All=ASD_All[['viq']]
viq_ASD_All_list=viq_ASD_All.values.T.tolist()


# In[12]:


plt.hist(viq_TD_All_list, bins=50, color='green')
plt.hist(viq_TD_reg_list, bins=50, color='blue')



# In[13]:


plt.hist(viq_ASD_All_list, bins=50, color='red')
plt.hist(viq_ASD_reg_list, bins=50, color='yellow')



# In[14]:


plt.hist(fsiq_ASD_ID_list, bins=50, color='red')


# In[51]:


fig = plt.figure(figsize=(14,12))
ax = fig.add_subplot(111)
ax.hist(fsiq_ASD_All_list, bins=np.arange(0, 150, 2), alpha = 0.4, lw=3, color='r')
ax.hist(fsiq_TD_All_list, bins=np.arange(0, 150, 2), alpha = 0.6, lw=3, color='y')
ax.set_xlim(20,180)

