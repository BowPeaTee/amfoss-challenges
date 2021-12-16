def isValidChessBoard(d):
    val=list(d.values())
    key=list(d.keys())

    """positions=[]
    for i in range(1,9):
        for j in list('abcdefgh'):
            positions.append(str(i)+j)"""
    positions=['1a', '1b', '1c', '1d', '1e', '1f', '1g', '1h', '2a', '2b', '2c', '2d', '2e', '2f', '2g', '2h', '3a', '3b', '3c', '3d', '3e', '3f', '3g', '3h', '4a', '4b', '4c', '4d', '4e', '4f', '4g', '4h', '5a', '5b', '5c', '5d', '5e', '5f', '5g', '5h', '6a', '6b', '6c', '6d', '6e', '6f', '6g', '6h', '7a', '7b', '7c', '7d', '7e', '7f', '7g', '7h', '8a', '8b', '8c', '8d', '8e', '8f', '8g', '8h']
    for i in range(len(d)):
        if key[i] not in positions:
            print('All pieces not in valid space')
            return False
        positions.remove(key[i])

    if val.count('bking')!=1:
        print('Black does not have exactly one king!')
        return False
    if val.count('wking')!=1:
        print('White does not have exactly one king!')
        return False

    wcount,bcount=0,0
    for i in range(len(d)):
        if val[i][0]=='w':
            wcount+=1
        elif val[i][0]=='b':
            bcount+=1
    if wcount>16:
        print('White has too many pieces')
        return False
    elif bcount>16:
        print('Black has too many pieces')
        return False
    if val.count('bpawn')>8:
        print('Black has too many pawns')
        return False
    if val.count('wpawn')>8:
        print('White has too many pawns')
        return False
    return True
dic={'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(dic))