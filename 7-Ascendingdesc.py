y = {'carl': 40, 'alan': 2, 'bob': 1, 'danny': 3}
print("given dictionary",y)
l = list(y.items())
l.sort()
d=dict(l)
print('Ascending order is', d)
l = list(y.items())
l.sort(reverse=True)
dict = dict(l)
print('Descending order is', dict)

