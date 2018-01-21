sundays=0
day=2
leap=0
for year in range(1901, 2001):
    leap+=1
    day+=31  #Jan
    if not(day%7):
        sundays+=1
    day%=7
    day+=28  #Feb
    if leap==4:
        leap=0
        day+=1
    if not(day%7):
        sundays+=1
    day%=7
    day+=31  #Mar
    if not(day%7):
        sundays+=1
    day%=7
    day+=30  #Apr
    if not(day%7):
        sundays+=1
    day%=7
    day+=31
    if not(day%7):
        sundays+=1
    day%=7
    day+=30
    if not(day%7):
        sundays+=1
    day%=7 
    day+=31
    if not(day%7):
        sundays+=1
    day%=7
    day+=31
    if not(day%7):
        sundays+=1
    day%=7  
    day+=30
    if not(day%7):
        sundays+=1
    day%=7
    day+=31
    if not(day%7):
        sundays+=1
    day%=7  
    day+=30
    if not(day%7):
        sundays+=1
    day%=7
    day+=31
    if not(day%7):
        sundays+=1
    day%=7
print(sundays)
