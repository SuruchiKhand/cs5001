from math import sqrt

def max3(one, two,three):
    max_two = max(one, two)
    max_three = max(max_two, three)
    return max_three

def test_max3(one, two,three, expected_result):
    actual = max3(one, two, three)
    print("Inputs were: ", one, two, three)
    print(f"Actual  = {actual}, Expected ={expected_result}")

def max_tests():
    print("Testing max3")
    print()
    test_max3(2, 3, 5, 5)
    test_max3(10, 3, 5, 10)
    test_max3(2, 33, 5, 33)

if __name__ == "__main__":
    max_tests()