#!/usr/bin/env python
# coding: utf-8

# In[33]:


#first iteration
import itertools 
  
a = ['A','T','T','C','A']
b = ['A','T','T','C','A']
c = ['A','T','T','C','G']


for (a,b,c) in zip(a,b,c):
    
    bpcount = 0
    
    Acount = 0
    Tcount = 0
    Ccount = 0
    Gcount = 0

    if a == "A":
        Acount += 1
        bpcount +=1
    else:
        Acount = Acount
        
    if b == "A":
        Acount += 1
        bpcount +=1
    else:
        Acount = Acount
    
    if c == "A":
        Acount += 1
        bpcount +=1
    else:
        Acount = Acount
#########   
    
    if a == "T":
        Tcount += 1
        bpcount +=1
    else:
        Tcount = Tcount
        
    if b == "T":
        Tcount += 1
        bpcount +=1
    else:
        Tcount = Tcount
    
    if c == "T":
        Tcount += 1
        bpcount +=1
    else:
        Tcount = Tcount
#########     
    
    if a == "C":
        Ccount += 1
        bpcount +=1
    else:
        Ccount = Ccount
        
    if b == "C":
        Ccount += 1
        bpcount +=1
    else:
        Ccount = Ccount
    
    if c == "C":
        Ccount += 1
        bpcount +=1
    else:
        Ccount = Ccount
 #########    
    
    if a == "G":
        Gcount += 1
        bpcount +=1
    else:
        Gcount = Gcount
        
    if b == "G":
        Gcount += 1
        bpcount +=1
    else:
        Gcount = Gcount
    
    if c == "G":
        Gcount += 1
        bpcount +=1
    else:
        Gcount = Gcount
    
    print('[', Acount,',', Tcount,',', Ccount,',', Gcount, ']', bpcount)
    
    if bpcount == 0:
        bpcount += 1
    else:
        bpcount == bpcount
    
    Aprop = Acount/bpcount
    Tprop = Tcount/bpcount
    Cprop = Ccount/bpcount
    Gprop = Gcount/bpcount
    
    print('[', Aprop,',', Tprop,',', Cprop,',', Gprop, ']')


'''num = ['A','T','T','C','A']
color = ['A','T','T','C','A']
value = ['A','T','T','C','G']
'''


# In[27]:


#first iteration w/ N
import itertools 
  
a = ['A','T','T','N','N']
b = ['A','N','C','N','N']
c = ['A','T','T','N','G']


for (a,b,c) in zip(a,b,c):
    
    bpcount = 0
    
    Acount = 0
    Tcount = 0
    Ccount = 0
    Gcount = 0

    if a == "A":
        Acount += 1
        bpcount +=1
    else:
        Acount = Acount
        
    if b == "A":
        Acount += 1
        bpcount +=1
    else:
        Acount = Acount
    
    if c == "A":
        Acount += 1
        bpcount +=1
    else:
        Acount = Acount
#########   
    
    if a == "T":
        Tcount += 1
        bpcount +=1
    else:
        Tcount = Tcount
        
    if b == "T":
        Tcount += 1
        bpcount +=1
    else:
        Tcount = Tcount
    
    if c == "T":
        Tcount += 1
        bpcount +=1
    else:
        Tcount = Tcount
#########     
    
    if a == "C":
        Ccount += 1
        bpcount +=1
    else:
        Ccount = Ccount
        
    if b == "C":
        Ccount += 1
        bpcount +=1
    else:
        Ccount = Ccount
    
    if c == "C":
        Ccount += 1
        bpcount +=1
    else:
        Ccount = Ccount
 #########    
    
    if a == "G":
        Gcount += 1
        bpcount +=1
    else:
        Gcount = Gcount
        
    if b == "G":
        Gcount += 1
        bpcount +=1
    else:
        Gcount = Gcount
    
    if c == "G":
        Gcount += 1
        bpcount +=1
    else:
        Gcount = Gcount
    
    print('[', Acount,',', Tcount,',', Ccount,',', Gcount, ']', bpcount)
    
    if bpcount == 0:
        bpcount += 1
    else:
        bpcount == bpcount
    
    Aprop = Acount/bpcount
    Tprop = Tcount/bpcount
    Cprop = Ccount/bpcount
    Gprop = Gcount/bpcount
    
    print('[', Aprop,',', Tprop,',', Cprop,',', Gprop, ']')

'''num = ['A','T','T','N','N']
color = ['A','N','C','N','N']
value = ['A','T','T','N','G']'''


# In[28]:


#second iteration (condensed if statements)
import itertools 
  
a = ['A','T','T','C','A']
b = ['A','T','T','C','A']
c = ['A','T','T','C','G']


for (a,b,c) in zip(a,b,c):
    
    bpcount = 0
    
    Acount = 0
    Tcount = 0
    Ccount = 0
    Gcount = 0
    
    if a == "A":
        Acount += 1
        bpcount += 1
    elif a == "T":
        Tcount += 1
        bpcount += 1
    elif a == "C":
        Ccount += 1
        bpcount += 1
    elif a == "G":
        Gcount += 1
        bpcount += 1
    else:
        bpcount == bpcount
        Acount == Acount
        Tcount == Tcount
        Ccount == Ccount
        Gcount == Gcount

