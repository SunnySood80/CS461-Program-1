import queue
import math
def start():
    while True:
        try:
            city1 = input("Starting city? -> ")
            if city1 not in coord_dict.keys():
                raise IOError
            return city1
        except:
            print("invalid location")
def end():
    while True:
        try:
            city2 = input("Target city? -> ")
            if city2 not in coord_dict.keys():
                raise IOError
            return city2
        except:
            print("invalid location")
def coordinates_dict():
    coord_dict = {}
    read = open("coordinates.txt", 'r+')
    for l in read:
        l = l.strip('\n')
        l = l.split(' ')
        coord_dict[l[0]] = l[1], l[2]
    return coord_dict
def adjacent_dict():
    adjacent_dict = {}
    read = open("Adjacencies.txt", 'r+')
    for l in read:
        l = l.strip('\n')
        l = l.split(' ')
        k = l[0]
        l.remove(k)
        values = []
        for i in l:
            values.append(i)
        adjacent_dict[k] = values
    read.close()
    for k in list(adjacent_dict):
        for item in adjacent_dict[k]:
            if item not in adjacent_dict.keys():
                adjacent_dict.update({item: [k]})
            elif k not in adjacent_dict[item]:
                temp = adjacent_dict[item]
                temp.append(k)
                adjacent_dict.update({item: temp})
    return adjacent_dict
def dist_citites(target: str, next: str):
    target_coord = coord_dict[target]
    next_coord = coord_dict[next]
    x = float(target_coord[0]) - float(next_coord[0])
    y = float(target_coord[1]) - float(next_coord[1])
    x = x * x
    y = y * y
    dist = math.sqrt(x + y)
    return dist
def bfs(target: str, curr: str):
    priority = queue.PriorityQueue()
    visited = [curr]
    while True:
        cities = adj_dict[curr]
        for city in cities:
            if city in visited:
                pass
            else:
                dist_city = (dist_citites(target, city), city)
                priority.put(dist_city)
        place = priority.get()
        visited.append(place[1])
        if visited[-1] == target:
            break
        else:
            curr = visited[-1]
    return visited
def dist_total(places: list):
    longitudegitude_conv = 54
    latitudeitude_conv = 69
    dist = 0
    for x in range(len(places) - 1):
        city_1 = coord_dict[places[x]]
        city_2 = coord_dict[places[x + 1]]
        latitude = float(city_1[0]) - float(city_2[0])
        longitude = float(city_1[1]) - float(city_2[1])
        latitude = latitude * latitudeitude_conv
        longitude = longitude * longitudegitude_conv
        latitude = latitude * latitude
        longitude = longitude * longitude
        dist = math.sqrt(latitude + longitude)
        dist += dist
    return dist
def loop_again():
    options = ['Y', 'y', 'N', 'n']
    while True:
        option = input("Calculate another route? 'Y' 'N' --> ")
        if option not in options:
            print("Plnease answer: 'Y' or 'N'")
        else:
            if option == 'Y' or option == 'y':
                return True
            else:
                return False
if __name__ == "__main__":
    adj_dict = adjacent_dict()
    coord_dict = coordinates_dict()
    print("Input is case sensitive!\n")
    while True:
        start_here = start()
        end_here = end()
        route = bfs(end_here, start_here)
        for city in route:
            if city != route[-1]:
                print(city, " -> ", end="", flush=True)
            else:
                print(city)
        print("\nTravel distance:", round(dist_total(route), 2), "Miles\n")
        again = loop_again()
        if not again:
            break
