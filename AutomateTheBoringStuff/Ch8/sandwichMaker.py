import pyinputplus as pyip
cost=0
order=[]

bread = pyip.inputMenu(['wheat','white','sourdough'])
order.append(bread)

protein = pyip.inputMenu(['chicken','turkey','ham','tofu'])
order.append(protein)

chyees = pyip.inputYesNo(prompt='Do you want cheese?')
if chyees=='yes':
    cheese=pyip.inputMenu(['cheddar','Swiss','mozzarella'])
    order.append(cheese)

for i in ['mayo','mustard','lettuce','tomato']:
    j=i
    i=pyip.inputYesNo(prompt='Do you want %s?' % i)
    if i=='yes':
        order.append(j)

count=pyip.inputInt(prompt='How many sandwiches do you want?',min=1)

prices={'wheat':15,'white':10,'sourdough':20,'chicken':30,'ham':20,'turkey':25,'tofu':35,'cheddar':20,'Swiss':25,'mozzarella':30,'mayo':15,'mustard':15,'lettuce':25,'tomato':30}

for i in order:
    cost+=prices[i]
print('Your total cost is %s' % (cost*count))