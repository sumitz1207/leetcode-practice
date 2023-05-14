public int reverse(int x)
{
    int r = 0;

    while (x != 0)
    {
        int t = x % 10;
        int n = r * 10 + t;
        if ((n - t) / 10 != r)
        { return 0; }
        r = n;
        x = x / 10;
    }

    return r;
}
