#Iterative algorithm
def fibonatti_iterative(num):
    '''
    Return the referred value of a position of Fibonacci sequence.
    Iterative algotithm

    Parameters:
        num (int): position number

    Returns:
        Calculate the value of the given position in Fibonacci sequence
    '''

    previous = 0
    current = 1
    final = 0

    for _ in range(num-1):
        final = current + previous
        previous = current
        current = final

    return final

#Recursive algorithm
def fibonacci_recursive(num):
    '''
    Return the referred value of a position of Fibonacci sequence.
    Recursive algotithm

    Parameters:
        num (int): position number

    Returns:
        Calculate the value of the given position in Fibonacci sequence
    '''
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return fibonacci_recursive(num-1) + fibonacci_recursive(num-2)

def main():
    print("Type a number")
    num = int(input())

    result = fibonatti_iterative(num)
    print("Referred fibonacci sequence (iteractive): " + str(result))

    result = fibonacci_recursive(num)
    print("Referred fibonacci sequence (recursive): " + str(result))

if __name__ == "__main__":
    main()