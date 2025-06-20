import random

def main():
    #n_random=5
    for n in range(5):
        print(random.randint(1,69))
    print(random.sample(range(1,69),5))
    print (random.randint(1,26))
    #print(random.uniform(1,13))


if __name__ == "__main__":
    main()