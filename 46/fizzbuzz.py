def fizzbuzz(num):
    
    if num % 3 == 0 and num % 5 == 0:
        answer = "Fizz Buzz"

    elif num % 3 == 0 and num % 5 != 0:
        answer = "Fizz"
    
    elif num % 3 != 0 and num % 5 == 0:
        answer = "Buzz"
    
    else:
        answer = int(num)

    return answer
