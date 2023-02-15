def Com(s1, s2):
    i_1 = 0;
    i_2 = len(s2) - 1;
    s = "";
    while 1:
        if i_1 != len(s1):
            s += s1[i_1];
        if i_2 != -1:
            s += s2[i_2];
        if i_1 == len(s1) and i_2 == -1:
            break;
        i_1 += 1;
        i_2 -= 1;
    print(s);
s1 = "Abc"
s2 = "Xyz"
Com(s1, s2)