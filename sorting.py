
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


def bubble_sort(input_arr):
    n = len(input_arr)

    for i in range(n):

        for j in range(0, n - i - 1):
            if input_arr[j] > input_arr[j + 1]:
                input_arr[j], input_arr[j + 1] = input_arr[j + 1], input_arr[j]

    return input_arr

def merge_sort(input_arr):

    if len(input_arr) > 1 :
        middle = len(input_arr) // 2
        left_half = input_arr[:middle]
        right_half = input_arr[middle:]

        merge_sort(left_half)
        merge_sort(right_half)

        i,j,k = 0,0,0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                input_arr[k] = left_half[i]
                i += 1
            else:
                input_arr[k] = right_half[j]
                j += 1

            k += 1

        # check the arrays to ensure they have all been merged
        
        while i < len(left_half):
            input_arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            input_arr[k] = right_half[j]
            j += 1
            k += 1
    return input_arr



def main():
    #result = insertion_sort([12, 11, 13, 5, 6])
    #result = selection_sort([12, 11, 13, 5, 6])
    #result = bubble_sort([64, 34, 25, 12, 22, 11, 90])
    result = merge_sort([38, 27, 43, 3, 9, 82, 10])
    print("sorted", result)


if __name__ == '__main__':
    main()