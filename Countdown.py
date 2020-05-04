import time
def countdown(t):
    while t > 0:
        print(t)
        t -= 1
        time.sleep(10)
    print("DIE MATAFAKA! *puts mentos in coke*")

print("How many seconds to count down? Enter an integer:")
seconds = input()
while not seconds.isdigit():
    print("That wasn't an integer! Enter an integer:")
    seconds = input()
seconds = int(seconds)
countdown(seconds)
