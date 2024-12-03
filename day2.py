#%%
import pandas as pd
import os
import sys
print (os.getcwd())
print (sys.version)
# %%
datadf = pd.read_csv("day1_data.txt", sep="  ", header=None,  names=["lista_a", "lista_b"])
print (datadf.shape)
datadf.head()

# %%
# %%
new_lista_a = datadf.lista_a.sort_values(ascending=True).values.tolist()
new_lista_b = datadf.lista_b.sort_values(ascending=True).values.tolist()
datadf["new_lista_a"]=new_lista_a
datadf["new_lista_b"]=new_lista_b
# datadf["diff_new_listas"]= datadf["new_lista_a"]- datadf["new_lista_b"]
# datadf["diff_new_listas"] =datadf["diff_new_listas"].abs()
# %%
rep_list  =  []
for elem in new_lista_a:
    repetition = datadf.loc[datadf["new_lista_b"] == elem, :].shape[0]
    rep_list.append(repetition)
datadf["repetition"]=rep_list
datadf["similarity"]=datadf["new_lista_a"]* datadf["repetition"]

# %%
datadf.head(10)
# %%
print ("RESULT: ", datadf["similarity"].sum())



# %%
