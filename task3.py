s = '123456'
s1 = 'abcd'

print(''.join([''.join(i) for i in zip(s,s1)]) + s[min(len(s), len(s1)):])