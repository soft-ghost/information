import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
from collections import Counter
import seaborn as sns
import math

all = pd.read_csv('D:\python 打开文件\项目数据\附件1.csv',encoding ='gbk')
#导入附件一中的数据
all2=pd.read_csv('D:\python 打开文件\项目数据\附件2.csv',encoding ='gbk')
#导入附件二中的数据

place_A=all.loc[all['地点']=='A',['订单号','设备ID','应付金额','实际金额','商品','支付时间','地点','状态','提现']]
place_B=all.loc[all['地点']=='B',['订单号','设备ID','应付金额','实际金额','商品','支付时间','地点','状态','提现']]
place_C=all.loc[all['地点']=='C',['订单号','设备ID','应付金额','实际金额','商品','支付时间','地点','状态','提现']]
place_D=all.loc[all['地点']=='D',['订单号','设备ID','应付金额','实际金额','商品','支付时间','地点','状态','提现']]
place_E=all.loc[all['地点']=='E',['订单号','设备ID','应付金额','实际金额','商品','支付时间','地点','状态','提现']]
#将各个地点的数据分别存放于不同的dataframe中

pd.DataFrame.to_csv(place_A,"task1-1A.csv",',',encoding ='gbk')
pd.DataFrame.to_csv(place_B,"task1-1B.csv",',',encoding ='gbk')
pd.DataFrame.to_csv(place_C,"task1-1C.csv",',',encoding ='gbk')
pd.DataFrame.to_csv(place_D,"task1-1D.csv",',',encoding ='gbk')
pd.DataFrame.to_csv(place_E,"task1-1E.csv",',',encoding ='gbk')
#将各个地点的数据分别新建一个csv文件进行存放





place_A['支付时间'] = pd.DatetimeIndex(place_A['支付时间'])
place_A_5=place_A.loc[place_A['支付时间'].dt.month==5,['订单号','设备ID','应付金额','实际金额','商品','支付时间','地点','状态','提现']]
place_B['支付时间'] = pd.DatetimeIndex(place_B['支付时间'])
place_B_5=place_B.loc[place_B['支付时间'].dt.month==5,['订单号','设备ID','应付金额','实际金额','商品','支付时间','地点','状态','提现']]
place_C['支付时间'] = pd.to_datetime(place_C['支付时间'])
place_C_5=place_C.loc[place_C['支付时间'].dt.month==5,['实际金额','商品','支付时间','状态','提现']]
place_D['支付时间'] = pd.DatetimeIndex(place_D['支付时间'])
place_D_5=place_D.loc[place_D['支付时间'].dt.month==5,['订单号','设备ID','应付金额','实际金额','商品','支付时间','地点','状态','提现']]
place_E['支付时间'] = pd.DatetimeIndex(place_E['支付时间'])
place_E_5=place_E.loc[place_E['支付时间'].dt.month==5,['订单号','设备ID','应付金额','实际金额','商品','支付时间','地点','状态','提现']]
#将各个售货机的5月的数据进行提取

print('A售货机5月的总交易额为',np.sum(place_A_5['实际金额']),'元')
print('B售货机5月的总交易额为',np.sum(place_B_5['实际金额']),'元')
print('C售货机5月的总交易额为',np.sum(place_C_5['实际金额']),'元')
print('D售货机5月的总交易额为',np.sum(place_D_5['实际金额']),'元')
print('E售货机5月的总交易额为',np.sum(place_E_5['实际金额']),'元')
print()#换行使得结果更易于阅读
#将实际金额那一列数据进行相加求得该月交易额

print('A售货机5月订单量为',place_A_5.iloc[:,0].size,'单')
print('B售货机5月订单量为',place_B_5.iloc[:,0].size,'单')
print('C售货机5月订单量为',place_C_5.iloc[:,0].size,'单')
print('D售货机5月订单量为',place_D_5.iloc[:,0].size,'单')
print('E售货机5月订单量为',place_E_5.iloc[:,0].size,'单')
print()
#通过计算有多少行来得知该月订单量为多少

