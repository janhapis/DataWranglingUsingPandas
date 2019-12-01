import pandas as pd
a = {'Student':['Ice Bear','Panda','Grizzly'],'Math':[80,95,79]}
A = pd.DataFrame(a,columns=['Student','Math'])
b = {'Student':['Ice Bear','Panda','Grizzly'],'Electronics':[85,81,83]}
B = pd.DataFrame(b,columns=['Student','Electronics'])
c = {'Student':['Ice Bear','Panda','Grizzly'],'GEAS':[90,79,93]}
C = pd.DataFrame(c,columns=['Student','GEAS'])
d = {'Student':['Ice Bear','Panda','Grizzly'],'ESAT':[93,89,88]}
D = pd.DataFrame(d,columns=['Student','ESAT'])
Grades = pd.merge(A,B, how='right',on='Student')
Grades = pd.merge(Grades,C, how='right',on='Student')
Grades = pd.merge(Grades,D, how='right',on='Student')
LongFormat = pd.melt(Grades,id_vars='Student',var_name = 'Subject',value_name = 'Grades')
LongFormat = LongFormat.sort_values('Student').reset_index().drop(columns = ['index'])
print(LongFormat)