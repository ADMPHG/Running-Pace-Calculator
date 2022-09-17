# splits user input into whole numbers and remainder if it contains a period or colon
# used by take_distance() and take_time()
def handle_remainder(userInput):
    if userInput.find('.') != -1:
        decomp = userInput.split('.')
        part1 = decomp[0]
        part2 = decomp[1]
        return part1, part2

    elif userInput.find(':') != -1:
        decomp = userInput.split(':')
        part1 = decomp[0]
        part2 = decomp[1]
        return part1, part2
    
    else:
        return userInput, 0

# takes distance from user, convert decomposed str into ints
# if anything but ints are entered, user is prompted to input a valid number
# BUG currently multiple periods/colons are accepted which needs to be addressed
def take_distance():
    while True:
        try:
            distance = input('Enter the distance you are running (in km): ')
            kilometers, meters = handle_remainder(distance)
            kilometers = int(kilometers)
            meters = int(meters)
            break
        except ValueError:
            print('Enter a valid number')

    return kilometers, meters

# takes time from user, convert decomposed str into ints
# if anything but ints are entered, user is prompted to input a valid number
# BUG currently multiple periods/colons are accepted which needs to be addressed
def take_time():
    while True:
        try:
            time = input('Enter the time you would like to finish (in mins): ')
            minutes, seconds = handle_remainder(time)
            minutes = int(minutes)
            seconds = int(seconds)
            break
        except ValueError:
            print('Enter a valid number')
    return minutes, seconds

# calculates pace from user supplied values - main concern is conversion from 60ths to 100ths and back for seconds
# may want to create separate function to handle different print statement cases
def calc_pace(kilometers, meters, minutes, seconds):
    if seconds != 0 or meters != 0:
        pace = ((minutes + 0.01 * (seconds * (1 + (2 / 3)))) / (kilometers + 0.1 * (meters))) # recombine minutes/seconds and kilometers/meters
        paceSec = round(((pace % 1) * 60), 2)
        paceMins = int(pace - (pace % 1))
        print(f'Pace required to run {kilometers}.{meters} kilometers in {minutes} minutes and {seconds} seconds is {paceMins}:{paceSec} mins/km')
    else:
        pace = minutes / kilometers
        pace = (pace - pace % 1) + (pace % 1) * 0.6
        print(f'Pace required to run {kilometers} kilometers in {minutes} minutes is {pace} mins/km')

def main():
    kilometers, meters = take_distance()
    minutes, seconds = take_time()
    calc_pace(kilometers, meters, minutes, seconds)

main()
