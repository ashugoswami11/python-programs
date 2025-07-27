from datetime import timedelta, datetime

now = datetime.now()
formatted_now = now.strftime("%H:%M")

def water_alert():

    day_start = "9:00"
    day_end = "17:00"
    start = datetime.strptime(day_start, "%H:%M")
    end = datetime.strptime(day_end, "%H:%M")

    step = timedelta(minutes=28)

    time_list_water = []
    time_start = start #just taking 9:00 am into different variable so that by accident i won't change the original
    while time_start <= end:
        time_list_water.append(time_start.strftime("%H:%M"))
        time_start = time_start + step

    return time_list_water #list of times from 9 to 5 in which user have to be alert for drinking water


def eyes_alert():

    day_start = "9:00"
    day_end = "17:00"
    start = datetime.strptime(day_start, "%H:%M")
    end = datetime.strptime(day_end, "%H:%M")

    step = timedelta(minutes=30)

    time_list_eye = []
    time_start = start #just taking 9:00 am into different variable so that by accident i won't change the original
    while time_start <= end:
        time_list_eye.append(time_start.strftime("%H:%M"))
        time_start = time_start + step

    return time_list_eye

def exercise_alert():

    day_start = "9:00"
    day_end = "17:00"
    start = datetime.strptime(day_start, "%H:%M")
    end = datetime.strptime(day_end, "%H:%M")

    step = timedelta(minutes=45)

    time_list_exercise = []
    time_start = start #just taking 9:00 am into different variable so that by accident i won't change the original
    while time_start <= end:
        time_list_exercise.append(time_start.strftime("%H:%M"))
        time_start = time_start + step

    return time_list_exercise