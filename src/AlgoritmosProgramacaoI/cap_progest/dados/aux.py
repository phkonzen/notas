n = int(input('Digite um número natural n:\n'))
soma = 0
for i in range(n):
    soma = soma + i
print(f'1 + ... + {n} = {soma}')

for i in range(13,2,-1):
    print(i)

soma = 0
for x in {1,3,5,7}:
    soma = soma + x
media = soma/4
print(f'média = {media}')
