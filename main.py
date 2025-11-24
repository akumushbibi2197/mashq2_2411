#1-misol
zar = random.randint(1, 6)
print("Zar natijasi:", zar)

#2-misol
son = random.randint(1000, 9999)
print("Tasodifiy 4 xonali son:", son)

#3-misol
items = ["olma", "banan", "gilos", "shaftoli", "nok"]
tanlangan = random.sample(items, 2)
print("Tanlangan elementlar:", tanlangan)

#4-misol
num = random.randint(0, 100)
print("Son:", num)

if num % 2 == 0:
    print("Bu juft son.")
else:
    print("Bu toq son.")

#5-misol
import string

satr = "".join(random.choice(string.ascii_lowercase) for _ in range(10))
print("Tasodifiy satr:", satr)

#6-misol
num = random.randint(1, 100)
print("Son:", num)

if num > 50:
    print("Katta")
else:
    print("Kichik yoki teng")

#7-misol
natija = random.choice(["heads", "tails"])
print("Tanga natijasi:", natija)

#8-misol
num = random.randint(1, 20)
print("Son:", num)

if num % 3 == 0:
    print("Bu son 3 ga bo‘linadi.")
else:
    print("Bu son 3 ga bo‘linmaydi.")

#9-misol
colors = ["qizil", "yashil", "ko'k", "sariq", "oq"]

tanlangan = random.choice(colors)
colors.remove(tanlangan)

print("Tanlangan element:", tanlangan)
print("Yangi ro‘yxat:", colors)

#10-misol
num = random.randint(1, 1000)
print("Son:", num)
print("Kvadrati:", num ** 2)
