command = ""
started = False





command = input(">please enter your command(start/stop/quit/help/....) ").lower()


if command == "start":
    if started == True:
        print("Your car has started")
    else:
        # started = True
        print("You started")
elif command == "stop":
    if started == False: 
        print("Car has stopped")
    else:
        # started = False
        print("You stopped")
elif command == "quit":
    print("break")
elif command == "help":
    print("""
Start--Car start
Stop--Car stop
Quit--Game over      
    """)
else:
    print("I don't understand.")