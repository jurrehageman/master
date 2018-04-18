class NotDnaBaseError(Exception):
    pass


def validate(*args):
    bases = "GATC"
    for arg in args:
        #print(arg)
        for base in arg:
            if base not in bases:
                raise NotDnaBaseError(arg)


def main():
    try:
        validate("atcg".upper(), "atcf".upper())
    except NotDnaBaseError as e:
        print("Oops", e, type(e).__name__)


if __name__ == "__main__":
    main()
