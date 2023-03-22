from functools import reduce

amount_of_fractions = int(input("Enter the amount of fractions: "))
fractions = []
for i in range(1, amount_of_fractions + 1):
    fraction = input("Enter numerator and denominator: ")
    numerator, denominator = list(map(int, fraction.split()))
    fractions.append((numerator, denominator))
print(f'{fractions}')


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def gcd_for_several_nums(num_list):
    result = 0
    for item in num_list:
        result = gcd(result, item)
    return result


def lcm(numbers):
    return reduce(lambda x, y: x * y // gcd(x, y), numbers)

numerators = []
denominators = []
for i in range(amount_of_fractions):
    numerators.append(fractions[i][0])
    denominators.append(fractions[i][1])

lcm_numerators = lcm(numerators)
gcd_denominators = gcd_for_several_nums(denominators)

print(f'LCM of numerators: {lcm_numerators}')
print(f'GCD of denominators: {gcd_denominators}')

for i in range(amount_of_fractions):
    result = ((fractions[i][1]) * lcm_numerators) % ((fractions[i][0]) * gcd_denominators)
    if result == 0:
        print(f'{result = }')
        print(f'{fractions[i][0]} / {fractions[i][1]} ')
    else:
        print(f'{result = }')
        print(f'{fractions[i][0]} / {fractions[i][1]} is not')
if gcd_denominators != 0:
    print(f'{lcm_numerators}/{gcd_denominators}')
else: print("-1")
