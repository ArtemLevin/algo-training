import random

a = [random.randint(1, 100) for i in range(50)]
print(a)


def gcd(a, b):
    return gcd(b, a % b) if b else a


def gcd_for_several_nums(num_list):
    result = 0
    for item in num_list:
        result = gcd(result, item)
    return result

max_gcd = 0
for element in a:
    index_element = a.index(element)

    gcd_right = gcd_for_several_nums(a[index_element + 1:])
    gcd_left = gcd_for_several_nums(a[:index_element])
    final_gcd = gcd(gcd_left, gcd_right)
    if final_gcd > max_gcd: max_gcd = final_gcd
    # print(f"{element = }, {gcd_left = }, {gcd_right = }, {final_gcd = }")
print(max_gcd)