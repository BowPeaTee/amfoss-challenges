def Regexstrip(string, todel=' '):
    import re
    stringRegex = re.compile(r'^'+todel)
    stringRegex.sub('',string)
    stringRegex = re.compile(todel+r'$')
    stringRegex.sub('',string)
    print(string)
Regexstrip(' amany  ')