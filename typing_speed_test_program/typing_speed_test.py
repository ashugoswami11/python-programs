#agenda :-- to create a program which give a sentence to the user and check how and accurately the user type that sentence

import time

script = "python is a fun programming language to learn"

print("welcome to the python typing speed test")
print("\ntype the following sentence as fast as possible")

print("sentence:--",script)

print("press enter to begin")
input()

start_time = time.time()
typed_sentence = input("start typing now!! and press enter when done\n")
end_time = time.time()

time_taken = round((end_time - start_time),2) #round(time,2"precision after decimal") func is used to return the floating number which is rounded version of the specified number

typed_script = typed_sentence.split()
original_script = script.split()

#checking the correct words
correct_words = 0
total_words = 0
for o,t in zip(original_script,typed_script): #it combines the two list into one list of tuples and join their corresponding values
    total_words += 1
    if o.lower() == t.lower():
        correct_words += 1

#calculating speed in words per minute
speed = ( len(typed_script) / time_taken)*60
speed = round(speed,2)

print("*******result********")
print("time taken in typing =",time_taken," seconds")
print("speed =",speed,"words per minute")
print(f"total correct words {correct_words} out of {total_words}")

if correct_words == total_words:
    print("you typed all words correctly")
else:
    print("you typed some wrong words need to improve your accuracy")