print('所有售货机5月订单量为',place_A_5.iloc[:,0].size+place_B_5.iloc[:,0].size+place_C_5.iloc[:,0].size+place_D_5.iloc[:,0].size+place_E_5.iloc[:,0].size
,'单')
#将每个售货机的订单量相加即可得出所有售货机的订单量

print('所有售货机5月总交易额为',np.sum(place_A_5['实际金额'])+np.sum(place_B_5['实际金额'])+np.sum(place_C_5['实际金额'])+np.sum(place_D_5['实际金额'])+np.sum(place_E_5['实际金额']),'元')
print()
#将每个售货机的交易额相加即可得出所有售货机的交易额

A=[]
B=[]
C=[]
D=[]
E=[]
#建立空列表用于存放每个月的支付金额

def whichmonth(i):
  #计算每个月各个售货机的交易额和订单量
  place_A['支付时间'] = pd.DatetimeIndex(place_A['支付时间'])
  place_A_month=place_A.loc[place_A['支付时间'].dt.month==i,['实际金额','商品','支付时间','状态','提现']]
  A.append(np.sum(place_A_month['实际金额']))
  place_B['支付时间'] = pd.DatetimeIndex(place_B['支付时间'])
  place_B_month=place_B.loc[place_B['支付时间'].dt.month==i,['实际金额','商品','支付时间','状态','提现']]
  B.append(np.sum(place_B_month['实际金额']))
  place_C['支付时间'] = pd.to_datetime(place_C['支付时间'])
  place_C_month=place_C.loc[place_C['支付时间'].dt.month==i,['实际金额','商品','支付时间','状态','提现']]
  C.append(np.sum(place_C_month['实际金额']))
  place_D['支付时间'] = pd.DatetimeIndex(place_D['支付时间'])
  place_D_month=place_D.loc[place_D['支付时间'].dt.month==i,['实际金额','商品','支付时间','状态','提现']]
  D.append(np.sum(place_D_month['实际金额']))
  place_E['支付时间'] = pd.DatetimeIndex(place_E['支付时间'])
  place_E_month=place_E.loc[place_E['支付时间'].dt.month==i,['实际金额','商品','支付时间','状态','提现']]
  E.append(np.sum(place_E_month['实际金额']))
  print('A售货机',i,'月的总交易额为',np.sum(place_A_month['实际金额']),'元')
  print('B售货机',i,'月的总交易额为',np.sum(place_B_month['实际金额']),'元')
  print('C售货机',i,'月的总交易额为',np.sum(place_C_month['实际金额']),'元')
  print('D售货机',i,'月的总交易额为',np.sum(place_D_month['实际金额']),'元')
  print('E售货机',i,'月的总交易额为',np.sum(place_E_month['实际金额']),'元')
  print()
  print('A售货机',i,'月订单量为',place_A_month.iloc[:,0].size,'单')
  print('B售货机',i,'月订单量为',place_B_month.iloc[:,0].size,'单')
  print('C售货机',i,'月订单量为',place_C_month.iloc[:,0].size,'单')
  print('D售货机',i,'月订单量为',place_D_month.iloc[:,0].size,'单')
  print('E售货机',i,'月订单量为',place_E_month.iloc[:,0].size,'单')
  return;

for i in range(1,13):
#分别计算1到12月的每个售货机的交易额和订单量
 print(i,'月各个售货机的交易额和订单量分别如下所示:')
 whichmonth(i)
 print()





#2017年6月商品销售前五的柱状图

all['支付时间'] = pd.DatetimeIndex(all['支付时间'])
#将all中的支付时间转换转换成为datatime格式

number=all.loc[all['支付时间'].dt.month==5,['商品','提现']]
#将所有商品5月份出售的商品提取出来

list=[]
#建造空列表存放'商品'列的数据

x=[]
y=[]
#建造两个空列表存放x轴y轴的数据

for row in number.itertuples():
    list.append(getattr(row, '商品'))

for i in range(5):
#把x轴，y轴数据录入
  x.append(Counter(list).most_common(5)[i][0])
  y.append(Counter(list).most_common(5)[i][1])
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
plt.bar(x,y)
plt.xlabel('商品')
plt.ylabel('销售量')
plt.title('2017年6月销量前五商品销量图')
plt.savefig('2017年6月销量前五商品销量图.png')
plt.show()
#画出柱状图





