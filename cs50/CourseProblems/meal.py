def main():
    time_in_hours = convert("time")
    if time_in_hours < 12:
        print('breakfast')
    elif time_in_hours < 18 :
        print('lunch')
    elif time_in_hours > 18 and time_in_hours < 24 :
        print('dinner')
    elif time_in_hours > 24 :
        print('Thats not a time')
    else:
        print('Thanks')

def convert(time):
    time = input('What is the time?: ')
    hours, minutes = time.split(':')
    hours = float(hours)
    minutes = float(minutes)/60
    return hours + minutes

if __name__ == "__main__":
    main()