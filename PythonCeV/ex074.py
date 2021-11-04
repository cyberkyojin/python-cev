import random

num = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10),
    random.randint(1, 10), random.randint(1, 10))

print('-' * 15)
print(num)
print('-' * 15)
print(f'o maior numero foi: {max(num)}')
print('-' * 15)
print(f'o menor numero foi: {min(num)}')