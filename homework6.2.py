seconds = int(input("Write your number: "))

if not (0 <= seconds <= 8640000):
    print("The number must be from 0 to 8640000")
    exit()

days = seconds // (24 * 3600)
seconds = seconds % (24 * 3600)

hours = seconds // 3600
seconds = seconds % 3600

minutes = seconds // 60
seconds = seconds % 60

hours = str(hours).zfill(2)
minutes = str(minutes).zfill(2)
seconds = str(seconds).zfill(2)



def days_ua(days):
    if days == 0 or 11 <= days % 100 <= 14:
        return "днів"
    elif days % 10 == 1:
        return "день"
    elif 2 <= days % 10 <= 4:
        return "дні"
    else:
        return "днів"


print(f"{days} {days_ua(days)},{hours}:{minutes}:{seconds}")

