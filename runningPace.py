def take_distance():
    while True:
        try:
            distance = float(input('Enter the distance you are running (in km): '))
            break
        except ValueError:
            print('Enter a valid number')

    return distance

def take_time():
    while True:
        try:
            time = float(input('Enter the time you would like to finish (in mins): '))
            time = (time - (time % 1)) + (time % 1) * (1 + (2 / 3))
            break
        except ValueError:
            print('Enter a valid number')
    return time

def calc_pace(distance, time):
    pace = time / distance
    if pace % 1 != 0:
        pace = (pace - (pace % 1)) + (pace % 1) * 0.6
        seconds = (time % 1) * 60
        minutes = time - (time % 1)
        print(f'Pace required to run {int(distance)} kilometers in {int(minutes)} minutes and {int(seconds)} seconds is {pace} mins/km')
    else:
        print(f'Pace required to run {int(distance)} kilometers in {int(time)} minutes is {pace} mins/km')

def main():
    distance = take_distance()
    time = take_time()
    calc_pace(distance, time)

main()