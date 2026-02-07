lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

result = [threes for threes in lst if threes < 30 and threes % 3 == 0]

print(result)