#各个售货机每月的折线图

month=[1,2,3,4,5,6,7,8,9,10,11,12]
#构造month列表存放所有月份作为x轴

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(8,7))
plt.plot(month[:],A[:])
plt.xlabel('月份')
plt.ylabel('销售额(元)')
plt.title('A售货机每月总交易额')
plt.savefig('A售货机每月总交易额的折线图.png')
plt.show()
#A售货机每月交易额的折线图

plt.figure(figsize=(8,7))
plt.plot(month[:],B[:])

plt.xlabel('月份')
plt.ylabel('销售额(元)')
plt.title('B售货机每月总交易额')
plt.savefig('B售货机每月总交易额的折线图.png')
plt.show()
#B售货机每月交易额的折线图

plt.figure(figsize=(8,7))
plt.plot(month[:],C[:])
plt.xlabel('月份')
plt.ylabel('销售额(元)')
plt.title('C售货机每月总交易额')
plt.savefig('C售货机每月总交易额的折线图.png')
plt.show()
#C售货机每月交易额的折线图

plt.figure(figsize=(8,7))
plt.plot(month[:],D[:])
plt.xlabel('月份')
plt.ylabel('销售额(元)')
plt.title('D售货机每月总交易额')
plt.savefig('D售货机每月总交易额的折线图.png')
plt.show()
#D售货机每月交易额的折线图

plt.figure(figsize=(8,7))
plt.plot(month[:],E[:])
plt.xlabel('月份')
plt.ylabel('销售额(元)')
plt.title('E售货机每月总交易额')
plt.savefig('E售货机每月总交易额的折线图.png')
plt.show()
#E售货机每月交易额的折线图





#每个售货机月环比增长率

a=[]
b=[]
c=[]
d=[]
e=[]
#构建存放y轴数据的列表

month1=[2,3,4,5,6,7,8,9,10,11,12]
#由于第一个月没有环比增长率创建一个只有11一个月的列表

for i in range(0,11):
 a.append((A[i+1]-A[i])/A[i])
 b.append((B[i+1]-B[i])/B[i])
 c.append((C[i+1]-C[i])/C[i])
 d.append((D[i+1]-D[i])/D[i])
 e.append((E[i+1]-E[i])/E[i])  

plt.figure(figsize=(8, 6))
plt.bar(month1,a)
plt.xlabel('月份')
plt.ylabel('增长率')
plt.title('A售货机每月环比增长率')
plt.savefig('A售货机每月总交易额的柱状图.png')
plt.show()
#A售货机的每月环比增长率的柱状图

plt.figure(figsize=(8, 6))
plt.bar(month1,b)
plt.xlabel('月份')
plt.ylabel('增长率')
plt.title('B售货机每月环比增长率')
plt.savefig('B售货机每月总交易额的柱状图.png')
plt.show()
#B售货机的每月环比增长率的柱状图

plt.figure(figsize=(8, 6))
plt.bar(month1,c)
plt.xlabel('月份')
plt.ylabel('增长率')
plt.title('C售货机每月环比增长率')
plt.savefig('C售货机每月总交易额的柱状图.png')
plt.show()
#C售货机的每月环比增长率的柱状图

plt.figure(figsize=(8, 6))
plt.bar(month1,d)
plt.xlabel('月份')
plt.ylabel('增长率')
plt.title('D售货机每月环比增长率')
plt.savefig('D售货机每月总交易额的柱状图.png')
plt.show()
#D售货机的每月环比增长率的柱状图

plt.figure(figsize=(8, 6))
plt.bar(month1,e)
plt.xlabel('月份')
plt.ylabel('增长率')
plt.title('E售货机每月环比增长率')
plt.savefig('E售货机每月总交易额的柱状图.png')
plt.show()
#E售货机的每月环比增长率的柱状图




#每台售货机毛利润饼图

