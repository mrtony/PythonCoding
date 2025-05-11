def list_comprehension_example():
    # Example of list comprehension to create a list of squares of even numbers from 1 to 10
    squares_of_even_numbers = [x**2 for x in range(1, 11) if x % 2 == 0]
    print("Squares of even numbers from 1 to 10:", squares_of_even_numbers)


def apply_lambda_to_list(lambda_func):
    # Example of applying a lambda function to a list of numbers
    numbers = [1, 2, 3, 4, 5]
    result = [lambda_func(x) for x in numbers]
    print("Result after applying lambda function:", result)


def string_closure(input_string):
    # Closure that appends a suffix to the input string
    def append_suffix(suffix):
        return input_string + suffix

    return append_suffix


### Example usage

list_comprehension_example()

# output: Result after applying lambda function: [2, 4, 6, 8, 10]
apply_lambda_to_list(lambda x: x * 2)

closure_func = string_closure("Hello")
print(closure_func(" World!"))  # output: Hello World!
