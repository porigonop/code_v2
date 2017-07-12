from math import sqrt
import time
nb = 100000000

def crible(nb):
    nb_sqrt = int(sqrt(nb)) + 1 
    L = [False, False, True] + [True, False] * (nb//2 - 1)
    cur = 3 #0, 1 sont déj�  traité au dessus, on commence le crible �  2

    while cur < nb_sqrt: #on s'arréte �  la racine de la limite haute

        if not L[cur]:
            cur += 2
            continue
            
        cur22 = cur **2
        #cela evite de faire 2*3 puis 3*2
        
        #on commence a la position au carré
        #et on avance de la position a chaque fois jusqu'a la limite
        for i in range(cur22, nb, cur):
            #on ne test pas le modulo, deja tester grace a range
            # le gain ce fait par le debut qui est a la position cur au carré 
            # alors qu'avant on était a la position cur et donc
            L[i] = False

        cur += 2
    return L
t_0 = time.time()
prem = crible(nb)
nb_prem =[i for i, is_valid in enumerate(prem) if is_valid]
t_1 = time.time()
print(t_1 - t_0)
print(len(nb_prem))
#print(nb_prem)
