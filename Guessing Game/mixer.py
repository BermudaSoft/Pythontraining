from random import shuffle
import Parameters

jumbler = list(range(int(Parameters.s), int(Parameters.e)))
shuffle(jumbler)





if __name__ == '__main__':
    print(jumbler)