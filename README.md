# Perm2c
####  Perm2c-Algebra Abstracta

**Integrantes**

-Marcelo Torres Acuña

-Jhon Berly Taype Alccaccahua 

-Brian Bermudez Navarro

#### 1 .(5 points) Si m es el mensaje y c es el cifrado (ambos representados por un entero). Y además, la clave pública es P ={e,n}(en ese orden). Hallar m cuando:

P = {65537;999630013489} y c=747120213790

El siguiente algoritmo encuentra tres números primos que multiplicados me dan n, todo acumulada en una lista.
El (for i=3) recorre todos los números impares comenzando del 3 hasta encontrar el primer número que divide a “n” ya a la vez es primo, el while se detendrá cuando “n” entre “i” sea primo.

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

#### *Output:*

```
[41, 109, 22293581]
```
Como se ve nos dio tres números primos que multiplicados me dan n, todo esto con la finalidad de hallar phi(n) y “d”. 

para hallar phi multiplicamos cada uno de los elementos de la lista pero descontando 1, y paara hallar "d" hallamos la inversa de e mod phi
```
phi=1 
 
for i in lista:
    phi=phi*(i-1)

d=inverso(e,phi)
```
#### *Output:*
```
phi:  96308265600
d:  64030147073
```

Buscamos un numero "X"que se encuentre en el rango de 0 hasta n-1 y a la vez x tiene que ser coprimo con n, a continuacion hallamos un c' que es la multiplicacion de 
(c*x**e )mod n, luego con los valores obtenidos de "d" hallamos el m'que esta dado por c'**d mod n, por ultimo hallaremos el m'*la inversa de x mod n y asi obtendremos
el valor m.
```
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
```
####*Output:*
```
n:  99630013489
e:  65537
c:  747120213790
phi:  96308265600
d:  64030147073
m:  18649707670
comprobar:  18649707670
```
COMPROBAMOS c**d mod n = m, con el "d" que hallamos si nos retorna el mismo valor de m

#### 2. 7 points) Si m es el mensaje y c es el cifrado (ambos representados por un entero). Y además, la clave pública es P = {e, n} (en ese orden). Hallar m cuando:

P ={7, 357942341797258687749918078325684554030037780242282261
93532908190484670252364677411513516111204504060317568667}

c =35794234179725868774991807832568455403003778024228226193
532908190484670252364677411513516052471686245831933544

Sin embargo al enviar el mismo mensaje (m) cuando e' = 11, el cifrado resulto ser
c'=357942341797258687749918078325684554030037780242282261935329081
90484670252364665786748759822531352444533388184

primero e' tiene que ser coprimo con e y c' con n tambien tiene que ser coprimo y con el teorema extendido de euclides lo aplicamos en e' y e hallando x e y, como
x en este caso es negativo lo multiplicamos por -, y hallamos la inversa de e.
```
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
```

#### *Output:*
```
e:  7
c:  35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516052471686245831933544
n:  35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516111204504060317568667
e_2:  11
c_2:  35794234179725868774991807832568455403003778024228226193532908190484670252364665786748759822531352444533388184
x:  -3
y:  2
m:  13827831465063886838020624394233523964302535713793476149786042550018831062823603673726648906292457820275857059

```
#### 3.(8 points) Validar firmas digitales: Verificar que P(S(m)) = HASH(M) para 3 mensajes distintos, mostrando la respectiva firma σ en cada caso. Utilice la Función Hash SHA-1 para generar m a trav´es de un texto M ( por ejemplo Hola Mundo). Utilizar b = 32 bits en el algoritmo RSA.


hallamos d y n con el algoritmo RSA de 32 bits, elegimos 3 textos y de cada uno hallaremos su hash SHA-1 y lo convertiremos a hexadecimal para luego volver a convertirlo a decimal que tomara el valor de m, como m>n hallaremos el m mod n para no tener inconvenientes a la hora de hallar S(m)=phi que sera la firma y luego para verificar aplicamos p(phi)=phi**e mod n que tendra que ser mismo valor de m.

```
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
```

#### *Output:*
```


```




