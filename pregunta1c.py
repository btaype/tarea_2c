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
    y = x1 - y1 * (a / b)
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

n=99630013489
aux=99630013489
e=65537
c =747120213790

lista=[]
D=0
while (True):
    for i in range(3,aux,2):
        if(aux%i==0):
            if(MILLER_RABIN(i,20)):
                k=i
                break
    lista.append(k)
    h=int(aux/k)
    if(MILLER_RABIN(h,20)):
        lista.append(h)
        
        break
    aux=h
    
phi=1 
 
for i in lista:
    phi=phi*(i-1)

d=inverso(e,phi)
for i in range(n):
    if (euclides(i, n)==1):
        x=i
        break

c_1=((c%n)*(EXPMOD(x, e, n)))%n
m_1=EXPMOD(c_1, d, n)
x_1=inverso(x,n)
m=(m_1*x_1)%n
print("n: ",n)
print("e: ",e)
print("c: ",c)
print("phi: ",phi)
print("d: ",d )
print("m: ",m)
#SD=EXPMOD(m, e, n)
#comprobacion
dr=EXPMOD(c, d, n)
print("comprobar: ",dr)







        
       

