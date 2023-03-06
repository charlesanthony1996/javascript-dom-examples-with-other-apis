using System;

static void MergeSort(int[] arr) {
    if (arr.Length > 1) {
        int mid = arr.Length / 2;
        int[] left = new int[mid];
        int[] right = new int[arr.Length - mid];
        for (int i = 0; i < mid; i++) {
            left[i] = arr[i];
        }
        for (int i = mid; i < arr.Length; i++) {
            right[i - mid] = arr[i];
        }
        MergeSort(left);
        MergeSort(right);
        int i = 0;
        int j = 0;
        int k = 0;
        while (i < left.Length && j < right.Length) {
            if (left[i] <= right[j]) {
                arr[k] = left[i];
                i++;
            } else {
                arr[k] = right[j];
                j++;
            }
            k++;
        }
        while (i < left.Length) {
            arr[k] = left[i];
            i++;
            k++;
        }
        while (j < right.Length) {
            arr[k] = right[j];
            j++;
            k++;
        }
    }
}

int[] arr = { 3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5 };
MergeSort(arr);
foreach (int i in arr) {
    Console.Write(i + " ");
}
