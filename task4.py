
l = [1, 2, 3, 4, 5, 6]
for i in l:
	if i%2==0:

		l = str(l).replace(str(i), 'subbu')
	else:
		l = str(l).replace(str(i), 'Nag')
print(l)