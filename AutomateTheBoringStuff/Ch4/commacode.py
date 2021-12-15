def func(l):
    s=''
    for i in range(len(l)):
        if i==len(l)-1 and len(l)!=1:
            s+='and '
            s+=l[i]
        else:
            s+=l[i]
            if i!=len(l)-1:
                s+=', '
    return s
print('checking 3 lists- original spam, empty list and list with single value:')
spam = ['apples', 'bananas', 'tofu', 'cats']
bacon = []
ham = ['apples']
ans=func(spam)
ansb=func(bacon)
ansc=func(ham)
print(ans,ansb,ansc,sep='\n')