##############################

    if b == "A":
        Acount += 1
        bpcount += 1
    elif b == "T":
        Tcount += 1
        bpcount += 1
    elif b == "C":
        Ccount += 1
        bpcount += 1
    elif b == "G":
        Gcount += 1
        bpcount += 1
    else:
        bpcount == bpcount
        Acount == Acount
        Tcount == Tcount
        Ccount == Ccount
        Gcount == Gcount

##############################

    if c == "A":
        Acount += 1
        bpcount += 1
    elif c == "T":
        Tcount += 1
        bpcount += 1
    elif c == "C":
        Ccount += 1
        bpcount += 1
    elif c == "G":
        Gcount += 1
        bpcount += 1
    else:
        bpcount == bpcount
        Acount == Acount
        Tcount == Tcount
        Ccount == Ccount
        Gcount == Gcount
        
    print('[', Acount,',', Tcount,',', Ccount,',', Gcount, ']', bpcount)
    
    if bpcount == 0:
        bpcount += 1
    else:
        bpcount == bpcount
        
##############################
    
    Aprop = Acount/bpcount
    Tprop = Tcount/bpcount
    Cprop = Ccount/bpcount
    Gprop = Gcount/bpcount
    
    print('[', Aprop,',', Tprop,',', Cprop,',', Gprop, ']')


'''num = ['A','T','T','C','A']
color = ['A','T','T','C','A']
value = ['A','T','T','C','G']
'''


# In[32]:


#second iteration (condensed if statements) w/ N
import itertools 
  
a = ['A','T','T','N','N']
b = ['A','N','C','N','N']
c = ['A','T','T','N','G']

for (a,b,c) in zip(a,b,c):
    
    bpcount = 0
    
    Acount = 0
    Tcount = 0
    Ccount = 0
    Gcount = 0
    
    if a == "A":
        Acount += 1
        bpcount += 1
    elif a == "T":
        Tcount += 1
        bpcount += 1
    elif a == "C":
        Ccount += 1
        bpcount += 1
    elif a == "G":
        Gcount += 1
        bpcount += 1
    else:
        bpcount == bpcount
        Acount == Acount
        Tcount == Tcount
        Ccount == Ccount
        Gcount == Gcount

##############################

    if b == "A":
        Acount += 1
        bpcount += 1
    elif b == "T":
        Tcount += 1
        bpcount += 1
    elif b == "C":
        Ccount += 1
        bpcount += 1
    elif b == "G":
        Gcount += 1
        bpcount += 1
    else:
        bpcount == bpcount
        Acount == Acount
        Tcount == Tcount
        Ccount == Ccount
        Gcount == Gcount

##############################

    if c == "A":
        Acount += 1
        bpcount += 1
    elif c == "T":
        Tcount += 1
        bpcount += 1
    elif c == "C":
        Ccount += 1
        bpcount += 1
    elif c == "G":
        Gcount += 1
        bpcount += 1
    else:
        bpcount == bpcount
        Acount == Acount
        Tcount == Tcount
        Ccount == Ccount
        Gcount == Gcount
        
    print('[', Acount,',', Tcount,',', Ccount,',', Gcount, ']', bpcount)
    
    if bpcount == 0:
        bpcount += 1
    else:
        bpcount == bpcount
        
##############################
    
    Aprop = Acount/bpcount
    Tprop = Tcount/bpcount
    Cprop = Ccount/bpcount
    Gprop = Gcount/bpcount
    
    print('[', Aprop,',', Tprop,',', Cprop,',', Gprop, ']')


'''a = ['A','T','T','N','N']
b = ['A','N','C','N','N']
c = ['A','T','T','N','G']'''


# In[35]:


#second iteration (condensed if statements) w/ N making a data frame
import itertools
import pandas as pd
  
a = ['A','T','T','N','N']
b = ['A','N','C','N','N']
c = ['A','T','T','N','G']

df = pd.DataFrame(columns = ["Aprop", "Tprop", "Cprop", "Gprop", "Aprop2", "Tprop2", "Cprop2", "Gprop2"])


for (a,b,c) in zip(a, b, c):
    
    bpcount = 0
    
    Acount = 0
    Tcount = 0
    Ccount = 0
    Gcount = 0
    
    if a == "A":
        Acount += 1
        bpcount += 1
    elif a == "T":
        Tcount += 1
        bpcount += 1
    elif a == "C":
        Ccount += 1
        bpcount += 1
    elif a == "G":
        Gcount += 1
        bpcount += 1
    else:
        bpcount == bpcount
        Acount == Acount
        Tcount == Tcount
        Ccount == Ccount
        Gcount == Gcount

##############################

    if b == "A":
        Acount += 1
        bpcount += 1
    elif b == "T":
        Tcount += 1
        bpcount += 1
    elif b == "C":
        Ccount += 1
        bpcount += 1
    elif b == "G":
        Gcount += 1
        bpcount += 1
    else:
        bpcount == bpcount
        Acount == Acount
        Tcount == Tcount
        Ccount == Ccount
        Gcount == Gcount

