import binascii


a = 5
c = 160
a1 = "{0:b}".format(a).zfill(8)
a2 = "{0:b}".format(c).zfill(8)

b = a1+a2

print(b == "0000010110100000")

d = int(a1, 2)
print(type(d), d)
