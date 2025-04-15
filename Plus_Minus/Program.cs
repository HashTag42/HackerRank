using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

class Result
{

    /*
     * Complete the 'plusMinus' function below.
     *
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static void plusMinus(List<int> arr)
    {
        int tot = arr.Count;
        float neg = 0, zer = 0, pos = 0;
        for (int i = 0; i < arr.Count; i++)
        {
            int num = arr[i];
            if (num > 0)
                pos++;
            else if (num < 0)
                neg++;
            else
                zer++;
        }
        Console.WriteLine((pos / tot).ToString("F6"));
        Console.WriteLine((neg / tot).ToString("F6"));
        Console.WriteLine((zer / tot).ToString("F6"));
    }
}

class Solution
{
    public static void Main(string[] args)
    {
        // int n = Convert.ToInt32(Console.ReadLine().Trim());

        // List<int> arr = Console.ReadLine().TrimEnd().Split(' ').ToList().Select(arrTemp => Convert.ToInt32(arrTemp)).ToList();
        List<int> arr = new List<int> { -4, 3, -9, 0, 4, 1};

        Result.plusMinus(arr);
    }
}
