numbers = input("Enter numbers to find GCD ")
num_list = list(map(int, numbers.split()))
print(*num_list)

def gcd(a, b):
    return gcd(b, a % b) if b else a

def gcd_for_several_nums(num_list):
    result = 0
    for item in num_list:
        result = gcd(result, item)
    return result

print(gcd_for_several_nums(num_list))

