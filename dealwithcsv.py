# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 08:43:33 2020

@author: MSI-PC
"""
import pandas as pd
#a和b的长度必须保持一致，否则报错
a = []


import csv
import re
df = pd.read_csv('test0.csv',encoding='gbk')
chapcode=0
bookcode=0
for i in range(len(df['li'])):
    b=str(df['content'][i])
    if bookcode == df['li'][i]:
        pass
    else:
        bookcode = df['li'][i]
        chapcode=0
    if 'CHAPTER' in b or 'Chapter' in b:
        chapcode+=1
    if chapcode==0:
        df['chap'][i]='content'
    else:
        df['chap'][i]='chap'+str(chapcode)
    df['ln'][i]=(chapcode)
print((df))
df.to_csv(r"novel_books_info111.csv",sep=',')













# df = pd.read_csv('test1.csv',encoding='gbk')
# exp='NENG0000000'
# neng=[]
# for i in range(len(df['li'])):
#     b=str(df['li'][i])   
#     for j in range(len(b)):
#         exp=exp[:len(exp)-1-j]+b[len(b)-1-j]+exp[len(exp)-j:]
#     neng.append(exp)
#     # print(df['li'][i])
# for i in range(len(df['text'])):
#     b=str(df['li'][i])
#     df['text'][i]=df['text'][i][:len(df['text'][i])-4:]
# df.insert(5,'typeSmallSmall',neng)
# df.to_csv(r"novel_books_info1.csv",sep=',')

# df = pd.read_csv('test2.csv',encoding='gbk')
# exp='NENG0000000'
# neng=[]
# for i in range(len(df['li'])):
#     b=str(df['li'][i])   
#     for j in range(len(b)):
#         exp=exp[:len(exp)-1-j]+b[len(b)-1-j]+exp[len(exp)-j:]
#     neng.append(exp)
#     # print(df['li'][i])
# for i in range(len(df['text'])):
#     b=str(df['li'][i])
#     df['text'][i]=df['text'][i][:len(df['text'][i])-4:]
# df.insert(5,'typeSmallSmall',neng)
# df.to_csv(r"novel_books_info2.csv",sep=',')

# df = pd.read_csv('test3.csv',encoding='gbk')
# exp='NENG0000000'
# neng=[]
# for i in range(len(df['li'])):
#     b=str(df['li'][i])   
#     for j in range(len(b)):
#         exp=exp[:len(exp)-1-j]+b[len(b)-1-j]+exp[len(exp)-j:]
#     neng.append(exp)
#     # print(df['li'][i])
# for i in range(len(df['text'])):
#     b=str(df['li'][i])
#     df['text'][i]=df['text'][i][:len(df['text'][i])-4:]
# df.insert(5,'typeSmallSmall',neng)
# df.to_csv(r"novel_books_info3.csv",sep=',')

# df = pd.read_csv('test4.csv',encoding='gbk')
# exp='NENG0000000'
# neng=[]
# for i in range(len(df['li'])):
#     b=str(df['li'][i])   
#     for j in range(len(b)):
#         exp=exp[:len(exp)-1-j]+b[len(b)-1-j]+exp[len(exp)-j:]
#     neng.append(exp)
#     # print(df['li'][i])
# for i in range(len(df['text'])):
#     b=str(df['li'][i])
#     df['text'][i]=df['text'][i][:len(df['text'][i])-4:]
# df.insert(5,'typeSmallSmall',neng)
# df.to_csv(r"novel_books_info4.csv",sep=',')

# df = pd.read_csv('test5.csv',encoding='gbk')
# exp='NENG0000000'
# neng=[]
# for i in range(len(df['li'])):
#     b=str(df['li'][i])   
#     for j in range(len(b)):
#         exp=exp[:len(exp)-1-j]+b[len(b)-1-j]+exp[len(exp)-j:]
#     neng.append(exp)
#     # print(df['li'][i])
# for i in range(len(df['text'])):
#     b=str(df['li'][i])
#     df['text'][i]=df['text'][i][:len(df['text'][i])-4:]
# df.insert(5,'typeSmallSmall',neng)
# df.to_csv(r"novel_books_info5.csv",sep=',')

# df = pd.read_csv('test6.csv',encoding='gbk')
# exp='NENG0000000'
# neng=[]
# for i in range(len(df['li'])):
#     b=str(df['li'][i])   
#     for j in range(len(b)):
#         exp=exp[:len(exp)-1-j]+b[len(b)-1-j]+exp[len(exp)-j:]
#     neng.append(exp)
#     # print(df['li'][i])
# for i in range(len(df['text'])):
#     b=str(df['li'][i])
#     df['text'][i]=df['text'][i][:len(df['text'][i])-4:]
# df.insert(5,'typeSmallSmall',neng)
# df.to_csv(r"novel_books_info6.csv",sep=',')

# df = pd.read_csv('test7.csv',encoding='gbk')
# exp='NENG0000000'
# neng=[]
# for i in range(len(df['li'])):
#     b=str(df['li'][i])   
#     for j in range(len(b)):
#         exp=exp[:len(exp)-1-j]+b[len(b)-1-j]+exp[len(exp)-j:]
#     neng.append(exp)
#     # print(df['li'][i])
# for i in range(len(df['text'])):
#     b=str(df['li'][i])
#     df['text'][i]=df['text'][i][:len(df['text'][i])-4:]
# df.insert(5,'typeSmallSmall',neng)
# df.to_csv(r"novel_books_info7.csv",sep=',')