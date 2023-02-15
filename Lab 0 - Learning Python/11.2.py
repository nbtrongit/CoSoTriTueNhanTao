from datetime import datetime as d
s = "Feb 25 2020 4:20PM"
date = d.strptime(s, '%b %d %Y %I:%M%p')
print(date)