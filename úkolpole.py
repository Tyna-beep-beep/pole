cislo=[1,2,3,2]
hodnota= int(input("zadejte cislo"))
for i in range(4):
    if hodnota==cislo[i]:
        print(f"cislo je v poli",i)
    else:
        print("cislov poli není")
