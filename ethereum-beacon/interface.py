# take command line arguments and spit out random string
import random_str
import verify

def main(argv):
    excute_command(argv)

def args(argv):
    if len(argv)>3:
        print("Arguments were not supplied")
        sys.exit()
    else:
        flag = argv[1]
        options =[]
        for args in argv[2:]
            options.append(args)
    return flag, options

def execute_command(argv):
    flag, options = args(argv)
    if flag == "v":
        verify.verify_random_num(options[0], options[1])



if __name__=="__main__":

    random_str.most_recent()
