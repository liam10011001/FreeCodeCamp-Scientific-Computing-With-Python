def changeFormat(time, twelveTotwentyfour=True):
    if twelveTotwentyfour:
        (tmp, meridiem) = time.split()
        (hour, minute) = tmp.split(":")
        if meridiem == "PM":
            hour = str(int(hour) + 12)
        return (hour + ":" + minute)
    else:
        (hour, minute) = time.split(":")
        if len(minute) < 2:
            minute = "0" + minute
        meridiem = "AM"
        if int(hour) >= 12 and int(hour) < 24:
            meridiem = "PM"
        if int(hour) > 12:
            hour = str(int(hour) - 12)
        return (hour + ":" + minute + " " + meridiem)

def findDay(start, duration):
    days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    tmp = start[0].upper() + start[1:].lower()
    index = (days.index(tmp) + duration) % 7
    return days[index]
    
def add_time(start, duration, day_of_week=False):
    tmp = changeFormat(start)
    (startH, startM) = [int(x) for x in tmp.split(":")]
    (dH, dM) = [int(x) for x in duration.split(":")]
    
    day = int(dH/24)
    endM = (startM + dM) % 60
    tmpH = dH - (day*24)
    endH = startH + tmpH + int((startM + dM) / 60)
    if endH == 24:
        day += 1
    elif endH > 24:
        day += int(endH / 24)
        endH = endH % 24
    transformedTime = str(endH) + ":" + str(endM)

    new_time = changeFormat(transformedTime, False)
    if day_of_week:
        new_time = new_time + ", " + findDay(day_of_week, day)
        
    if day == 1:
        new_time += " (next day)"
    elif day > 1:
        new_time = new_time + " (" + str(day) + " days later)"
    return new_time

if __name__=="__main__":
    print(add_time("3:00 PM", "3:10"))
    print(add_time("11:30 AM", "2:32", "Monday"))
    print(add_time("11:43 AM", "00:20"))
    print(add_time("10:10 PM", "3:30"))
    print(add_time("11:43 PM", "24:20", "tueSday"))
    print(add_time("6:30 PM", "205:12"))
