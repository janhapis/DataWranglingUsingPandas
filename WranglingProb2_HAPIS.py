import pandas as pd
data = {'Box':'Box1','Dimension':['Length','Width','Height'],'Value':[6,4,2]}
data2 = {'Box':'Box2','Dimension':['Length','Width','Height'],'Value':[5,3,4]}
Box1 = pd.DataFrame(data,columns = ['Box','Dimension','Value'])
Box2 = pd.DataFrame(data2,columns = ['Box','Dimension','Value'])
messy = Box1.append(Box2).reset_index().drop(columns = ['index'])
tidy1 = messy.pivot_table(index = 'Box',columns = 'Dimension',values = 'Value').reset_index()
data3 = {'Box':['Box1','Box2'],'Volume':[6*4*2,5*3*4]}
Volume = pd.DataFrame(data3,columns = ['Box','Volume'])
tidy = pd.merge(tidy1,Volume, how='right',on='Box')
print(tidy)