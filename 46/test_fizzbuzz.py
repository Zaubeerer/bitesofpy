from fizzbuzz import fizzbuzz

def test_fizzbuzz():
    input_numbers = range(1, 37)

    expected_string = "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, Fizz Buzz, 31, 32, Fizz, 34, Buzz, Fizz".split(", ") 
    
    expected = []
    for string in expected_string:
        if string not in ["Fizz", "Buzz", "Fizz Buzz"]:
            expected.append(int(string))
        else: 
            expected.append(string)

    result = [fizzbuzz(number) for number in input_numbers]

    assert result == expected