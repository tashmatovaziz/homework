from random import randint, choice

b = []
for i in range(12):
    b.append(randint(0, 100))
print(f'unsorted list: {b}')


def buble_sort(ls:list):
    for i in range(len(ls) - 1):
        for j in range(len(ls) - 1 - i):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
    return ls


value = choice(buble_sort(b))
print(f'desired number: {value}')
print(f'sorted list: {b}')


def binary_search(val, A):
    n = len(A)
    First = 0
    Last = n - 1
    while True:
        if First < Last:
            Middle = (First + Last) // 2
            if val == A[Middle]:
                First = Middle
                Last = First
                Pos = Middle
                print(f'i found the number i was looking for\nposition: {Pos}')
                break
            elif val > A[Middle]:
                First = Middle + 1
            else:
                Last = Middle - 1
        else:
            print(f'element not found')
            break


binary_search(value, b)
