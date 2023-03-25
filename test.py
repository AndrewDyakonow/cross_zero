list_1 = [0, 6]
list_2 = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

for option in list_2:
    if len(set(option).difference(set(list_1))) == 1:
        print("входит")
    else:
        print(":(")

