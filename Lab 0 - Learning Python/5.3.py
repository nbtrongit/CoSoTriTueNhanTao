def lower(s):
    lower = "";
    upper = "";
    for i in s:
        if i.islower():
            lower += i;
        else:
            upper += i;
    print(lower + upper);
lower("PyNaTive")