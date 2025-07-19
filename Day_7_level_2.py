A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
AB=A.union(B)
BA=B.union(A)
print("\n","Here is the union between the sets A and B: ",AB)#1
print("\n","Here are the intersections between A and B: ",A.intersection(B))#2
print("\n","Is A a subset of B? ",A.issubset(B))#3
print("\n","Are A and B disjoint sets? ",A.isdisjoint(B))#4
print("\n","Here is A whith B: ",AB," And B with A: ",BA)#5
print("\n","What is the symetric diference between A and B? ",A.symmetric_difference(B))#6
del A#7
del B
del AB
del BA
