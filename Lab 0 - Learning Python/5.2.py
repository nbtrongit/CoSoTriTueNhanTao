def AppMi(s1, s2):
    mi1 = int(len(s1) / 2);
    mi2 = int(len(s1) / 2);
    print(s1[0] + s2[0] + s1[mi1] + s2[mi2] + s1[len(s1) - 1] + s2[len(s2) - 1])
AppMi("Ault", "Kelly")