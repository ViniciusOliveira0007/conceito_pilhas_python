
p1 = [1, 2, 1, 3, 2, 4, 1, 7, 7, 3]
p2 = [] 

while p1:
    valor = p1.pop(0)
    if valor not in p2:    
        p2.append(valor)  

print(p2)