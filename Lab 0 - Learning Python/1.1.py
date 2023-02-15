def MultiSum (a,b):
    kq = a * b;
    if kq <= 1000:
        return kq;
    else:
        return a + b;

kq = MultiSum(40,30);
print("The result is", kq);
