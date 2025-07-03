HISTORY_FILE = "history.txt"

def show_history():
    file = open(HISTORY_FILE, 'r')
    lines = file.readlines()
    if len(lines) == 0:
        print("NOT HISTORY FOUND")
    else:
        for line in reversed(lines):
            print(line.split())

    file.close()
                