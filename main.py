# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def fibonacci_brute_force(n):

    if n<=1:
        return n
    else:
        return fibonacci_brute_force(n-1) * fibonacci_brute_force(n-2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x =fibonacci_brute_force(3)
    print(x)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
