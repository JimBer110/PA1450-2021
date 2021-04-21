from datetime import timedelta, date

x= int(input('\nDate no. ONE\nYEAR: '))
y= int(input('MONTH: '))
z= int(input('DAY: '))

a= int(input('\nDate no. TWO\nYEAR: '))
b= int(input('MONTH: '))
c= int(input('DAY: '))
print('\n')

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

start_dt = date(x, y, z)
end_dt = date(a, b, c)
for dt in daterange(start_dt, end_dt):
    print(dt.strftime("%Y-%m-%d"))