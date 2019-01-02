def transform_complex_array(array):
    if len(array) == 1:
        final_array.append(array)
        return
    for j in array:
        if isinstance(j, int):
            final_array.append(j)
            continue

        if len(j) == 1:
            if isinstance(j, list):
                final_array.append(j[0])
                continue
            final_array.append(j)
            continue
        else:
            transform_complex_array(j)


if __name__ == "__main__":
    # test_array = [8, [1, 2, 3, 4], 8, [5, 6], 9, [7, 8, 9]]
    test_array = ['a', ['c', 1, 3], ['f', 7, [4, '4', ['a', 'b', ['x', 'y']]]], [{'la la la': 111}, {'test': 36}]]
    # test_array = input("Input array: ")
    final_array = []
    transform_complex_array(test_array)
    print(test_array)
    print(final_array)
