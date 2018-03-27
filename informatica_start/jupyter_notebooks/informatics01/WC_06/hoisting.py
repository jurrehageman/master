
def function_1():
    print("running function_1")
    function_2()


def function_2():
    print("running function_2")


def main():
    print("main running")
    function_1()


main()