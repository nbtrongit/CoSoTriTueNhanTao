employees = ['K1', 'K2']
defaults = {"designation": 'Developer', "salary": 8000}

d = dict.fromkeys(employees, defaults)

print(d["K1"])