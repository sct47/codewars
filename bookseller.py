def bookseller(l, m):    
    for first_letter in L:
        first = first_letter[0]

    for letter in M:
        if letter in first:
            print(letter)

L = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
M = ["A", "B", "C", "W"]
print(bookseller(L, M))
