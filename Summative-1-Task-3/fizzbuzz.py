def fizzbuzz(n):
    '''
    Returns a list of strings representing the FizzBuzz game up to n

    Parameter: n, The upper limit for the FizzBuzz game.
    '''
    result = ["Fizz" * (not n % 3) + "Buzz" * (not n % 5) or n for n in range(1, n+1)]
    return result



print(fizzbuzz(15))
