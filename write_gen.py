def print_gen(res_gen):
    print("Генератор:\t", end=' ')
    while True:
        try:
            print(next(res_gen), end=' ')
        except StopIteration:
            print("\nГенератор вернул все элементы\n")
            break
