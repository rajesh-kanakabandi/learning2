"""
    this is my first python program.
"""
def say_hello():
    """
        this is a doc string that describes the method say_hello
        this method says Hello on the Console
        takes no args
        returns none
    """
    print("Hello")


if __name__ == '__main__':
    print(say_hello.__doc__)
    say_hello()
