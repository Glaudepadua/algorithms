#Iteractive version

def fibonatti_iteractive(n):
    previous = 0
    current = 1
    final = 0

    for _ in range(n-1):
        final = current + previous
        previous = current
        current = final

    return final

def main():
    print("Type a number")    
    num = int(input())
    result = fibonatti_iteractive(num)
    print("Referred fibonacci sequence: " + str(result))

if __name__ == "__main__":
    main()