place_A_1=pd.merge(place_A,all2,on='商品')
drink=place_A_1.loc[place_A_1['大类']=='饮料',['实际金额','商品','状态','提现']]
not_drink=place_A_1.loc[place_A_1['大类']=='非饮料',['实际金额','商品','状态','提现']]
money=[np.sum(drink['实际金额'])*0.25,np.sum(not_drink['实际金额'])*0.2]

plt.figure(figsize=(6,6))
label=['饮料毛利润','非饮料毛利润']
explode=[0.01,0.01]
plt.title('A售货机毛利润占比')
plt.savefig('A售货机毛利润占比.png')
plt.pie(money,explode=explode,labels=label)

place_B_1=pd.merge(place_B,all2,on='商品')
drink=place_B_1.loc[place_B_1['大类']=='饮料',['实际金额','商品','状态','提现']]
not_drink=place_B_1.loc[place_B_1['大类']=='非饮料',['实际金额','商品','状态','提现']]
money=[np.sum(drink['实际金额'])*0.25,np.sum(not_drink['实际金额'])*0.2]

plt.figure(figsize=(6,6))
label=['饮料毛利润','非饮料毛利润']
explode=[0.01,0.01]
plt.title('B售货机毛利润占比')
plt.savefig('B售货机毛利润占比.png')
plt.pie(money,explode=explode,labels=label)

place_C_1=pd.merge(place_C,all2,on='商品')
drink=place_C_1.loc[place_C_1['大类']=='饮料',['实际金额','商品','状态','提现']]
not_drink=place_C_1.loc[place_C_1['大类']=='非饮料',['实际金额','商品','状态','提现']]
money=[np.sum(drink['实际金额'])*0.25,np.sum(not_drink['实际金额'])*0.2]

plt.figure(figsize=(6,6))
label=['饮料毛利润','非饮料毛利润']
explode=[0.01,0.01]
plt.title('C售货机毛利润占比')
plt.savefig('C售货机毛利润占比.png')
plt.pie(money,explode=explode,labels=label)

place_D_1=pd.merge(place_D,all2,on='商品')
drink=place_D_1.loc[place_D_1['大类']=='饮料',['实际金额','商品','状态','提现']]
not_drink=place_D_1.loc[place_D_1['大类']=='非饮料',['实际金额','商品','状态','提现']]
money=[np.sum(drink['实际金额'])*0.25,np.sum(not_drink['实际金额'])*0.2]

plt.figure(figsize=(6,6))
label=['饮料毛利润','非饮料毛利润']
explode=[0.01,0.01]
plt.title('D售货机毛利润占比')
plt.savefig('D售货机毛利润占比.png')
plt.pie(money,explode=explode,labels=label)

place_E_1=pd.merge(place_E,all2,on='商品')
drink=place_E_1.loc[place_E_1['大类']=='饮料',['实际金额','商品','状态','提现']]
not_drink=place_E_1.loc[place_E_1['大类']=='非饮料',['实际金额','商品','状态','提现']]
money=[np.sum(drink['实际金额'])*0.25,np.sum(not_drink['实际金额'])*0.2]

plt.figure(figsize=(6,6))
label=['饮料毛利润','非饮料毛利润']
explode=[0.01,0.01]
plt.title('E售货机毛利润占比')
plt.savefig('E售货机毛利润占比.png')
plt.pie(money,explode=explode,labels=label)






#气泡图

all1['支付时间'] = pd.DatetimeIndex(all1['支付时间'])
#将all1['支付时间']的格式转换为datatime格式

Jan=all1.loc[all1['支付时间'].dt.month==1,['实际金额','二级类','支付时间']]
Jan_sum=dict(Jan.groupby('二级类')['实际金额'].mean())
Jan_sum=pd.DataFrame(pd.Series(Jan_sum),columns=['平均值'])
Jan_sum=Jan_sum.reset_index().rename(columns ={'二级类':'平均值'})
Jan_sum['月份'] = 1
pao=Jan_sum

