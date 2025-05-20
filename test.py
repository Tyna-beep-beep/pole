staty = ["Česko", "Čína", "USA"]
velikost = len(staty)
print(velikost)
for i in range(velikost):
    print(staty[i])
if "Česko" in staty:
    print("Je, vidím Česko.")
else:
    print("Česko nikde.")