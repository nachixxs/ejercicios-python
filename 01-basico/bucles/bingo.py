def bingo():
    
    for i in range (1, 31):
        if i % 5 == 0:
            print("Bingo!")
        else:
            print(i)
bingo()