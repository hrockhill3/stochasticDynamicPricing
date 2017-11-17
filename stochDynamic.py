import math
import numpy
alpha=float(1000)/23500
#proba for a customer to buy an item (result no decrease no increase)
k=25
#number of products available. result increase with k

c=29
#cost of one unit

landa=30
#number of people arriving in one t period. landa=lead/(numOfDayMonth*24*4)
#it corresponds to 4 changes every hour. coincidence landa=15 and 15 mins
T=24
#T corresponds to 6 hours. Every 6 hours we run again



listRound=[11,17,21,25,37,39,42,45,48,51,57,59,65,67,79,85,89]
def myRound( x,listRound):
    minRound=[abs(x-l) for l in listRound]
    return listRound[numpy.argmin(minRound)]
#test time...

l=[(1,25),(2,24),(3,24),(4,23),(5,22),(6,22),(7,20),(8,20),(9,19),(10,17),(11,15),(12,13),(13,13),(14,13),(15,14),(16,14),(17,13),(18,10),(19,8),(20,8),(21,7),(22,6),(23,6),(24,5)]
constant=math.exp(1+alpha*c)
sum=0
for k in range(0,24):
    sumNum=0
    sumDen=0

    for j in range(0,l[k][1]+1):
        calcNum= (math.pow(landa,j)*math.pow(T-l[k][0],j)*math.exp(-j*(1+alpha*c)))/math.factorial(j)
    
        sumNum+=calcNum
    

    for i in range(0,l[k][1]):    
        calcDen= (math.pow(landa,i)*math.pow(T-l[k][0],i)*math.exp(-i*(1+alpha*c)))/math.factorial(j)
        sumDen+=calcDen
    
    quotient=sumNum/sumDen  
    result=(1/alpha)*math.log(constant*quotient,math.exp(1))

    
    print "The prices of the upgrades for those 30 minutes are: "
    if k==0:
        print 19
        print 30
        print 50
        print 59
        print 159
        prev=result
        
    else:
        improvement=float(result-prev)/prev
        prev=result
        if improvement>0.5:
            print  int (19*1.5)
            print  int(30*1.5)
            print  int(50*1.5)
            print 87
            print 137
        else:
            if improvement<-0.5:
                print  int(19*0.5)
                print  int(30*0.5)
                print  int(50*0.5)
                print 35
                print 135
            else:
                prcentage=float(myRound((59*(1+improvement)),listRound))/59
                print int(19*(1+improvement))
                print int(30*(1+improvement))
                print int(50*(prcentage))
                print myRound((59*(1+improvement)),listRound)
                print myRound((59*(1+improvement)),listRound)+100