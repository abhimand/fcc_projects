def add_time(start, duration, day=None):
    ### set up
    week = {'Sunday': 0, 'Monday': 1, 'Tuesday': 2,
        'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6} 
    def findDay(value): 
        value %= 7
        for day, v in week.items(): 
            if v == value: 
                return day
    ### split strings into readable format
    startDetails= start.split()
    startNums = startDetails[0].split(':')
    durationNums = duration.split(':')
    meridiem = startDetails[1]
    ### operate on our numbers
    newHour = int(startNums[0]) + int(durationNums[0])
    newMins = int(startNums[1]) + int(durationNums[1])
    meriCounter = newHour // 12
    ### fix hour
    if newHour > 12: 
        newHour %= 12
    ### fix minutes
    if newMins > 60: 
        newMins %= 60
        newHour += 1
        if newHour >= 12: 
            meriCounter += 1
    ### fix meridiem
    n = meriCounter
    initialMeri = meridiem
    while meriCounter > 0:
        if meridiem == 'AM': 
            meridiem = 'PM'
        else: 
            meridiem = 'AM'
        meriCounter -= 1
    ### fix meridiem
    newDay = ''
    if day is not None:  
        val = week.get(day.title())
        newVal = val + round(n/2)
        newDay += ', ' + findDay(newVal)
    
    if initialMeri == 'PM' and meridiem == 'AM' and n == 1:
        meridiem += newDay + ' (next day)' 
    elif initialMeri == 'AM' and meridiem == 'AM': 
        if n == 2:  
            meridiem += newDay + ' (next day)'
        elif n > 2: 
            meridiem += newDay + ' (' + str(n - 1) + ' days later)'
        
    elif initialMeri == 'PM' and meridiem == 'AM' and n > 1:
        meridiem += newDay + ' (' + str(round(n/2)) + ' days later)'
    else: 
        meridiem += newDay


    ### fix strings
    if newMins < 10: 
        newMins = '0' + str(newMins)

    
    newTime = str(newHour) + ':' + str(newMins) + ' ' + meridiem
    return newTime



            





    