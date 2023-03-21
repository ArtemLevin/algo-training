numbers = input("Enter numbers t find GCD ")
a, b = list(map(int, numbers.split()))
print(f'{a = }, {b = }')

def gcd(a, b):
    return gcd(b, a%b) if b else a

gcd(a, b)