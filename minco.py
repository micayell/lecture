alphabet = [
	['A', 'B', 'C'],
    ['A', 'G', 'H'],
    ['H', 'I', 'J'],
    ['K', 'A', 'B'],
    ['A', 'B', 'C']
]

lst=[0]*26

for i in range(5):
    for j in range(3):
        lst[ord(alphabet[i][j])-65] +=1

for i in range(len(lst)):
    if lst[i] >= 1:
        print(chr(i+65), end="")

