import sys

"""
這個範例展示了如何使用可變參數來計算數字的總和。
Python 允許在函式定義中使用 * 和 ** 來接受可變數量的參數。

*args 表示函式可以接受任意數量的「位置參數」，這些參數在函式內部會被匯集成一個 tuple（元組）。換言之，使用 *args
能將呼叫函式時傳入的多個位置引數打包成一個元組，透過變數 args 來使用。

**kwargs 則表示函式可以接受任意數量的「關鍵字參數」，所有傳入的額外關鍵字引數將被匯集成一個 dictionary（字典）

結論: 
1. 函式定義中的 *args 和 **kwargs 分別讓函式能處理不定數量的位置引數與關鍵字引數。
2. *args 和 **kwargs 中的變數名稱並非語法關鍵字，而只是慣例用法。

chatgpt: https://chatgpt.com/share/681ec0e5-9eac-800d-98ef-ffe2c1aeac13
"""


def sum_numbers_args(*args):
    """python的可變參數-tuple"""
    print("type:", type(args))
    """Return the sum of all provided numbers."""
    return sum(args)


def sum_numbers_kwargs(**numbers):
    """python的可變參數-dicte"""
    print("type:", type(numbers))
    """Return the sum of all provided numbers."""
    return sum(numbers.values())


def main():
    print("Sum:", sum_numbers_args(1, 2, 3, 4))
    print("Sum:", sum_numbers_kwargs(num1=1, num2=2, num3=3, num4=4))


if __name__ == "__main__":
    main()
