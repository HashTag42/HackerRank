// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");


int birthdayCakeCandles(List<int> candles)
{
    int result = 0;
    int maxNum = 0;
    Dictionary<int, int> counts = new Dictionary<int, int>();

    for (int i = 0; i < candles.Count; i++)
    {
        int num = candles[i];
        try
        {
            counts[num]++;
        }
        catch
        {
            counts.Add(num, 1);
        }
        maxNum = (num > maxNum) ? num : maxNum;
    }

    result = counts[maxNum];
    return result;
}

List<int> candles = new List<int> { 3, 2, 1, 3};

Console.WriteLine(birthdayCakeCandles(candles));