import random
a = 15
list = []


for i in range(a):
    list.append(random.random() * 100)

print(list)

maximum = max(list)
minimum = min(list)
total = sum(list)
avg = sum(list) / len(list)

print("The max number: ", maximum,  "\nthe min number: ", minimum, "\nthe sum of numbers: ", total, "\nthe avg: ",
      avg)

    # print(max(list))