dots = input("Enter coordinates of dots: ")
xa, ya, xb, yb = list(map(int, dots.split(" ")))
x_left = min(xa, xb)
x_right = max(xa, xb)
y_top = max(ya, yb)
y_bottom = min(ya, yb)

print(x_left, x_right, y_top, y_bottom)

x_length = abs(x_right - x_left)
y_length = abs(y_bottom - y_top)

print(x_length, y_length)

k = (ya - yb) / (xa - xb)
b = ya - k * xa
counter = 0

for i in range(x_length + 1):
    x = x_left + i
    y = 0
    for j in range(y_length + 1):
        y = y_bottom + j
        result = k * x + b
        if y == result:
            print(x, y)
            counter = counter + 1

print(counter, '\n')


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def dots(x_length, y_length):
    return 1 + gcd(x_length, y_length)


print(dots(x_length, y_length))