Feb=all1.loc[all1['支付时间'].dt.month==2,['实际金额','二级类','支付时间']]
Feb_sum=dict(Feb.groupby('二级类')['实际金额'].mean())
Feb_sum=pd.DataFrame(pd.Series(Feb_sum),columns=['平均值'])
Feb_sum=Feb_sum.reset_index().rename(columns ={'二级类':'平均值'})
Feb_sum['月份'] = 2
pao=pao.append(Feb_sum)

Mar=all1.loc[all1['支付时间'].dt.month==3,['实际金额','二级类','支付时间']]
Mar_sum=dict(Mar.groupby('二级类')['实际金额'].mean())
Mar_sum=pd.DataFrame(pd.Series(Mar_sum),columns=['平均值'])
Mar_sum=Mar_sum.reset_index().rename(columns ={'二级类':'平均值'})
Mar_sum['月份'] = 3
pao=pao.append(Mar_sum)

Apr=all1.loc[all1['支付时间'].dt.month==4,['实际金额','二级类','支付时间']]
Apr_sum=dict(Apr.groupby('二级类')['实际金额'].mean())
Apr_sum=pd.DataFrame(pd.Series(Apr_sum),columns=['平均值'])
Apr_sum=Apr_sum.reset_index().rename(columns ={'二级类':'平均值'})
Apr_sum['月份'] = 4
pao=pao.append(Apr_sum)

May=all1.loc[all1['支付时间'].dt.month==5,['实际金额','二级类','支付时间']]
May_sum=dict(May.groupby('二级类')['实际金额'].mean())
May_sum=pd.DataFrame(pd.Series(May_sum),columns=['平均值'])
May_sum=May_sum.reset_index().rename(columns ={'二级类':'平均值'})
May_sum['月份'] = 5
pao=pao.append(May_sum)

Jun=all1.loc[all1['支付时间'].dt.month==6,['实际金额','二级类','支付时间']]
Jun_sum=dict(Jun.groupby('二级类')['实际金额'].mean())
Jun_sum=pd.DataFrame(pd.Series(Jun_sum),columns=['平均值'])
Jun_sum=Jun_sum.reset_index().rename(columns ={'二级类':'平均值'})
Jun_sum['月份'] = 6
pao=pao.append(Jun_sum)

Jul=all1.loc[all1['支付时间'].dt.month==7,['实际金额','二级类','支付时间']]
Jul_sum=dict(Jul.groupby('二级类')['实际金额'].mean())
Jul_sum=pd.DataFrame(pd.Series(Jul_sum),columns=['平均值'])
Jul_sum=Jul_sum.reset_index().rename(columns ={'二级类':'平均值'})
Jul_sum['月份'] = 7
pao=pao.append(Jun_sum)

Aug=all1.loc[all1['支付时间'].dt.month==8,['实际金额','二级类','支付时间']]
Aug_sum=dict(Aug.groupby('二级类')['实际金额'].mean())
Aug_sum=pd.DataFrame(pd.Series(Aug_sum),columns=['平均值'])
Aug_sum=Aug_sum.reset_index().rename(columns ={'二级类':'平均值'})
Aug_sum['月份'] = 8
pao=pao.append(Aug_sum)

Sep=all1.loc[all1['支付时间'].dt.month==9,['实际金额','二级类','支付时间']]
Sep_sum=dict(Sep.groupby('二级类')['实际金额'].mean())
Sep_sum=pd.DataFrame(pd.Series(Sep_sum),columns=['平均值'])
Sep_sum=Sep_sum.reset_index().rename(columns ={'二级类':'平均值'})
Sep_sum['月份'] = 9
pao=pao.append(Sep_sum)

Oct=all1.loc[all1['支付时间'].dt.month==10,['实际金额','二级类','支付时间']]
Oct_sum=dict(Oct.groupby('二级类')['实际金额'].mean())
Oct_sum=pd.DataFrame(pd.Series(Oct_sum),columns=['平均值'])
Oct_sum=Oct_sum.reset_index().rename(columns ={'二级类':'平均值'})
Oct_sum['月份'] = 10
pao=pao.append(Oct_sum)

