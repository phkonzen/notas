n = int(input('Digite um número natural n>=1:\n'))
primo = True
for i in range(2, n//2+1):
    if (n % i == 0):
        primo = False
        break
print(f'{n} é primo? {primo}')

max_iter = 50
tol = 1e-15

x = float(input('Digite um número não negativo para x:\n'))

r0 = 1
k = 0
print(f'{k}: {r}')
for k in range(max_iter):
    r = 0.5*(r0 + x/r0)
    print(f'{k+1}: {r}')
    if (abs(r-r0) < tol):
        break
    r0 = r
print(f'sqrt({x}) = {r}')


n = int(input('Digite um número natural n:\n'))
soma = 0
for i in range(1,n+1):
    soma = soma + i
print(f'1 + ... + {n} = {soma}')

for i in range(13,2,-1):
    print(i)

soma = 0
for x in {1,3,5,7}:
    soma = soma + x
media = soma/4
print(f'média = {media}')
