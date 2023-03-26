using System;
using System.Collections.Generic;

public static class MergeSort
{
    public static void Sort<T>(List <T> list) where T: IComparable<T>
    {
        // if the list is null or has 1 element, its already sorted
        if(list == null || list.Count <= 1)
        {
            return;
        }

        // divide the list into two halves

        int mid = list.Count / 2;
        List<T> left = new List<T>();
        List<T> right = new List<T>();

        // copy the first half of elements to the left part of the list

        for(int i = 0; i< mid; i++)
        {
            left.Add(list[i]);
        }

        // copy the second half of elements to the right part of the list

        for(int i = mid; i < list.Count; i++)
        {
            right.Add(list[i]);
        }

        // revursively sort left and right lists

        Sort(left);
        Sort(right);

        // merge the sorted left and right lists
        Merge(list, left, right);
    }


    private static void Merge<T>(List<T> list, List<T> left, List<T> right) where T: IComparable <T>
    {
        // inits to the variables for indexing
        int leftIndex = 0;
        int rightIndex = 0;
        int arrayIndex = 0;


        while(leftIndex < left.Count && rightIndex < right.Count)
        {

            // compare elements from the left and right lists , and add the smaller one to the left of the list first
            // refer to the viz on this link -> https://www.youtube.com/watch?v=4VqmGXwpLqc

            if(left[leftIndex].CompareTo(right[rightIndex]) <= 0)
            {
                list[arrayIndex] = left[leftIndex];
                leftIndex++;

            }
            else
            {
                list[arrayIndex] = right[rightIndex];
                rightIndex++;
            }

            arrayIndex++;

        }

        // add the remaining elements from the left list

        while(leftIndex < left.Count)
        {
            list[arrayIndex] = left[leftIndex];
            leftIndex++;
            arrayIndex++;

        }

        // add the remaining elements from the right list
        // that were not added to the left one

        while(rightIndex < right.Count)
        {
            list[arrayIndex] = right[rightIndex];
            rightIndex++;
            arrayIndex++;
        }

    }
    
}


public class Program
{
    public static void Main(string[] args)
    {
        // create the list here.
        // get the unsorted numbers to the list
        List<int> list = new List<int> {1, 6, 2, 4, 8, 5 };

        // sort the list using merge sort
        MergeSort.Sort(list);

        // print the sorted list to the console
        Console.Write("Sorted list: ");
        foreach(int num in list)
        {
            Console.Write(num + " ");
        }
    }
}