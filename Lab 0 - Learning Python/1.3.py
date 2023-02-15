def PrintChar():
    s = str(input("Enter Word: "));
    for i in range(len(s)):
        if i % 2 == 0:
            print(s[i]);
PrintChar()