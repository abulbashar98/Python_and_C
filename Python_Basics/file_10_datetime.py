import datetime

date = datetime.date(2026, 6, 16)
today = datetime.datetime.today()


time = datetime.time(9, 45, 30)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %d-%m-%y")
# print(now)

target_datetime = datetime.datetime(2024, 4, 4, 11,  59, 59)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target datetime has passed")

else:
    print("Target datetime has not passed")






