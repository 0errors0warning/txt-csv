import re   #引用re模块
import os
import csv
import calendar
f1  =  open("./ebooks/9.txt","r")
headers = ['Title','Author','Character set encoding','Language','Releasing Date','Posting Date','ID','id1','id2']

with open('test.csv','w',newline='')as f:
     f_csv = csv.writer(f)
     f_csv.writerow(headers)


pathlist=(os.listdir("./ebooks/"))
for index in range(len(pathlist)):
 with open("./ebooks/"+pathlist[index], "r") as f:
     try:
      data=f.readlines()
     except:
      pass
     try:
      data=f.readlines(encoding='gbk')   
     except:
      pass
     for i in range(len(data)):
         if data[i]=='\n':
             data[i]= '114514'
             continue
         data[i] = data[i].strip('\n')  #去掉列表中每一个元素的换行符
     j=0
     tmp=''
     seclist=[]
     for i in range(len(data)):
         if data[i]=='114514':
             for k in range(j+1,i):
                 tmp+=data[k]
             j=i

             seclist.append(tmp)
             tmp=''

 name1=['unknown']
 name2=['unknown']
 name3=['unknown']
 name4=['unknown']
 name5=['26,1976,12']
 name6=['26,1976,12']
 for i in range(len(seclist)):
     pattern = re.compile("Title:.*?")
     a=re.findall(pattern,seclist[i])
     if a:
         name1[0]=seclist[i][6::]
 
         continue

     pattern = re.compile("Author:.*?")
     a=re.findall(pattern,seclist[i])
     if a:
         name2[0]=seclist[i][7::]

     pattern = re.compile("Character set encoding:.*?")
     a=re.findall(pattern,seclist[i])
     if a:
         name3[0]=seclist[i][23::]

     pattern = re.compile("Language:.*?")
     a=re.findall(pattern,seclist[i])
     if a:
         name4[0]=seclist[i][9::]
         
     pattern = re.compile("Release Date:.*?")
     a=re.findall(pattern,seclist[i])
     if a:
         name5[0]=seclist[i][13::]

         for j in range (len(name5[0])):
             if name5[0][j]=='[':
                 name5[0]=name5[0][:j]
                 break
         f0=re.findall('(\d+)',name5[0])
         f1=re.findall('(\D+)',name5[0])
         f1 = ''.join([x for x in f1[0] if x.isalpha()])
         if f0:
          if f1 !='unknown':
              try:
                  f0.append(str(list(calendar.month_name).index(f1)))
              except:
                  f0=['26,1976,12']
          else:
             f0=['26,1976,12']
         if len(f0)==2:
             f0.insert(0, '1')
         name5=[','.join(f0)]
         
     pattern = re.compile("Posting Date:.*?")
     a=re.findall(pattern,seclist[i])
     if a:
         name6[0]=seclist[i][13::]
         for j in range (len(name6[0])):
             if name6[0][j]=='[':
                 name6[0]=name6[0][:j:]
                 break
         if name6[0].find('First')!=-1:
             name6[0]=name6[0][:name6[0].find('First')]
     name6=name5
 rows = [       name1,name2,name3,name4,name5,name6,[index],[index]    ]
 rows=sum(rows,[])
 rows.append( pathlist[index])
 print(index)
 with open('test.csv','a+',newline='')as f:
     f_csv = csv.writer(f)
     f_csv.writerow(rows)

 
