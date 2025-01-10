// See https://aka.ms/new-console-template for more information
void miniMaxSum(List<int> arr)
{
    int min = 1000000000, max = 0;
    uint tot = 0;
    Console.WriteLine(Int32.MaxValue);
    for (int i = 0; i < arr.Count; i++)
    {
        tot += (uint) arr[i];
        min  = (arr[i] < min) ? arr[i] : min;
        max  = (arr[i] > max) ? arr[i] : max;
    }
    Console.WriteLine($"{tot-max} {tot-min}");
}

List<int> arr = new List<int> { 256741038 , 623958417 , 467905213 , 714532089 , 938071625};

miniMaxSum(arr);