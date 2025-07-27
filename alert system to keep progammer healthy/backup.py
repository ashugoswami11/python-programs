#-- working on the water alert

from datetime import timedelta, datetime, time
from time import sleep

from pygame import mixer
mixer.init()
mixer.music.set_volume(0.3)

from log_retrive import logger

# now = datetime.now()
# formatted_now = now.strftime("%H:%M") #current time

from time_list_generator import water_alert

from time_list_generator import eyes_alert

from time_list_generator import exercise_alert


task_queue = []
while True:

    now = datetime.now()
    formatted_now = now.strftime("%H:%M")  # current time

    #handling the clash of two alerts using list as a queue
    if formatted_now in water_alert() and "water" not in task_queue:
        task_queue.append("water")

    if formatted_now in eyes_alert() and "eyes" not in task_queue:
        task_queue.append("eyes")

    if formatted_now in exercise_alert() and "exercise" not in task_queue:
        task_queue.append("exercise")

    if task_queue:
        task = task_queue.pop(0)
        if task == "water":
            mixer.music.load("water.mp3")
            while True:
                mixer.music.play(-1)
                print("please write 'drank' to stop music")
                w_input = input().strip().lower()
                if w_input == "drank":
                    print("thank you for water")
                    logger("drank")
                    mixer.music.stop()
                    break
            sleep(60)


        elif task == "eyes":
            mixer.music.load("eyes.mp3")
            while True:
                mixer.music.play(-1)
                print("please write 'eydone' to stop music")
                e_input = input().strip().lower()
                if e_input == "eydone":
                    print("thank you for eyes")
                    logger("eydone")
                    mixer.music.stop()
                    break
            sleep(60)


        elif task == "exercise":
            mixer.music.load("exercise.mp3")
            while True:
                mixer.music.play(-1)
                print("please write 'exdone' to stop music")
                ex_input = input().strip().lower()
                if ex_input == "exdone":
                    print("thank you for exercise")
                    logger("exdone")
                    mixer.music.stop()
                    break
            sleep(60)

    sleep(5)