##############################

    if c == "A":
        Acount += 1
        bpcount += 1
    elif c == "T":
        Tcount += 1
        bpcount += 1
    elif c == "C":
        Ccount += 1
        bpcount += 1
    elif c == "G":
        Gcount += 1
        bpcount += 1
    else:
        bpcount == bpcount
        Acount == Acount
        Tcount == Tcount
        Ccount == Ccount
        Gcount == Gcount
        
    #print('[', Acount,',', Tcount,',', Ccount,',', Gcount, ']', bpcount)
    
    if bpcount == 0:
        bpcount += 1
    else:
        bpcount == bpcount
        
##############################
    
    Aprop = Acount/bpcount
    Tprop = Tcount/bpcount
    Cprop = Ccount/bpcount
    Gprop = Gcount/bpcount
    

    df = df.append({'Aprop' : Aprop, 'Tprop' : Tprop, 'Cprop' : Cprop, 'Gprop' : Gprop}, 
                ignore_index = True)
    
    
   
df


# In[6]:


#third itertaion (counting the sites)
import itertools
import pandas as pd
  
a = ['A','T','T','N','N']
b = ['A','N','C','N','N']
c = ['A','T','T','N','G']

df = pd.DataFrame(columns = ["Locus", "Aprop", "Tprop", "Cprop", "Gprop", "Aprop2", "Tprop2", "Cprop2", "Gprop2"])

site = 0

for locus in zip(a, b, c):
    
    site += 1
    
    Acount = locus.count("A")
    Tcount = locus.count("T")
    Ccount = locus.count("C")
    Gcount = locus.count("G")
    
    bpcount = Acount+Tcount+Ccount+Gcount
    
    if bpcount == 0:
        bpcount += 1
    else:
        bpcount == bpcount
        
    Aprop = Acount/bpcount
    Tprop = Tcount/bpcount
    Cprop = Ccount/bpcount
    Gprop = Gcount/bpcount
    
    df = df.append({'Locus' : site, 'Aprop' : Aprop, 'Tprop' : Tprop, 'Cprop' : Cprop, 'Gprop' : Gprop}, 
                ignore_index = True)
    
    
   
df


# In[35]:


#fourth iteration (with second population)
import itertools
import pandas as pd
  
a = ['A','T','T','N','N']
b = ['A','N','C','N','N']
c = ['A','T','T','N','G']

df = pd.DataFrame(columns = ["Locus", "Aprop", "Tprop", "Cprop", "Gprop"])

site = 0

for locus in zip(a, b, c):
    
    site += 1
    
    Acount = locus.count("A")
    Tcount = locus.count("T")
    Ccount = locus.count("C")
    Gcount = locus.count("G")
    
    bpcount = Acount+Tcount+Ccount+Gcount
    
    if bpcount == 0:
        bpcount += 1
    else:
        bpcount == bpcount
        
    Aprop = Acount/bpcount
    Tprop = Tcount/bpcount
    Cprop = Ccount/bpcount
    Gprop = Gcount/bpcount
    
    df = df.append({'Locus' : site, 'Aprop' : Aprop, 'Tprop' : Tprop, 'Cprop' : Cprop, 'Gprop' : Gprop}, 
                ignore_index = True)


    
d = ['C','T','C','N','C']
e = ['C','T','C','A','N']
f = ['C','T','T','N','G']

df2 = pd.DataFrame(columns = ["Locus", "Aprop2", "Tprop2", "Cprop2", "Gprop2"])

site2 = 0

for locus in zip(d, e, f):
    
    site2 += 1
    
    Acount2 = locus.count("A")
    Tcount2 = locus.count("T")
    Ccount2 = locus.count("C")
    Gcount2 = locus.count("G")
    
    bpcount2 = Acount2+Tcount2+Ccount2+Gcount2
    
    if bpcount2 == 0:
        bpcount2 += 1
    else:
        bpcount2 == bpcount2
        
    Aprop2 = Acount2/bpcount2
    Tprop2 = Tcount2/bpcount2
    Cprop2 = Ccount2/bpcount2
    Gprop2 = Gcount2/bpcount2
    
    df2 = df2.append({'Locus' : site2 ,'Aprop2' : Aprop2, 'Tprop2' : Tprop2, 'Cprop2' : Cprop2, 'Gprop2' : Gprop2}, 
                ignore_index = True)


combined = pd.merge(df, df2, on='Locus')

combined['Adiff'] = abs(combined['Aprop'] - combined['Aprop2'])
combined['Tdiff'] = abs(combined['Tprop'] - combined['Tprop2'])
combined['Cdiff'] = abs(combined['Cprop'] - combined['Cprop2'])
combined['Gdiff'] = abs(combined['Gprop'] - combined['Gprop2'])

combined['diff_score'] = combined[["Adiff","Tdiff","Cdiff","Gdiff"]].max(axis=1)

filtered = combined[combined.diff_score !=0]

filtered


# In[ ]:




