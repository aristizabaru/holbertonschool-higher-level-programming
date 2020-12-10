#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    my_list = dir(hidden_4)
    letter = "s"
    for item in my_list:
        if item[1] is not "_":
            print("{}".format(item))
