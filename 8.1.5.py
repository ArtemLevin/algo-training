import math

n = input("Enter the number of dots ")
coordList = []
i_list = []
j_list = []
for i in range(int(n)):
    coords = input("Enter coordinates ")
    coord = list(map(int, coords.split()))
    i_list.append(coord[0])
    j_list.append(coord[1])
    coordList.append(coord)
print(coordList)

i_min = min(i_list)
j_min = min(j_list)
j_max = max(j_list)
i_max = max(i_list)
distanceList = []

coord_and_dist_List = []
for i in range(i_min, i_max + 1):
    distance = 0
    for j in range(j_min, j_max + 1):
        distance = 0
        for coord in coordList:
            distance += abs(i - coord[0]) + abs(j - coord[1])
        coord_and_dist_List.append([distance, i, j])
        # print(coord_and_dist_List)

coord_and_dist_List.sort()
print(f'i = {coord_and_dist_List[0][1]}, j = {coord_and_dist_List[0][2]}, distance = {coord_and_dist_List[0][0]}')



def dots_visualisation(coordList, i_max, j_max):
    for i in range(i_max + 1):
        for j in range(j_max + 1):
            if [i, j] in coordList:
                print(f"{'O':^5}", end='')
            elif [i, j] not in coordList:
                print(f'{"*": ^5}', end='')
        print()

dots_visualisation(coordList, i_max, j_max)
