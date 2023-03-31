#include <iostream>

void bubblesort(int arr[], int size) {
    for(int i =0; i <size - 1; ++i) {
        for(int j = 0; j < size - i - 1; ++j) {
            if(arr[j]> arr[j+1]) {
                std::swap(arr[j], arr[j+ 1]);
            }
        }
    }

}

int main() {
    int arr[] = {1, 3, 2, 4, 22, 1, 5, 6, 4, 2, 8, 5, 7};
    // to get the number of elements in the array
    int size = sizeof(arr)/sizeof(arr[0]);

    bubblesort(arr, size);

    std::cout << "Sorted array: \n";
    for(int i = 0; i < size; ++i) {
        std::cout << arr[i] << " ";
    }

    std::cout << std::endl;
    return 0;
}