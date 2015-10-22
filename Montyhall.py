import random

switchedcorrect = 0
stayedcorrect = 0
doors = [1, 2, 3]
incorrectdoor = 0
newguess = 0

timestosimulate = int(raw_input("How many times do you want to simulate the problem for both switching and not switching choices? "))

# Switches it's answer every time #
for i in range(timestosimulate):
    print "-----------------------------------"
    correct = random.choice(doors)
    guess = random.choice(doors)
    print "The prize is behind door #" + str(correct)
    print "The contestant initially guesses door #" + str(guess)
    for i in doors:
        if i != correct and i != guess:
            incorrectdoor = i
    for i in doors:
        if i != guess and i != incorrectdoor:
            newguess = i
    print "The host reveals a goat behind door #" + str(incorrectdoor)
    print "The contestant switches their choice to door #" + str(newguess)
    if newguess == correct:
        switchedcorrect += 1
        print "The contestant won a new car!"
    else:
        print "The contestant lost!"

# Sticks with it's first answer #
for i in range(timestosimulate):
    print "-----------------------------------"
    correct = random.choice(doors)
    guess = random.choice(doors)
    print "The prize is behind door #" + str(correct)
    if correct == guess:
        stayedcorrect += 1
        print "The contestant guessed " + str(guess) + " correctly!"
    else:
        print "The contestant guessed door #" + str(guess) + " and lost!"

timestosimulate += 0.0

print "Switching their choice got the contestant the correct answer " + str(switchedcorrect) + " out of " + str(int(timestosimulate)) + " times! (" + str(switchedcorrect/timestosimulate*100) + "%)"
print "Staying with their initial choice got the contestant the correct answer " + str(stayedcorrect) + " out of " + str(int(timestosimulate)) + " times! (" + str(stayedcorrect/timestosimulate*100) + "%)"
