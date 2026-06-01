HISTORY_FILE = "history.txt"

def show_history():
    with open(HISTORY_FILE, "r") as file:
        lines = file.readlines()
    if len(lines) == 0:
        print("no history found")
    else:
        for line in reversed(lines):
           print(line.strip())
     
    
def clear_history():
    with open(HISTORY_FILE, 'w') as file:
        file.close()
    print("history has been deleted")
    
def save_to_history(equation, result):
    with open()
            