def sum_numbers(numbers=None):
    if numbers is None:
        numbers = [number for number in range(1, 101)]
    
    return sum(numbers) 
