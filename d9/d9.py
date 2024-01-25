from itertools import permutations

with open("input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

city_set = set()
city_dict = {}

for line in data:
    parts = line.split()
    city_set.add(parts[0])
    city_set.add(parts[2])
    city_dict[(parts[0], parts[2])] = parts[4]
    city_dict[(parts[2], parts[0])] = parts[4]

dist_list = []
for trip in list(permutations(city_set)):
    sum_dist = 0
    for i, j in zip(trip, trip[1:]):
        sum_dist += int(city_dict[(i,j)])
    dist_list.append(sum_dist)
    
print(f"R1: {min(dist_list)}")
print(f"R2: {max(dist_list)}")