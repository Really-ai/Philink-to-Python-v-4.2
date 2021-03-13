import pandas as pd
import datetime
import math
import os#?
import sys#?


#location =r"C:\Users\Maximus E Dizon\Desktop\Philink to Python v 1\PhilinkToPython.xlsx"
location="PhilinkToPython 4.22.xlsx"
choice=0
UI_size=42
def E(arn):
    earns=0
    for sec in transactions:
        if (sec[1]=='Output PC' and (sec[4]=='PC '+str(arn)or sec[4]=='PC'+str(arn))):
            earns+=sec[2]
            #print(sec)
            #print(earns)
    return earns

def S(hare):
    split=distribution[hare-1]
    sums=0
    totalshares=[]
    for num in range(1,len(split)):
        sums+=split[num][1]
    for num in range(1,len(split)):
        print(str(split[num][0])+': '+str(split[num][1]/sums*E(hare)))

def Shares():
    if (totalshares==[]):
        for hare in range(1,len(distribution)+1):
            split=distribution[hare-1]
            #print(split)
            sums=0
            for num in range(1,len(split)):
                sums+=split[num][1]
            for num in range(1,len(split)):
                add=True
                for nameval in totalshares:
                    if (nameval[0]==split[num][0]):
                        add=False
                        nameval[1]+=split[num][1]/sums*E(hare)
                        nameval[2]+=split[num][1]
                if add:
                    totalshares.append([split[num][0],split[num][1]/sums*E(hare),split[num][1]])
def Es(arn,date):
    ## Computes for the total earnings for that computer from that given date onwards
    earns=0
    for sec in transactions:
        if (sec[1]=='Output PC' and (sec[4]=='PC '+str(arn)or sec[4]=='PC'+str(arn)) and date<=sec[3]):
            earns+=sec[2]
    
            #print(sec)
            #print(earns)
    ## Computes for the total investment for that computer
    split=distribution[arn-1]
    sums=0
    totalshares=[]
    for num in range(1,len(split)):
        sums+=split[num][1]
        
    return earns/sums

def Shares_Max():
    print(distribution)
    if (totalshares==[]):
        for hare in range(1,len(distribution)+1):
            split=distribution[hare-1]
            #print(split)
            sums=0
            for num in range(1,len(split)):
                sums+=split[num][1]
            for num in range(1,len(split)):
                add=True
                for nameval in totalshares:
                    if (nameval[0]==split[num][0]):
                        add=False
                        nameval[1]+=split[num][1]/sums*E(hare)
                        nameval[2]+=split[num][1]
                if add:
                    totalshares.append([split[num][0],split[num][1]/sums*E(hare),split[num][1]])
            #print(str(split[num][0])+': '+str(split[num][1]/sums*E(hare)))
    #print(totalshares)

def Shareni(name):
    for arrays in totalshares:
        if (name == arrays[0]):
            tit(name+"'s Shares")
            bod("Return:     ₱ {:.2f}".format(arrays[1]))
            bod("Investment: ₱ {:.2f}".format(arrays[2]))
            end()

def Sharenila():
    Shares()
    for arrays in totalshares:
        print("{} Php {:.2f}".format(arrays[0],arrays[1]))



def tit(Text):
    print( '{:{}^{}} ' .format(Text,"*",UI_size))
    
def bod(Text):
    print("* {:{}<{}}*".format(Text," ",UI_size-3))

def opt(*arg):
    for num in range(0,len(arg)):
        print("*{:{}<{}}*".format(" [{}] {}".format(num+1,arg[num])," ",UI_size-2))

def end():
    print("*"*UI_size)
    
def endl():
    global choice
    print("*"*UI_size)
    choice=eval(input(">>> "))
# How to Display: Desu
# How to do padding
# Example: $one:{$two}$three{$four}
# $one:     Text
# $two:     filler char or text
# $three:   can be < for left padding, > for right padding, and = for center padding
# $four:    Maximum limit of filler char, is a number
# Template: print( '{:{}^{}}' .format("","*",35))
# Template: print("*{:{}<{}}*".format(""," ",33))
# Template: print("*"*35)

#tit("")
#opt("")
#end()
#endl()

