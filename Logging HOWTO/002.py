import logging


def printN():
    logging.info("Doing something")
    print("*"*5)


def main():
    logging.basicConfig(filename="myapp.log", level=logging.INFO)
    logging.info("Started")
    printN()
    logging.info("Finished")

if __name__ == '__main__':
    main()