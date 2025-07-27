import datetime

now = datetime.datetime.now()
right_now = now.strftime("%H:%M %p")

def logger(str_name):
    if str_name == "drank":
        with open("drink_log.txt","a") as f:
            f.write(f"i drank water at: [ {right_now} ]\n" )
            f.close()

    elif str_name == "eydone":
        with open("eye_log.txt","a") as f:
            f.write(f"i gave rest to my eyes at: [ {right_now} ]\n" )
            f.close()

    elif str_name == "exdone":
        with open("exercise_log.txt","a") as f:
            f.write(f"i did exercises at: [ {right_now} ]\n" )
            f.close()

