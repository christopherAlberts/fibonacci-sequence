# fibonacci array

n = 10
fibonacci_arr = []
a = 0
b = 1

# Build fibonacci array
for num in range(n):
    fibonacci_arr.append(a)
    c = a + b
    a = b
    b = c

print(fibonacci_arr)

