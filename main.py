from matplotlib import pyplot as plt

list1 = []
list2 = []

color = 0
t = input("what Mode:")
if t == "normal":
    f = 1
elif t == "compare":
    f = int(input("how many times copare: "))
else:
    f = 0

for i in range(f):
    color += 1
    list1 = []
    list2 = []
    a = int(input("what number: "))
    b = a

    while b != 1:
        list1.append(b)
        if (b % 2) == 0:
            b = b / 2
        else:
            b = b * 3
            b += 1
    for i in range(len(list1)):
        list2.append(i)
    plt.plot(list2, list1)
    if color == 1:
        print("Blue")
    if color == 2:
        print("orange")
    if color == 3:
        print("Green")
    if color == 4:
        print("Red")
    if color == 5:
        print("Purple")
    if color == 6:
        print("Brown")
    if color == 7:
        print("Pink")
    if color == 8:
        print("Gray")
    if color == 9:
        print("Olive Green")
    if color == 10:
        print("light blue")
    if color == 11:
        print("Blue")
    if color == 12:
        print("orange")
    if color == 13:
        print("Green")
    if color == 14:
        print("Red")
    if color == 15:
        print("Purple")
    if color == 16:
        print("Brown")
    if color == 17:
        print("Pink")
    if color == 18:
        print("Gray")
    if color == 19:
        print("Olive Green")
    if color == 20:
        print("light blue")
plt.show()
