import random


def gcd(a, b):
    return gcd(b, a % b) if b else a

def gcd_for_several_nums(num_list):
    result = 0
    for item in num_list:
        result = gcd(result, item)
    return result

num_of_numbers = int(input("Enter the number of numbers: "))
list_ = [random.randint(1, 100) for i in range(num_of_numbers)]
gcd_num = int(input("Enter the gcd number: "))
print(list_, gcd_num)
gcd_num_dividible = []
for number in list_:
    if number % gcd_num == 0:
        gcd_num_dividible.append(number)
        print(number)

local_gcd = gcd_for_several_nums(gcd_num_dividible)
if local_gcd == gcd_num:
    print(gcd_num_dividible)

