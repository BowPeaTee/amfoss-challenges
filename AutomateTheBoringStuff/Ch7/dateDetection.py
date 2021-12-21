# find valid dates using re

import re

dateRegex= re.compile(r'''(
    (\d{2})     #day
    /
    (\d{2})     #month
    /
    (\d{4})     #year
    )''', re.VERBOSE)

text=input()
matches=[]

for dates in dateRegex.findall(text):
    day=dates[1]
    month=dates[2]
    year=dates[3]
    date='/'.join([day,month,year])
    y=int(year)
    if month in ['01','03','05','07','08','10','12']:
        if int(day)<=31:
            matches.append(date)
    elif month in ['04','06','09','11']:
        if int(day)<31:
            matches.append(date)
    elif (y%4==0 and y%100!=0) or y%400==0:
        if int(day)<=29:
            matches.append(date)
    else:
        if month=='02' and int(day)<=28:
            matches.append(date)

for match in matches:
    print(match)
