import argparse

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_numbers(low, high):
    if low < 2:
        low = 2
    if low > high:
        return []
    prime_list = []
    for num in range(low, high + 1):
        if is_prime(num):
            prime_list.append(num)
    return prime_list

def main():
    parser = argparse.ArgumentParser(description="Find prime numbers in a given range.")
    parser.add_argument("low", type=int, help="The lower bound of the range")
    parser.add_argument("high", type=int, help="The upper bound of the range")
    args = parser.parse_args()
    
    low = args.low
    high = args.high

    result = prime_numbers(low, high)
    print(result)

if __name__ == '__main__':
    main()