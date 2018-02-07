
# coding: utf-8

# In[1]:


cd /Users/apple/bme590s18_lecture03/


# In[84]:


cfile=open('everyone.csv','w')
import glob
list1=glob.glob('*.csv')
list1.remove('mlp6.csv')
list1.remove('everyone.csv')
print(list1)

                



                
                
                


# In[114]:


len(list1)


# In[127]:


mydata = []
for name in list1:
    with open(name) as infile:
        data = infile.read()
        data = data.replace('\n','')
        data = data.replace('\ufeff','')
        data = data.replace('# Firstname, lastname, NetID, Githubname, Teamname','')
        data = data.split(',')
        mydata.append(data)
mydata


# In[292]:


import pandas as pd
df =  pd.DataFrame(mydata,columns=['Firstname', 'lastname', 'NetID', 'Githubname', 'Teamname'])
df


# In[143]:


df.to_csv('everyone.csv', sep=',',index=False)


# In[264]:


def cameltest(x):
    return (x[4]!= x[4].lower() and x[4]!= x[4].upper())

a=0
for teamname in mydata:
    if cameltest(teamname)==False:
        a=a+1
        print(teamname[4])

import sys       
print('numer of non-camel:', a , file=sys.stdout)
        


# In[286]:


print('numer of non-camel:', len(Camel_Case) , file=sys.stdout)


# In[275]:


df['Teamname'][1].replace(' ','')


# In[189]:


def spacetest(x):
    return (x[4].find(' ')!=-1)

for teamname in mydata:
    if spacetest(teamname)==True:
        print(teamname[4])

     


# In[258]:


import csv
import json
for file in list1:
    File = open(file.replace('.csv','.json'), 'w')
    with open (file) as infile:
        Titles = ("FirstName","LastName","NetID","GithubID","GroupName")
        reader = csv.DictReader(infile, Titles)
        for row in reader:
            json.dump(row, File)
            File.write('\n')


# In[262]:


with open('zk28.json') as f:
    doc=json.load(f)
doc.values()

