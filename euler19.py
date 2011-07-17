from datetime import date

def euler19():
    count=0
    for year in range(1901, 2001):
        for month in range(1,13):
            if date(year, month, 1).weekday() == 6: count+=1

    return count

print(euler19())
            
