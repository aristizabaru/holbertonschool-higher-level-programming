#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print("{:d} {}:".format(len(sys.argv)-1, "argument" if len(sys.argv)
                                == 2 else "arguments"))
        for arg_index in range(1, len(sys.argv)):
            print("{}: {}".format(arg_index, sys.argv[arg_index]))
    else:
        print("0 arguments.")
