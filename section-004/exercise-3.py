#Write a program that will mark a spot with an X.

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")


x = int(position[0])
y = int(position[1])

selectedRow = map[y - 1]
selectedRow[x - 1] = 'X'

print(f"{row1}\n{row2}\n{row3}")