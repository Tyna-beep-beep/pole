skola = ["učení", "knihy", "židle", "učitel", "lavice" , "matematika"]

print(len(skola))

for i in skola:
    print(i)

dalsiSkola = input("Zadej dalsi skolu")
skola.append(dalsiSkola)

skola.remove("židle")

print(skola.sort())

print(skola.reverse())