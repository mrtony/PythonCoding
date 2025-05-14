def test_type_define(last_name: str, age: int) -> str:
    result = last_name.capitalize() + " is " + str(age) + " years old."
    return result

def main():
    print("Hello from pythoncoding!")
    test_type_define("Tony", 30)


if __name__ == "__main__":
    main()