Nov=all1.loc[all1['支付时间'].dt.month==11,['实际金额','二级类','支付时间']]
Nov_sum=dict(Nov.groupby('二级类')['实际金额'].mean())
Nov_sum=pd.DataFrame(pd.Series(Nov_sum),columns=['平均值'])
Nov_sum=Nov_sum.reset_index().rename(columns ={'二级类':'平均值'})
Nov_sum['月份'] = 11
pao=pao.append(Nov_sum)

Dec=all1.loc[all1['支付时间'].dt.month==12,['实际金额','二级类','支付时间']]
Dec_sum=dict(Dec.groupby('二级类')['实际金额'].mean())
Dec_sum=pd.DataFrame(pd.Series(Dec_sum),columns=['平均值'])
Dec_sum=Dec_sum.reset_index().rename(columns ={'二级类':'平均值'})
Dec_sum['月份'] = 12
pao=pao.append(Dec_sum)
#分别计算每个月的交易额均值，将数据存在pao这个dataframe中以便进行作图

sns.set(style = "whitegrid")#设置样式
x = pao['月份']#X轴数据
y = pao['index']#Y轴数据
z = pao['平均值']#用来调整各个点的大小s
cm = plt.cm.get_cmap('RdYlBu')
fig,ax = plt.subplots(figsize = (12,10))
bubble = ax.scatter(x, y , s = (z - np.min(z) + 0.1) * 1000, c = z, cmap = cm, linewidth = 0.5, alpha = 0.5)
ax.grid()
fig.colorbar(bubble)
ax.set_xlabel('月份', fontsize = 15)#X轴标签
ax.set_ylabel('二级类', fontsize = 15)#Y轴标签
plt.show()
#绘制气泡图




#热力图



list_1=[]
list_2=[]
for i in range(1,32):
    list_1.append(i)
    list_2.append(0)
month_C_6 = dict(zip(list_1,list_2))
month_C_8 = dict(zip(list_1,list_2))
month_C_7 = dict(zip(list_1,list_2))
#list_1存放日期，list_2存放销售量（默认值为0），将list_1作为字典的key值，list_2作为字典的value值

list_1=[]
list_2=[]
for i in range(24):
    list_1.append(i)
    list_2.append(0)
date=dict(zip(list_1,list_2))
#list_1存放时间（单位小时间），list_2存放每小时的销售数据（默认值为0），将list_1作为字典的key值，list_2作为字典的value值

place_C=all.loc[all['地点']=='C',['订单号','设备ID','应付金额','实际金额','商品','支付时间','地点','状态','提现']]
place_C['支付时间'] = pd.DatetimeIndex(place_C['支付时间'])
place_C_8=place_C.loc[place_C['支付时间'].dt.month==8,['商品','支付时间',]]
place_C_6=place_C.loc[place_C['支付时间'].dt.month==6,['商品','支付时间',]]
place_C_7=place_C.loc[place_C['支付时间'].dt.month==7,['商品','支付时间',]]
place_C_8['支付时间'] = pd.DatetimeIndex(place_C_8['支付时间'])
place_C_6['支付时间'] = pd.DatetimeIndex(place_C_6['支付时间'])
place_C_7['支付时间'] = pd.DatetimeIndex(place_C_7['支付时间'])

for i in range(1,32):
  a = place_C_8[(place_C_8['支付时间'].dt.day==i)].index.tolist()
  month_C_8[i]=len(a)
  a = place_C_7[(place_C_7['支付时间'].dt.day==i)].index.tolist()
  month_C_7[i]=len(a)
  a = place_C_6[(place_C_6['支付时间'].dt.day==i)].index.tolist()
  month_C_6[i]=len(a)
#统计C售货机 6、7、8月每天分别销售了多少    

for i in range(24):
  a = place_C_8[(place_C_8['支付时间'].dt.hour==i) & (place_C_8['支付时间'].dt.day==1)].index.tolist()
  date[i]=len(a)
daily_8=pd.DataFrame(date,index=[1])
#先将8月份第一天的每小时数据输入到daily_8中

