The monty hall problem is as follows:


Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?

This program simulates the situation X amount of times. It simulates a situation where the contestant doesn't switch doors, and one where they do. At the end of the program it displays percentage results, and by running this program one can see how switching choices greatly increases their odds of winning.




Here is the program being used (final results are at the bottom):


How many times do you want to simulate the problem for both switching and not switching choices? 3
-----------------------------------
The prize is behind door #2
The contestant initially guesses door #3
The host reveals a goat behind door #1
The contestant switches their choice to door #2
The contestant won a new car!
-----------------------------------
The prize is behind door #3
The contestant initially guesses door #1
The host reveals a goat behind door #2
The contestant switches their choice to door #3
The contestant won a new car!
-----------------------------------
The prize is behind door #3
The contestant initially guesses door #3
The host reveals a goat behind door #2
The contestant switches their choice to door #1
The contestant lost!
-----------------------------------
The prize is behind door #3
The contestant guessed door #1 and lost!
-----------------------------------
The prize is behind door #1
The contestant guessed door #2 and lost!
-----------------------------------
The prize is behind door #3
The contestant guessed 3 correctly!
Switching their choice got the contestant the correct answer 2 out of 3 times! (66.6666666667%)
Staying with their initial choice got the contestant the correct answer 1 out of 3 times! (33.3333333333%)




The mathematical reason for this is quite simple. When the contestant initially guesses, they have a 1/3 (33.333%) chance of guessing correctly. That part should be obvious. When they switch their answer they have a 2/3 (66.666%) chance of guessing correctly. This is because the only way you could get an incorrect answer after you switch would be if you initially chose the correct answer (which you have a 33.333% chance of doing) -- so if you switch your answer, you only have a 33.333% chance of getting it wrong, and since there are only two possible outcomes you have a 66.666% (2/3) chance of getting it right after switching.
