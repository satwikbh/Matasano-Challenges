a = "1c0111001f010100061a024b53535009181c"
b = "686974207468652062756c6c277320657965"

ans = ""

for x in xrange(len(a)):
    ans += hex(int(a[x],16) ^ int(b[x],16)).split('x')[1]
    
print ans
