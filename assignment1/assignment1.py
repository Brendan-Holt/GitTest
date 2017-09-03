import sys

from controller import Controller


def main(argv):
    controller = Controller(True, sys.argv)
    controller.go()

if __name__ == "__main__":
    main(sys.argv)