def printTable(tableData):
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        colWidths[i]=len(max(tableData[i],key=len))
    i,j=0,0
    try:    
        while True:
            data=tableData[j][i]
            print(data.rjust(colWidths[j]), end=' ')
            j+=1
            if j==len(tableData):
                i+=1
                j=0
                print()
    except IndexError:
        return

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)
