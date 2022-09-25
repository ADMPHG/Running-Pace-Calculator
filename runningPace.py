# splits user input into whole numbers and remainder if it contains a period or colon
# used by take_distance() and take_time()
def handle_remainder(userInput):
    if userInput.find('.') != -1:
        decomp = userInput.split('.')
        # limit no. of periods in input to two
        if len(decomp) > 2:
            return ''
        part1 = decomp[0]
        part2 = decomp[1]
        return part1, part2

    elif userInput.find(':') != -1:
        decomp = userInput.split(':')
        # limit no. of colons in input to two
        if len(decomp) > 2:
            return ''
        part1 = decomp[0]
        part2 = decomp[1]
        return part1, part2
    
    else:
        return userInput, 0

# takes distance from user, convert decomposed str into ints
# if anything but ints are entered, user is prompted to input a valid number
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

# prints the results of the calculation in the appropriate format
# the else case is for when the result of the pace calculation is a whole number
def print_output(kilometers, meters, minutes, seconds, pace, paceSec, paceMins):
    if paceSec != 0:
        print(f'Pace required to run {kilometers}.{meters} kilometers in {minutes} minutes and {seconds} seconds is {paceMins}:{paceSec} mins/km')

    else:
        print(f'Pace required to run {kilometers} kilometers in {minutes} minutes is {int(pace)} mins/km')

# calculates pace from user supplied values - main concern is conversion from 60ths to 100ths and back for seconds
def calc_pace(kilometers, meters, minutes, seconds):
    pace = ((minutes + 0.01 * (seconds * (1 + (2 / 3)))) / (kilometers + 0.1 * (meters))) # recombine minutes/seconds and kilometers/meters, then divide the former by the latter
    paceSec = round(((pace % 1) * 60), 2) # rounds the remainder of the pace calculation to 2 d.p
    paceMins = int(pace - (pace % 1)) # captures the minutes part of the pace calculation and converts to int to remove the '.0' of the float

    print_output(kilometers, meters, minutes, seconds, pace, paceSec, paceMins)


def main():
    kilometers, meters = take_distance()
    minutes, seconds = take_time()
    calc_pace(kilometers, meters, minutes, seconds)

main()