def menu():
    while (True):
        global choice
        print("Desc.: Enter a number to continue..")
        tit("PHILINK")
        tit("MENU")
        opt("Shares","Sum","Tools","Return Maxifier","All Return Maxifier","Exit")
        endl()
        
        if choice==1:
            Shares()
            tit("Shares")
            opt("of Owner","of All")
            endl()
            if choice==1:
                tit("Owner Name")
                owners=[]
                for arrays in totalshares:
                    owners.append(arrays[0])
                opt(*owners)
                end()
                name=eval(input("Owner Number:\n>>> "))
                Shareni(owners[name-1])
            elif choice==2:
                Sharenila()
                
        elif choice==2:
            print(("Php {:.2f}".format(money)))
        elif choice==3:
            tit("Tools")
            opt("Per PC","Per Owner","Total")
            end()
        elif choice==4:
            Shares()
            tit("Return Maxifier")
            #owners=[]
            #for arrays in totalshares:
                #owners.append(arrays[0])
            #opt(*owners)
            #end()
            #name=eval(input("Owner Number:\n>>> "))
            #Shareni(owners[name-1])
            amount=(eval(input("Enter Amount:\n>>> ")))
            tit("The Months")
            opt("January","February","March","April","May","June","July","August","September","October","November","December")
            end()
            month=(eval(input("Enter Month (in num):\n>>> ")))
            day=(eval(input("Enter Day:\n>>> ")))
            year=(eval(input("Enter Year:\n>>> ")))
            date=datetime.datetime(year, month, day)
            revs=[]
            for num in range(1,int(max(PC))+1):
                  revs.append(amount*Es(num,date))
            print(revs)
            print(max(revs))
        elif choice==5:
            Shares()
            tit("All Return Maxifier")
            owners=[['France',500,datetime.datetime( 2017, 1, 21)],['Max',1500,datetime.datetime( 2017, 3, 10)],['Gedric',8000,datetime.datetime( 2017, 10, 10)],['France',1200,datetime.datetime( 2017, 11, 9)],['Max',2000,datetime.datetime( 2017, 11, 9)],['Gedric',2000,datetime.datetime( 2017, 12, 8)],['Andrei',100,datetime.datetime( 2018, 2, 15)],['France',1000,datetime.datetime( 2018, 3, 15)],['Jetro',1000,datetime.datetime( 2018, 8, 28)],['Keryn',1200,datetime.datetime( 2018, 12, 31)],['Andrei',100,datetime.datetime( 2017, 12, 4)],['Andrei',100,datetime.datetime( 2018, 2, 15)],['Andrei',100,datetime.datetime( 2018, 3, 15)],['Andrei',200,datetime.datetime( 2018, 5, 25)]]

            #owners=[]
            #for arrays in totalshares:
                #owners.append(arrays[0])
            #opt(*owners)
            #end()
            #name=eval(input("Owner Number:\n>>> "))
            #Shareni(owners[name-1])
            for owner in owners:
                revs=[]
            
                for num in range(1,int(max(PC))+1):
                    revs.append(owner[1]*Es(num,owner[2]))
                owner.append(max(revs))
                #print("Owner: {}\nBefore: {}\nAfter: {}".format(owner[0],owner[1],max(revs)))

            names=[]
            for owner in owners:
                if owner[0] not in names:
                    names.append(owner[0])
            print(names)

            for name in names:
                end_sum=0
                for owner in owners:
                    if owner[0]==name:
                        end_sum+=owner[3]
                print("Owner:{}\n Sum: {}".format(name,round(end_sum, 2)))
                
            
        else:
            break
        choice=input()
        #os.execl(sys.executable, sys.executable, * sys.argv)
    
df = pd.read_excel(location, sheet_name='Sheet1')
C1=df.columns[0]
C2=df.columns[1]
C3=df.columns[2]
C4=df.columns[3]
C5=df.columns[4]
C8=df.columns[7]
C9=df.columns[8]
C10=df.columns[9]

Transactor=list(df[C1])
Purpose=list(df[C2])
in_Pesos=list(df[C3])
Date=list(df[C4])
Remarks=list(df[C5])

Owner=list(df[C8])
Amount=list(df[C9])
PC=list(df[C10])

distribution=[]
transactions=[]
totalshares=[]
dist_temp=[]

for num in range(0,len(Transactor)):
    transactions.append([Transactor[num],Purpose[num],in_Pesos[num],Date[num],Remarks[num]])

for num in range(0,len(PC)):
    if math.isnan(PC[num]):
        break
    dist_temp.append([int(PC[num]),[Owner[num],Amount[num]]])
    
for num in range(1,int(max(PC))+1):
    temp1=[num]
    for index in  dist_temp:
        if (num<index[0]):
            break
        elif num==index[0]:
            temp1.append(index[1])
    distribution.append(temp1)

money=sum(in_Pesos)

menu()
## Create a nice user interface
#Shares()
#Shareni()

