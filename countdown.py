# countdown program
import time

timer = int(input("Set countdown ( seconds ): "))

for x in range(timer, 0, -1):
    seconds = x % 60
    minutes = int( x / 60 ) % 60
    hours = int( x / 3600 )
    print(f"{hours:02}:{minutes:02}:{seconds:02}", end="\r")
    time.sleep(1)

print("DONEEEEEEEEEEEE!!!!!!!!!!!")