for x in range(2,32):
  for i in range(24):
      a = place_C_8[(place_C_8['支付时间'].dt.hour==i) & (place_C_8['支付时间'].dt.day==x)].index.tolist()
      date[i]=len(a)
  daily_8 = daily_8.append(pd.DataFrame(date,index=[x]))
#用for循环将8月份每天每小时的数据输入到daily_8中

for i in range(24):
  a = place_C_6[(place_C_6['支付时间'].dt.hour==i) & (place_C_6['支付时间'].dt.day==1)].index.tolist()
  date[i]=len(a)
daily_6=pd.DataFrame(date,index=[1])
#先将6月份第一天的每小时数据输入到daily_6中

for x in range(2,32):
  for i in range(24):
      a = place_C_6[(place_C_6['支付时间'].dt.hour==i) & (place_C_6['支付时间'].dt.day==x)].index.tolist()
      date[i]=len(a)
  daily_6 = daily_6.append(pd.DataFrame(date,index=[x]))
#用for循环将6月份每天每小时的数据输入到daily_6中

for i in range(24):
  a = place_C_7[(place_C_7['支付时间'].dt.hour==i) & (place_C_7['支付时间'].dt.day==1)].index.tolist()
  date[i]=len(a)
daily_7=pd.DataFrame(date,index=[1])
#先将7月份第一天的每小时数据输入到daily_7中

for x in range(2,32):
  for i in range(24):
      a = place_C_7[(place_C_7['支付时间'].dt.hour==i) & (place_C_7['支付时间'].dt.day==x)].index.tolist()
      date[i]=len(a)
  daily_7 = daily_7.append(pd.DataFrame(date,index=[x]))
#用for循环将7月份每天每小时的数据输入到daily_7中

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
#设置中文显示
plt.figure(figsize=(8, 6))
plt.subplots_adjust(left=.2, right=0.95, bottom=0.15, top=0.95)
plt.imshow(daily_6, interpolation='nearest', cmap=plt.cm.hot)
plt.xlabel('日期')
plt.ylabel('小时')
plt.colorbar()
plt.title('C售货机6月订单量热力图')
plt.savefig('C售货机6月订单量热力图.png')
plt.show()

plt.figure(figsize=(8, 6))
plt.subplots_adjust(left=.2, right=0.95, bottom=0.15, top=0.95)
plt.imshow(daily_7, interpolation='nearest', cmap=plt.cm.hot)
plt.xlabel('日期')
plt.ylabel('小时')
plt.colorbar()
plt.title('C售货机7月订单量热力图')
plt.savefig('C售货机7月订单量热力图.png')

plt.figure(figsize=(8, 6))
plt.subplots_adjust(left=.2, right=0.95, bottom=0.15, top=0.95)
plt.imshow(daily_8, interpolation='nearest', cmap=plt.cm.hot)
plt.xlabel('日期')
plt.ylabel('小时')
plt.colorbar()
plt.title('C售货机8月订单量热力图')
plt.savefig('C售货机8月订单量热力图.png')





#贴标签

Pivot_A=pd.pivot_table(drink_A[['商品','提现']],index='商品',aggfunc='count')
#将饮品类惊醒分类提取，用计数函数 算出每个的销售量
top=math.floor(len(Pivot_A)*0.2)
#以所有商品中排名前百分之20（向下取整）的作为热销商品，排名后百分之20（向下取整）的作为滞销商品，剩余的则是正常商品
Pivot_A=Pivot_A.reindex(Pivot_A['提现'].abs().sort_values(ascending=False).index)
#对Pivot_A进行排序，从大到小
Pivot_A['商标']='正常'
#先将所有商品标记为正常
Pivot_A.head(top)['商标']='热销'
#前百分之20改标记为热销
Pivot_A.tail(top)['商标']='滞销'
#后百分之20改标记为滞销

list_1=[]
list_2=[]
list_3=[]
#建立空列表分别存放'序号','商品名称'，'标签'
for i in range(Pivot_A.iloc[:,0].size-1):
    list_1.append(i+1)
    list_2.append(Pivot_A.index[i+1])
    list_3.append(Pivot_A['商标'][i])
