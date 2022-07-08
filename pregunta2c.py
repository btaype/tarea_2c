import random
import math
from random import sample

def EXPMOD(a, x, n):
    c=a%n
    r=1
    while(x>0):
        if((x%2)!=0):
            r=(r*c)%n
        c=(c*c)%n
        x=int(x/2)
    return r
def es_compuesto(a,n,t,u):
    x=EXPMOD(a,u,n)

    if (x==1 or x==n-1):
        return False
    for i in range(1,t,1):
        x=EXPMOD(x,2,n)
        if (x==n-1):
            return False
    return True
  
def MILLER_RABIN(n, s):
    t=0
    u=n-1
    while(u%2==0):
        u=u/2
        t=t+1
    list_a=[]
    nj=0
    while(nj<s):
        a=random.randint(2,n-1)
        if (a not in list_a):
            list_a.append(a)
            if(es_compuesto(a,n,t,u)):
                return False
            nj=nj+1
    return True
def euclides(a, b):
    if b == 0:
        return a
    else:
        return euclides(b, a % b)

def e_euclides(a,b): 
    if (b == 0):
      return a,1,0
    d,x1,y1 = e_euclides(b, a % b)
    x = y1
    y = x1 - y1 *int (a / b)
    return d,x,y
def PHI(n):
    r = 0
    for i in range(1,n):
        d = euclides(i, n)
        if (d == 1):
            r = r + 1
    return r
def inverso(a,n):
  if (euclides(a,n)==1):
    d,x,y=e_euclides(a,n)
    return(x%n)
  else:
    return "No tiene inverso"

e=7
n=  35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516111204504060317568667
c=  35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516052471686245831933544
e_2=11
c_2=35794234179725868774991807832568455403003778024228226193532908190484670252364665786748759822531352444533388184
mcd,x,y=e_euclides(e,e_2)

c_1=inverso(c,n)
x=x*-1

if(mcd==1 and euclides(c_2,n)):
    m=(EXPMOD(c_1, x, n)*EXPMOD(c_2, y, n))%n
print("e: ",e)
print("c: ",c)
print("n: ",n)
print("e_2: ",e_2)
print("c_2: ",c_2)
print("x: ",-1*x)
print("y: ",y)
print("m: ",m)




