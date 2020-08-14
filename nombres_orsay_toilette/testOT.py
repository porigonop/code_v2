
import pprint
from math import sqrt
import time

def crible(nb):
    nb_sqrt = int(sqrt(nb)) + 1 
    L = [False, False, True] + [True, False] * (nb//2 - 1)
    cur = 3 #0, 1 sont deja  traite au dessus, on commence le crible a 2

    while cur < nb_sqrt: #on s'arrete a la racine de la limite haute

        if not L[cur]:
            cur += 2
            continue
        cur22 = cur **2
        #cela evite de faire 2*3 puis 3*2
        #on commence a la position au carre
        #et on avance de la position a chaque fois jusqu'a la limite
        for i in range(cur22, nb, cur):
            #on ne test pas le modulo, deja tester grace a range
            # le gain ce fait par le debut qui est a la position cur au carre 
            # alors qu'avant on etait a la position cur et donc
            L[i] = False
        cur += 2
    return L
def wilson(range_):
    ans = []
    number = 1
    for i in range(range_):
        if i < 2:
            ans.append(False)
            continue
        number *= i-1
        #print((number + 1 )% i)
        if (number + 1) % i == 0:
            ans.append(True)
            #print(i)
        else:
            ans.append(False)
    return ans
def test_OT(n):
    for d in range(1, int(sqrt(n)) + 1):
        if (n // d ) * d == n and not(PREM[d + n//d]):
                return False
    return True

def OT_jumeau(lst_ot):
    dist = 4
    ans = []
    for i in range(len(lst_ot) - 1):
        if lst_ot[i+1] - lst_ot[i] == dist:
            ans.append((lst_ot[i], lst_ot[i+1]))
    return ans

if __name__ == "__main__":
    RANGE = 10000
    t_0 = time.time()
    PREM = wilson(RANGE+10)
    t_1 = time.time()
    print(t_1 - t_0)
    t_0 = time.time()
    PREM = crible(RANGE+10)
    t_1 = time.time()
    print(t_1 - t_0)
    print("prem fini")
    lst = [i for i in range(RANGE) if test_OT(i)]
    print("lst1 fini")
    print(lst)
    print(OT_jumeau(lst))
    t_1 = time.time()
    print(t_1-t_0)
    
    
