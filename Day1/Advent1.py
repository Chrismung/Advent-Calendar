input_data = "input.txt"

tuplelist = []
with open(input_data, "r") as file:
    for rows in file:
        tuples = rows.split()
        tuples = [int(num) for num in tuples]
        tuplelist.append(tuples)


list_1 = [row[0] for row in tuplelist]
list_2 = [row[1] for row in tuplelist]


list_1sort = sorted(list_1)
list_2sort = sorted(list_2)

dist_list = [abs(list_1sort[i] - list_2sort[i]) for i in range(len(list_1sort))]
sum_dist = sum(dist_list)

similar_score = 0
for a in list_1sort:
    similar_score += a * list_2sort.count(a)
    
print(sum_dist)
print(similar_score)