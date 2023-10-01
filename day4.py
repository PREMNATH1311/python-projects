def stonepaperscior():

    import random
    list=["stone","paper","scissor"]
    k=random.choice(list)

    i=input("Enter you value which you want to win: LIke stone,paper,scissor? ")
    if i==k:
        print(k)
        return "It draws, try again"
    if k=="stone" and i=="paper":
        print(k)
        return "you win"
    elif k=="stone" and i=="scissor":
        print(k)
        return "you lost"
    elif k=="paper" and i=="stone":
        print(k)
        return "you lost"
    elif k=="paper" and i=="scissor":
        print(k)
        return "you win"
    elif k=="scissor" and i=="stone":
        print(k)
        return "you won"
    elif k=="scissor" and i=="paper":
        print(k)
        return "you lost"

print(stonepaperscior())