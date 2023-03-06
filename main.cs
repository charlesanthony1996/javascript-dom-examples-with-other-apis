using System;

    static void BubbleSort(int[] arr) {
        // n is the length of the array
        int n = arr.Length;
        // array starts from position 0 to the last. hence the last is number of elements minus 1
        for (int i = 0; i < n - 1; i++) {
            
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
}

int[] arr = { 1, 4, 2, 3 };
BubbleSort(arr);
foreach (int i in arr) {
    Console.Write(i + " ");
}
