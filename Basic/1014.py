import string

s1 = raw_input()
s2 = raw_input()
s3 = raw_input()
s4 = raw_input()
l1 = min(len(s1), len(s2))
l2 = min(len(s3), len(s4))

common_1 = filter(lambda x: s1[x] == s2[x] and s1[x] in string.uppercase[:7], xrange(l1))[0]
common_2 = filter(lambda x: s1[x] == s2[x] and s1[x] in string.digits + string.uppercase[:14], xrange(common_1 + 1, l1))[0]
common_3 = filter(lambda x: s3[x] == s4[x] and s3[x].isalpha(), xrange(l2))[0]

w = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'][string.uppercase[:7].index(s1[common_1])]
h = (string.digits + string.uppercase[:14]).index(s1[common_2])
m = common_3
print "%s %02d:%02d" % (w, h, m)