using System;

namespace Test // no semicolon after namespace declaration

{
    public class BubbleSort<T> where T: IComparable<T>
    {

        public static void Main(string[] args )
        {
            int[] arr = { 5, 2, 4, 4, 2, 3, 12 };
            BubbleSort<int>.Sort(arr);
            foreach (int i in arr)
            {
                Console.Write(i + " ");
            }
        }


        public static void Sort(T[] arr)
        {
            int n = arr.Length;

            for (int i = 0 ; i < n; i++)
            {
                for (int j = 0; j < n - 1; j++ ) 
                {
                    if(arr[j].CompareTo(arr[j + 1]) > 0)
                    {
                        T temp = arr[j];
                        arr[j] = arr[j+ 1];
                        arr[ j+ 1 ] = temp;
                    }
                }
            }
        }
    }
}
