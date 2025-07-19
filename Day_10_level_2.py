suma=0
for i in range(0,101):
    print(i)
    suma=suma+i
print(suma)
par=0
inpar=1
suma1=0
suma2=0
while par <=100:
    print(par)
    suma1=suma1+par
    par=par+2
while inpar <=100:
    print(inpar)
    suma2=suma2+inpar
    inpar=inpar+2
print("Sum of all evens=",suma1,"Sum of all odds=",suma2)
