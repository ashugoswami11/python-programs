import random 
 
subjects = [
    "Nehru Chacha",
    "Modi",
    "Trump",
    "Rickshaw Wala From Delhi",
    "Justin Bieber",
]

Action = [
    "Dances",
    "Plays Vollyball",
    "Eating Banana",
    "Declares War",
    "Ride Horse",
]

Places_or_Things = [
    "Inside Parliament",
    "At Gaziabad Railway Station",
    "With Prince Charles",
    "On The Top of Burj Khalifa",
    "In Chinatown",
]

#start the headline Generator Loop
while True:
    sub = random.choice(subjects)
    act = random.choice(Action)
    place = random.choice(Places_or_Things)
    
    headline = f"BREAKING NEWS: {sub} {act} {place}"
    
    print("\n", headline)
    
    repeat = input("\nType yes for repeat or no for exit").strip().lower()
    
    if repeat == "no":
        break
   
print("bye bye")


