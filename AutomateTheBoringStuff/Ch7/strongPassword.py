def strongPassCheck(pasw):
    import re

    if len(pasw)<8:
        print('Weak Password. Size matters.')
        return

    checkone = re.compile(r'[0-9]+')
    if checkone.search(pasw)==None:
        print('Weak Password. Add a digit.')
        return
    
    checktwo = re.compile(r'[a-z]+')
    if checktwo.search(pasw)==None:
        print('Weak Password. Add a lowercase character.')
        return
    
    checkthree = re.compile(r'[A-Z]+')
    if checkthree.search(pasw)==None:
        print('Weak Password. Add an uppercase character.')
        return
    
    else:
        print('Strong Password.')
        return

passkey=input('Enter password.')
strongPassCheck(passkey)