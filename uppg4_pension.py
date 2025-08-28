"""  
Gör ett program som frågar användaren efter namn och ålder.
Programmet ska sedan skriva ut enligt nedan.
Räkna med att man går i pension vid 67 års ålder.

Exempel på utskrift, det inom () ska ändras om variablerna ändras:
Hej och välkommen till mitt program (Hampus). Du har (39) år kvar till pension.
"""

username= input("What is your name. ")
Year= int(input("How old are you. "))
Age= 67- Year  
print(f"hello {username}. You can take your pension in {Age} years. ")
