// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

static string timeConversion(string s)
{
    string result = "";
    int hour = int.Parse(s.Substring(0,2));

    if ("AM" == s.Substring(8,2))
    {
        hour = (12 == hour) ? 0 : hour;
    }
    else
    {
        hour = (12 == hour) ? hour : hour+12;
    }

    result = hour.ToString("D2") + s.Substring(2,6);
    return result;
}

Console.WriteLine(timeConversion("07:05:45PM"));
Console.WriteLine(timeConversion("12:40:22AM"));
Console.WriteLine(timeConversion("12:45:54PM"));