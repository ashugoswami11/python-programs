#readme  of python program "healthy programmer"
"""
Agenda :-- Create a program which alert programmer after specific period of time by playing a
           .mp3 file, for 3 particular tasks like drinking water, or for doing some physical workout
           and that music won't stop until programmer don't stop it by himself
tasks:--
1. create 3 files in this same folder:--
                    i.for water --  water.mp3
                   ii.for eyes -- eyes.mp3
                   iii.for physical activity -- physical_activity.mp3

2. all these alerts are execute during 9am to 5pm
3. for water --Alert user for "total(3.5) litres of water approx 16-18 glasses of 200 ml" throughout the day
   to stop this music user have to input -drank and press enter --> which generate a log file included at what time user drank water

4. for Eyes --alert will execute in every 30min since starting to ending of the day between 9 to 5
    to stop this music user have to input -eydone and press enter --> which generate a log file included at what time user gave eyes some rest

5. for physical activity --alert will execute in every 45 mins between 9 to 5
    to stop this music user have to input -exdone and press enter --> which generate a log file included at what time user did exercises
    (to make it more challengeful i can also include which exercises user did in this time)


challenges :--
1. maybe any two or three alerts can be executed at the same time causing a clash   __(sleep) can help here
2. handle that clash like first user stop the first music and later second or third

rules :-
1. for the alert music play take help from the pygame module
2. don't change the names of the files
"""