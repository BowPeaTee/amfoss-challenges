import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    events=['H','T']
    l=[]
    for i in range(100):
        toss=random.choice(events)
        l.append(toss)
    # Code that checks if there is a streak of 6 heads or tails in a row.
    i=0
    while i<100:
        count=0
        for j in range(1,6):
            try:
                if l[i]==l[i+j]:
                    count+=1
                else:
                    break
            except IndexError:
                break
        if count==5:
            numberOfStreaks+=1
            i+=6
        else:
            i+=1
print(numberOfStreaks)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))