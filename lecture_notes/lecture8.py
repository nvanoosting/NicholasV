list1 = list(range(0,11))

print(
    list1[:5],
    list1[::2],
    list1[::-1]
)

a = [[2, 4, 9], [4, 1, 2], [6, 10, 19]]
b = [[8, 20, 10], [10, 8, 6], [12, 9, 0]]
c = [14, 16, 18]

nested_list = [a, b, c]
print(nested_list)

print(nested_list[2][1])

stars_data = {
    "name" : ["Sirius", "Vega", "Altair"],
    "magnitude" : [-1.46, 0.03, 0.77],
    "distance_ly": [8.6, 25.0, 16.7],
    "constellation" : ["Canis Major", "Lyra", "Aquila"]
    }


for names in stars_data["name"]:
    print(names)

def star_distance_comparison(stars_data):
    count = 0
    for distance in stars_data["distance_ly"]:
        if distance > 20:
            count += 1
    return count