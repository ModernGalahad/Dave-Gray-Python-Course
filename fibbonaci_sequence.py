
n1 = input("\nInput a number.\n")
n = int(n1)

a = 0
b = 1
fib_sequence = []


for i in range(n):
    fib_sequence.append(a)
    a += b

print(fib_sequence)