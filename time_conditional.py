from time import localtime, get_clock_info
from unicodedata import decimal

activities = {0.1: 'Sleeping',
              9: 'Commuting',
              17: 'Working',
              18: 'Commuting',
              20: 'Eating',
              22: 'Resting'}

hour = float(f"{localtime().tm_hour}.{localtime().tm_min}")

print('Local hour', localtime().tm_hour)
print('Local minute', localtime().tm_min)
print('Hour', hour)

for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print(activities[activity_time])
        break
    else:
        print('Unknown, AFK or sleeping!')