#通过for循环意一一放入对应列表
dic1={'序号':list_1,'饮料类商品':list_2,'标签':list_3}  
task_3_1A=pd.DataFrame(dic1)
#将三个列表合为一个字典，并将字典转化为dataframe格式
pd.DataFrame.to_csv(task_3_1A,"task3-1A.csv",',',encoding ='gbk')
#保存该已含标签的csv文件


#方法和上述一样
Pivot_B=pd.pivot_table(drink_B[['商品','提现']],index='商品',aggfunc='count')
top=math.floor(len(Pivot_B)*0.2)
Pivot_B=Pivot_B.reindex(Pivot_B['提现'].abs().sort_values(ascending=False).index)
Pivot_B['商标']='正常'
Pivot_B.head(top)['商标']='热销'
Pivot_B.tail(top)['商标']='滞销'
list_1=[]
list_2=[]
list_3=[]
for i in range(Pivot_B.iloc[:,0].size-1):
    list_1.append(i+1)
    list_2.append(Pivot_B.index[i+1])
    list_3.append(Pivot_B['商标'][i])
dic1={'序号':list_1,'饮料类商品':list_2,'标签':list_3}  
task_3_1B=pd.DataFrame(dic1)
pd.DataFrame.to_csv(task_3_1B,"task3-1B.csv",',',encoding ='gbk')


#方法和上述一样
Pivot_C=pd.pivot_table(drink_C[['商品','提现']],index='商品',aggfunc='count')
top=math.floor(len(Pivot_C)*0.2)
Pivot_C=Pivot_C.reindex(Pivot_C['提现'].abs().sort_values(ascending=False).index)
Pivot_C['商标']='正常'
Pivot_C.head(top)['商标']='热销'
Pivot_C.tail(top)['商标']='滞销'
list_1=[]
list_2=[]
list_3=[]
for i in range(Pivot_C.iloc[:,0].size-1):
    list_1.append(i+1)
    list_2.append(Pivot_C.index[i+1])
    list_3.append(Pivot_C['商标'][i])
dic1={'序号':list_1,'饮料类商品':list_2,'标签':list_3}  
task_3_1C=pd.DataFrame(dic1)
pd.DataFrame.to_csv(task_3_1C,"task3-1C.csv",',',encoding ='gbk')


#方法和上述一样
Pivot_D=pd.pivot_table(drink_D[['商品','提现']],index='商品',aggfunc='count')
top=math.floor(len(Pivot_D)*0.2)
Pivot_D=Pivot_D.reindex(Pivot_D['提现'].abs().sort_values(ascending=False).index)
Pivot_D['商标']='正常'
Pivot_D.head(top)['商标']='热销'
Pivot_D.tail(top)['商标']='滞销'
list_1=[]
list_2=[]
list_3=[]
for i in range(Pivot_D.iloc[:,0].size-1):
    list_1.append(i+1)
    list_2.append(Pivot_D.index[i+1])
    list_3.append(Pivot_D['商标'][i])
dic1={'序号':list_1,'饮料类商品':list_2,'标签':list_3}  
task_3_1D=pd.DataFrame(dic1)
pd.DataFrame.to_csv(task_3_1D,"task3-1D.csv",',',encoding ='gbk')


#方法和上述一样
Pivot_E=pd.pivot_table(drink_E[['商品','提现']],index='商品',aggfunc='count')
top=math.floor(len(Pivot_E)*0.2)
Pivot_E=Pivot_E.reindex(Pivot_E['提现'].abs().sort_values(ascending=False).index)
Pivot_E['商标']='正常'
Pivot_E.head(top)['商标']='热销'
Pivot_E.tail(top)['商标']='滞销'
list_1=[]
list_2=[]
list_3=[]
for i in range(Pivot_E.iloc[:,0].size-1):
    list_1.append(i+1)
    list_2.append(Pivot_E.index[i+1])
    list_3.append(Pivot_E['商标'][i])
dic1={'序号':list_1,'饮料类商品':list_2,'标签':list_3}  
task_3_1E=pd.DataFrame(dic1)
pd.DataFrame.to_csv(task_3_1E,"task3-1B.csv",',',encoding ='gbk')

