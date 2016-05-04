# purpose is to spit out random string every set amount of time
import random_str
import datetime
import time
import sys

def main(argv):
    timeToSleep = int(time_to_sleep(argv))
    beacon_routine(timeToSleep)

def beacon_routine(timeToSleep):
    while True:
        try:
            print(datetime.datetime.now())
            random_str.most_recent()
            time.sleep(timeToSleep)
        except KeyboardInterrupt:
            print("Exiting Beacon")
            sys.exit()

def time_to_sleep(argv):
    try:
        return argv[1]
    except:
        print("No time was specified")
        sys.exit()

#beacon_routine(timeToSleep)
if __name__=="__main__":
    main(sys.argv)
