list_ = [[3, 8, 7], [11, 2, 3], [41, 5, 6]]

newlist = sorted(list_, key=lambda item: item[1])

print(newlist)