import pickle

with open("hello1.txt","rb") as f:

    while True:
        try:
            obj = pickle.load(f)
            obj.disp()
        except EOFError:
            print("Done")
            break