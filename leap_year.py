#leap year feb days
year = int(input())
if(year%4==0 and year%100!=0)or (year%400==0):
    print("29 days")
else:
    print("28 days")
