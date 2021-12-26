fyl = open('/home/moit/Desktop/example.txt','r')
fylContent = fyl.read()
print('The contents are:\n\n'+ str(fylContent))
fylList =  fylContent.split()

for x in fylList:
    if not x.isalnum():
        newx=''
        for element in x:
            if element.isalnum():
                newx+=element
        x=newx

    if x=='ADJECTIVE':
        adjective=input('Enter an adjective:\n')
        fylContent = fylContent.replace('ADJECTIVE',adjective,1)  
    elif x=='NOUN':
        noun=input('Enter a noun:\n')
        fylContent = fylContent.replace('NOUN',noun,1)
    elif x=='VERB':
        verb=input('Enter a verb:\n')
        fylContent = fylContent.replace('VERB',verb,1)
    elif x=='ADVERB':
        adverb=input('Enter an adverb:\n')
        fylContent = fylContent.replace('ADVERB',adverb,1)

print(fylContent)
fyl.close()

newfyl = open('/home/moit/Desktop/new.txt', 'w')
newfyl.write(fylContent)