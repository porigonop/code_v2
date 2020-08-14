import time
RANGE = 10000000

"""
def crible(range_):
    ans = [False, False] + [ True for _ in range(2, range_)]
    number = [i for i in range(range_)]
    for i in range(range_):
        if ans[i]:
            for indice in number[::i][2:]:
                ans[indice] = False

    return ans
PREM = crible(RANGE+10)
t_0 = time.time()
for i in range(RANGE):
    if not(False):
        pass
print(time.time()-t_0)


t_0 = time.time()
for i in range(RANGE):
    if False:
        pass
    else:
        pass
print(time.time()-t_0)


def test_OT(n):
    for d in range(1, n):
        if (n // d )*d==n and not(PREM[d + n//d]):
                return False
    return True
def test_OT1(n):
    for d in range(1, n):
        if (n // d )*d==n:
            if PREM[d + n//d]:
                pass
            else:
                return False
                
    return True


t_0 = time.time()
for i in range(RANGE):
    if test_OT(i):
        pass
    else:
        pass
print(time.time()-t_0)

a = test_OT1
t_0 = time.time()
for i in range(RANGE):
    if a(i):
        pass
    else:
        pass
print(time.time()-t_0)
"""
t_0 = time.time()
for i in range(RANGE):
    if True or False:
        pass
print(time.time()-t_0)

t_0 = time.time()
i = 0
while i < RANGE:
    if True or False:
        pass
    i += 1
print(time.time()-t_0)



