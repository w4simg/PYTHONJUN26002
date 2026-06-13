#Find how many numbers between 1 and 100 are divisible by 5.

w = 0

for x in range(1, 101):
    if x % 5 == 0:
        w += 1

print("total numbers Divisible by 5 =", w)