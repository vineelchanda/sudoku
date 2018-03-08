# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 17:37:47 2018

@author: vinee
"""

b=[]
b.append([0,3,6,0,9,0,7,5,0])
b.append([0,1,0,0,0,0,0,4,0])
b.append([7,0,0,0,0,0,0,0,2])
b.append([5,6,0,8,0,2,0,7,3])
b.append([0,0,0,0,0,0,0,0,0])
b.append([3,4,0,7,0,9,0,2,5])
b.append([4,0,0,0,0,0,0,0,7])
b.append([0,9,0,0,0,0,0,3,0])
b.append([0,5,1,0,7,0,4,6,0])
def Board(x=b):
    print("\n")
    for i in range(9):
            print(str(x[i][0:3])+"|"+str(x[i][3:6])+"|"+str(x[i][6:9]))
            if(i==2 or i==5):
                print("-----------------------------")
    print("\n")
    #creation on 1`s life 
def life(dig):
    temp = []
    for i in range(9):
        row=[]
        for j in range(9):
            if(b[i][j]==dig):
                row.append(dig)
            elif(b[i][j]==0):
                row.append("")
            else:
                row.append(0)
        temp.append(row)
    return temp 
def Life(digi):
    semiLife = life(digi)
    for i in range(9):
        for j in range(9):
            if(semiLife[i][j]==digi):
                for t in range(9):
                    semiLife[t][j]=0
                for t in range(9):
                    semiLife[i][t]=0
                semiLife[i][j]=digi
    for i in range(9):
        for j in range(9):
            if(semiLife[i][j]==digi):
                if(i==0 or i==3 or i==6):
                    if(j==0 or j==3 or j==6):
                        ti=i
                        tj=j
                        semiLife[ti+1][tj+1]=0
                        semiLife[ti+1][tj+2]=0
                        semiLife[ti+2][tj+1]=0
                        semiLife[ti+2][tj+2]=0
                    if(j==1 or j==4 or j==7):
                        ti=i
                        tj=j
                        semiLife[ti+1][tj-1]=0
                        semiLife[ti+1][tj+1]=0
                        semiLife[ti+2][tj-1]=0
                        semiLife[ti+2][tj+1]=0
                    if(j==2 or j==5 or j==8):
                        ti=i
                        tj=j
                        semiLife[ti+1][tj-2]=0
                        semiLife[ti+1][tj-1]=0
                        semiLife[ti+2][tj-2]=0
                        semiLife[ti+2][tj-1]=0
                if(i==1 or i==4 or i==7):
                    if(j==0 or j==3 or j==6):
                        ti=i
                        tj=j
                        semiLife[ti-1][tj+1]=0
                        semiLife[ti-1][tj+2]=0
                        semiLife[ti+1][tj+1]=0
                        semiLife[ti+1][tj+2]=0
                    if(j==1 or j==4 or j==7):
                        ti=i
                        tj=j
                        semiLife[ti-1][tj-1]=0
                        semiLife[ti+1][tj-1]=0
                        semiLife[ti-1][tj+1]=0
                        semiLife[ti+1][tj+1]=0
                    if(j==2 or j==5 or j==8):
                        ti=i
                        tj=j
                        semiLife[ti-1][tj-2]=0
                        semiLife[ti-1][tj-1]=0
                        semiLife[ti+1][tj-2]=0
                        semiLife[ti+1][tj-1]=0
                if(i==2 or i==5 or i==8):
                    if(j==0 or j==3 or j==6):
                        ti=i
                        tj=j
                        semiLife[ti-2][tj+1]=0
                        semiLife[ti-2][tj+2]=0
                        semiLife[ti-1][tj+1]=0
                        semiLife[ti-1][tj+2]=0
                    if(j==1 or j==4 or j==7):
                        ti=i
                        tj=j
                        semiLife[ti-2][tj-1]=0
                        semiLife[ti-1][tj-1]=0
                        semiLife[ti-2][tj+1]=0
                        semiLife[ti-1][tj+1]=0
                    if(j==2 or j==5 or j==8):
                        ti=i
                        tj=j
                        semiLife[ti-2][tj-2]=0
                        semiLife[ti-2][tj-1]=0
                        semiLife[ti-1][tj-2]=0
                        semiLife[ti-1][tj-1]=0

                semiLife[i][j]=digi
    return semiLife
def upDat(sudo,value):
    #checking row
    for i in range(9):
        sum=0
        for j in range(9):
            if(sudo[i][j]==0):
                sum=sum+1
            else:
                ti=i
                tj=j
        if(sum==8):
            if(sudo[ti][tj]==value):
                pass
            else:
                sudo[ti][tj]=value
                b[ti][tj]=value
                print("updated with value",value,"at",ti,tj)
    #checking coloumn
    for i in range(9):
        sum=0
        for j in range(9):
            if(sudo[j][i]==0):
                sum=sum+1
            else:
                ti=i
                tj=j
        if(sum==8):
            if(sudo[tj][ti]==value):
                pass
            else:
                sudo[tj][ti]=value 
                b[tj][ti]=value
                print("updated with value",value,"at",tj,ti)
    t = ["00","03","06","30","33","36","60","63","66"]
    for i in t:
        x=int(i[0])
        y=int(i[1])
        sum=0
        for j in range(2):
            for p in range(2):
                if(sudo[j+x][p+y]==0):
                    sum=sum+1
                else:
                    ti=i
                    tj=j
        if(sum==8):
            if(sudo[tj][ti]==value):
                pass
            else:
                sudo[tj][ti]=value 
                b[tj][ti]=value
                print("updated with value",value,"at",tj,ti)
            
        
    
    Board(sudo)

def temp():
    upDat(Life(9),9)
    upDat(Life(8),8)
    upDat(Life(7),7)
    upDat(Life(6),6)
    upDat(Life(5),5)
    upDat(Life(4),4)
    upDat(Life(3),3)
    upDat(Life(2),2)
    upDat(Life(1),1)
    
for i in range(8):
    temp()
Board(b)

