def main():
    try:
        divisor = 0
        x = 1 / divisor
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
    
    try:
        my_dict = {'name': 'Alice'}
        age = my_dict.get('age', 'N/A')
        print(f"Age: {age}")
    except KeyError as e:
        print(f"KeyError: {e}")

    try:
        num = int('abc')  # ValueError
    except ValueError as e:
        print(f"ValueError: {e}")

if __name__ == "__main__":
    main()
