import time

time=int(input("enter the time in seconds: "))
for x in range (time, 0, -1):
    seconds= x % 60
    minutes= int(x/60) % 60
    hours = int(x / 3600)
    days = int(x / 86400)
    print(f"{days}:{hours}:{minutes}:{seconds}")


print("Times up!")