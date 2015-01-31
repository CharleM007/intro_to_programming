#For loops

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in numbers:
    print(i*2, i)

for i in range(1,11):
    print(i, i**2)


for i in range(1,11):
    print(i, i**2)

##What IS "i^2"?
# for i in range(1,11):
#     print(i, i**2, float(i^2))

names = ["Bob", "Edgar", "Frank", "Olivia", "Katrina"]
for name in names:
    if name[0] in "AEIOU":
        print(name + " starts with a vowel")