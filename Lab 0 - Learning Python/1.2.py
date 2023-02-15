def SumPre(a):
    s = "Printing current and previous number sum in a range({0})"
    print(s.format(a));
    pre = 0;
    s = "Current Number {0} Previous Number  {1}  Sum:  {2}";
    for i in range(10):
        sum = pre + i;
        print(s.format(i, pre, sum));
        pre = i;

SumPre(10);