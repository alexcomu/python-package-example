def program():
    print "Welcome to my package!"


def main():
    try:
        program()
    except Exception as e:
        print e

if __name__ == "__main__":
    main()
