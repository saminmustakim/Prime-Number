from prime_number import prime_number

if __name__ == "__main__":
    n = int(input("Input a number: "))
    prime = prime_number(n)
    if prime is True:
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")