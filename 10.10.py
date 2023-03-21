a = [5, 15, 45, 64]


def gcd(a, b):
    return gcd(b, a % b) if b else a


suffix = [0] * (len(a) + 1)
print(suffix)
for i, item in reversed(list(enumerate(a))):
    suffix[i] = gcd(suffix[i + 1], item)
    print(f'{suffix[i] = }, {i = }, {item = }')
print(suffix)

answer = 0
prefix = 0
for i, item in enumerate(a):
    answer = max(answer, gcd(prefix, suffix[i+1]))
    prefix = gcd(prefix, item)
    print(f'{i = }, {item = },{answer = }, {prefix = }')
print(answer)
