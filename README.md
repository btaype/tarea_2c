# Perm2c
####  Perm2c-Algebra Abstracta

**Integrantes**

-Marcelo Torres Acuña

-Jhon Berly Taype Alccaccahua 

-Brian Bermudez Navarro

#### 1 .(5 points) Si m es el mensaje y c es el cifrado (ambos representados por un entero). Y además, la clave pública es P ={e,n}(en ese orden). Hallar m cuando:

P = {65537;999630013489} y c=747120213790
   
```
n=99630013489
aux=99630013489
e=65537
c =747120213790
lista=[]
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

```
