import random
import sys

#secret_int = random.randint(1,100)
secret_int = 42

print "Hello Meatbag, guess my secret number, you have three tries!"
print "Failure results in protein processing"

def process_user_guess(guess_count):
    print "Provide your {} guess:".format(guess_count)
    value = sys.stdin.readline()
    value = value.strip()
    guess_int = int(value)

    if guess_int == secret_int:
        print "Good job, Meatbag!  You get to live!"
        return True

    if guess_int > secret_int:
        print "Too high, Meatbag!"
    else:
        print "Too low, Meatbag!"
    return False

guessed = process_user_guess("first")
if not guessed:
    process_user_guess("second")
if not guessed:
    process_user_guess("final")
if not guessed:
    print "Enjoy your processing Meatbag! My secret number was {}".format(secret_int)
