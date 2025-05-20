#toto je pole
#pole slouží k ukládání více hodnot najednou (vzniklo proto, abychom nemuseli vytvářet spousty proměnných)
#pole je vždy indexované od 0 (index je pozice na kterém se konkrétní hodnota nachází)
cisla = [5,2,8] #takto se vytváří pole s čísli(nedávají se zde uvozovky okolo hodnot, aby s nimi šli provádět matematické operace)
jmena = ["Pave","Tomáš", "Eva"] #takto se vytváří pole se stringovými hodnotami(vše do uvozovek)
jeHezky = [False,True,False] #pole v sobě může mít i True/False hodnoty
 
#pomocí .append() se dá hodnota přidat na konec pole
cisla.append(10)
#pro zjištění velikosti pole(to kolik se tam vejde hodnot) se dá použít len()
velikost = len(cisla)
print(velikost)
 
#pro vypsání všech hodnot z pole je nejlepší použít for cyklus
#varianta 1 - obecný for cyklus
for i in range(velikost):
    print(cisla[i])
#varianta 2 - speciální cyklus pro procházení prvků v poli
#items je proměnná, do které se při každém průchodu uloží jedna hodnota z pole cisla, printem ji pak už jen při každém průchodu vypisuji
for items in cisla:
    print(cisla)
 
#ověření, zda se něco nachází v poli
#například pokud je v poli cisla číslo 2
#varianta 1 - projdu pole cisla a každou hodnotu ověřím pomocí if
containsNumberTwo = False
for number in cisla:
    if number==2:
        containsNumberTwo=True
print(containsNumberTwo)
 
#varianta 2 - dá se použít speciální if
if 2 in cisla:
    print("číslo 2 se nachází v poli")
else:
    print("číslo 2 se v poli nenachází")
 
#stejně tak to funguje i u stringových polí, jediný rozdíl je v uvozovkách
if "Eva" in jmena:
    print("Eva je v této třídě")
else:
    print("Eva není v této třídě")
 