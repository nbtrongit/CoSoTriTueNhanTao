l1 = [54, 44, 27, 79, 91, 41]
def ReAdd(l1):
    item = l1.pop(4);
    l1.insert(2, item);
    l1.append(item);
    print(l1);
ReAdd(l1)