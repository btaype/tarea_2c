import random
import math
from random import sample
import hashlib
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

def Random_bits(b):
    n=(pow(2,b-1)-1)
    n=random.randint(0,n)
    m=pow(2,b-1)+1
    n=n | m
    return n

def Random_primos(b):
    
    n=Random_bits(b)
    n=n+1-(n%2)
    while(True):
        if(MILLER_RABIN(n, 40)):
            return n
        else:
            n=n+2
def imprimir(a):
    for i in (a):
        print(i)

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
    y = x1 - y1 * int(a / b)
    return d,x,y

def inverso(a,n):
  if (euclides(a,n)==1):
    d,x,y=e_euclides(a,n)
    return(x%n)
  else:
    return "No tiene inverso"

def RSA(k):
    
    p=Random_primos(int(k/2))
    while (True):
        q=Random_primos(int(k/2))
        if (p!=q):
            break
    n=p*q
    phi_n=(p-1)*(q-1)
    while (True):
        e=random.randint(2,n-1)
        if(euclides(e,phi_n )==1):
            break    
    d=inverso(e,phi_n)    
    return e,d,n

h=hashlib.sha1()  
e,d,n=RSA(32)
print("e:",e)
print("d:",d)
print("n:",n)
palabra=[]
h.update(b"Hola Mundo")
palabra.append(h.hexdigest())
h.update(b"Caminos del odio")
palabra.append(h.hexdigest())
h.update(b"Solo es bromita")
palabra.append(h.hexdigest())
palabras=["Hola Mundo","Caminos del odio","Solo es bromita"]
print("-"*151)
print("|{:^40}|{:^45}|{:^20}|{:^20}|{:^20}|".format("M","HASH","m","phi=m^d mod n","m'=phi^e mod n"))
print("-"*151)
for i in range(3):    
    m=int(palabra[i],16)
    m=m%n
    
    phi = EXPMOD(m, d, n)
    
    m_i = EXPMOD(phi, e, n)
    
    print("|{:^40}|{:^45}|{:^20}|{:^20}|{:^20}|".format(palabras[i],palabra[i],m,phi,m_i))
    print("-"*151)

