import re, datetime
s = "I have a meeting on 20-12-2010 in New York.iNdia got independence in 12-12-1112"
op = []
match = re.search('\d{2}-\d{2}-\d{4}', s)
date = datetime.datetime.strptime(match.group(), '%d-%m-%Y').date()
print(date)
op.append(date)
print(len(set(op)))


