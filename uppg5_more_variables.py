"""  
Skapa en variabel för ditt namn.
Skapa en variabel för din ålder.
Skriv ut ditt namn med hjälp av variabeln.

Skapa en variabel och låt användaren skriva in sitt namn med hjälp av input.
Skapa en variabel och låt användaren skriva in sin ålder med hjälp av input.

Skriv ut en mening som använder sig av alla 4 variabler. Åldern ska adderas ihop.

Exempel på utskrift, det inom () ska ändras om variablerna ändras:
Välkommen till mitt program (Oskar). Du och (Hampus) är (53) år tillsammans.

"""

name1=("Gabriel")
year1=("17")
name2= input("What is your name. ")
year2=int(input("How old are you. "))
age= year2-17
age1=year2+17
print(f"Hello {name2}. You are {year2} years old and are {age} years older then {name1} who is {year1} years old. and together you are {age1} years old")