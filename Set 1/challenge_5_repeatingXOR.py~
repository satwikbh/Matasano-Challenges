import binascii

def main(s,key):
    s = binascii.hexlify(s)
    key = binascii.hexlify(key)
    if(len(s) < len(key)):
        s,key = key,s
    key *= int(1 + len(s)/len(key))
    key = key[:len(s)]
    
    ans = ""
    
    for x in xrange(len(s)):
        ans += hex( int(s[x],16) ^ int(key[x],16)).split('x')[1]
    
    return ans
        

if __name__ == "__main__":
    s = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = "ICE"
    ans = b"0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    if(ans == main(s,key)):
        print "Yes"
    else:
        print "No"
