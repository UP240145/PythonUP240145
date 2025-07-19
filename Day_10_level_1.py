i=0
for i_ in range(0,11):
    print(i_)
while i <= 10:
    print(i)
    i=i+1
for i_ in range(10,-1,-1):
    print(i_)
while i >= 1:
    i=i-1
    print(i)
for i_t in range(1, 8):
    print('#' * i_t)
for i_c in range(8):  
    for j in range(8):  
        print('#', end=' ')
    print()  
for i_p in range(0,11):
    print(i_p,"x",i_p,"=",i_p*i_p)
lista=['Python', 'Numpy','Pandas','Django', 'Flask']
for i_l in range(0,5):
    print(lista[i_l])
par=0
inpar=1
while par <100:
    par=par+2
    print(par)
while inpar <100:
    print(inpar)
    inpar=inpar+2