// See https://aka.ms/new-console-template for more information
void staircase(int n)
{
    for (int i = 0; i < n; i++)
    {
        string line = "";
        for (int j = 0; j < i+1; j++)
        {
            line += "#";
        }
        line = string.Format("{0," + n +"}", line);
        Console.WriteLine(line);
    }
}

staircase(6);