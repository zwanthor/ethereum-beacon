# take command line arguments and spit out random string
import random_str
import verify
import sys

def main(argv):
    execute_command(argv)

def args(argv):
    if len(argv)<2:
        print("Arguments were not supplied")
        sys.exit()
    else:
        flag = argv[1]
        options =[]
        if len(argv)<2:
            for args in argv[2:]:
                options.append(args)
    return flag, options

def execute_command(argv):
    flag, options = args(argv)
    if flag == "v":
        verify.verify_random_num(options[0], options[1])
    if flag == "r":
        random_str.most_recent()
    if flag == "s":
        random_str.specfic_block(options[0])


if __name__=="__main__":
    main(sys.argv)
