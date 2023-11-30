#!/usr/bin/python3
if __name__ == "__main__":

    import hidden_4

    for q in dir(hidden_4):
        if q[:2] != "__":
            print("{}".format(q))
