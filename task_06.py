import random
import copy
import math

cities = [[1380, 939], [2848, 96], [3510, 1671], [457, 334], [3888, 666], [984, 965], [2721, 1482], [1286, 525], [2716, 1432], [738, 1325], [1251, 1832], [2728, 1698], [3815, 169], [3683, 1533], [1247, 1945], [123, 862], [1234, 1946], [252, 1240], [611, 673], [2576, 1676], [928, 1700], [53, 857], [1807, 1711], [274, 1420], [2574, 946], [178, 24], [2678, 1825], [1795, 962], [3384, 1498], [3520, 1079], [1256, 61], [1424, 1728], [3913, 192], [3085, 1528], [2573, 1969], [463, 1670], [3875, 598], [298, 1513], [3479, 821], [2542, 236], [3955, 1743], [1323, 280], [3447, 1830], [2936, 337], [1621, 1830], [3373, 1646], [1393, 1368], [3874, 1318], [938, 955], [3022, 474], [2482, 1183], [3854, 923], [376, 825], [2519, 135], [2945, 1622], [953, 268], [2628, 1479], [2097, 981], [890, 1846], [2139, 1806], [2421, 1007], [2290, 1810], [1115, 1052], [2588, 302], [327, 265], [241, 341], [1917, 687], [2991, 792], [2573, 599], [19, 674], [3911, 1673], [872, 1559], [2863, 558], [929, 1766], [839, 620], [3893, 102], [2178, 1619], [3822, 899], [378, 1048], [1178, 100], [2599, 901], [3416, 143], [2961, 1605], [611, 1384], [3113, 885], [2597, 1830], [2586, 1286], [161, 906], [1429, 134], [742, 1025], [1625, 1651], [1187, 706], [1787, 1009], [22, 987], [3640, 43], [3756, 882], [776, 392], [1724, 1642], [198, 1810], [3950, 1558]]

def tsp(data):
    l = len(data)

    length = 1000000000

    path = []
    for index in range(int(l)):
        dist = 0
        p = []
        d = copy.deepcopy(data)

        # index = random.randint(0,l-1)
        d.pop(index)

        p.append(index)
        prev_x = data[index][0]
        prev_y = data[index][1]

        while len(d) != 0:

            min_dist = 100000000000
            next_v = 0

            for k in d:
                curr_dist = (float)(math.sqrt((prev_x - k[0]) ** 2 + (prev_y - k[1]) ** 2))
                if (min_dist > curr_dist):
                    min_dist = curr_dist
                    next_v = data.index(k)
            p.append(next_v)
            d.pop(d.index(data[next_v]))
            prev_x = data[next_v][0]
            prev_y = data[next_v][1]
            dist += min_dist

            if length < dist:
                break
        dist += (float)(math.sqrt((prev_x - data[index][0]) ** 2 + (prev_y - data[index][1]) ** 2))

        p.append(p[0])

        if length > dist:
            length = dist
            path = copy.deepcopy(p)
    return length, path

l,p = tsp(cities)
print l
def description():
    return "It's a realization of the Nearest neighbour algorithm. One thing that differs is that this algorithm is looking for the shortest path for each vertix taken as initial( in NNA )."
