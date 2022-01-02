#! python3
# stopwatch.py - A simple stopwatch program.

import time

# Display the program's instructions.
print("Press ENTER to begin. Afterward, press ENTER to 'click' the stopwatch")
input()
print("Started")
startTime = time.time()
lastTime = startTime
lapNum = 1

# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print(f"Lap #{lapNum}: {totalTime} ({lapTime})")
        lapNum += 1
        lastTime = time.time() # reset the last lap time.
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying
    print("\nDone.")