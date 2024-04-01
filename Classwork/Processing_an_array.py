# 03/12/2024
# Amanda M
# Processing the Contents of an Array (I don't understand Arrays when reading the PowerPoints)
# (So I'm just trying them out)

WEIGHT = ["113", "120", "124", "135", "140", "150", "160", "170", "182", "190", "220", "HW"]
# size = len(WEIGHT)        Just so I can remember how to find the amount of stuff in ^this^ "array".
for idx in WEIGHT:           
        print(idx)
choice = input("Please choose your weight class from the list: ")
if choice != [WEIGHT]:
    choice
else:
    print(f"You are in {choice} weight class.")
