
def insertion_sort(input_arr):
    for i in range(1, len(input_arr)):
        key_1 = input_arr[i]

        j = i - 1

        while j >= 0 and key_1 < input_arr[j]:
            input_arr[j + 1] = input_arr[j]
            j -= 1

        input_arr[j + 1] = key_1 #since J is less than 0, 
        #bring it back to range

    return input_arr

def selection_sort(input_arr):
    
    for i in range(len(input_arr)):
        min_index = i
        for j in range(i + 1, len(input_arr)):
            if input_arr[j] < input_arr[min_index]:
                min_index = j

        input_arr[i], input_arr[min_index] = input_arr[min_index], input_arr[i]

    return input_arr

def main():
    #result = insertion_sort([12, 11, 13, 5, 6])
    result = selection_sort([12, 11, 13, 5, 6])
    print("sorted", result)


if __name__ == '__main__':
    main()