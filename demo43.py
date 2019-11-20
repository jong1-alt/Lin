sales = ['S', 'M', 'L', 'S', 'L', 'M', 'L', 'S', 'L', 'S', 'L', 'M', 'L']
statistics = {}
for r in sales:
    statistics.setdefault(r, 0)
    statistics[r] += 1
print(statistics)
sales2 = [('S', 20), ('M', 30),
          ('L', 15), ('S', 20),
          ('L', 8), ('M', 13),
          ('L', 14), ('S', 9),
          ('L', 15), ('S', 4),
          ('L', 3), ('M', 8), ('L', 12)]
statistics2 = {}
for r, q in sales2:
    statistics2.setdefault(r, 0)
    statistics2[r] += q
print(statistics2)
