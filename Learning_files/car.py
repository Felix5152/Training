print("Welcome to the game! Type help to see list of commands.")
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("The car is already stared!")
        else:
            started = True
            print("The car starded. It's ready to go!")
    elif command == "stop":
        if not started:
            print("The car is already stopped.")
        else:
            started = False
            print("The car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit the game
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that:(")
