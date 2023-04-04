#include <iostream>

void merge(int arr[], int left[], int left_size,int right[], int right_size) {
    int i = 0;
    int j = 0;
    int k = 0;

    while(i < left_size && j < right_size) {
        if(left[i] <= right[j]) {
            arr[k++] = left[i++];
        }
        else {
            arr[k++] = right[j++];
        }
    }

    while(i < left_size) {
        arr[k++] = left[i++];
    }

    while(j < right_size) {
        arr[k++] = right[j++];
    }
}

void merge_sort(int arr[], int size) {
    if(size< 2) {
        return;
    }

    int mid = size/ 2;
    int left[mid];
    int right[size - mid];

    for(int i = 0; i < mid; i++) {
        left[i] = arr[i];
    }

    for(int i = mid; i < size; i++) {
        right[i - mid] = arr[i];
    }

    merge_sort(left, mid);
    merge_sort(right, size - mid);
    merge(arr, left, mid, right, size - mid);
}

int main() {
    int arr[] = {1, 3, 2, 4};
    int size = sizeof(arr)/ sizeof(arr[0]);

    merge_sort(arr, size);
    std::cout << "Sorted array: ";
    for(int i = 0; i < size; i++) {
        std::cout << arr[i] << " ";
    }

    std::cout << std::endl;
    return 0;
}