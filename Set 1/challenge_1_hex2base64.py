import binascii

#s = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

def hex2ascii(s):
    '''
     1. first convert hex to ascii
        straightaway method s.decode("hex")
    '''
    ans = ""
    x = 0
    y = 2
    l = len(s)
    while (y<=l):
        ans += chr(int(s[x:y],16))
        x += 2
        y += 2
    return ans

def raw2hex(s):
    ans = hex2ascii(s)
    '''
     2. now convert ascii to base64
    '''
    return binascii.b2a_base64(ans)
    
def main():
    s = str(raw_input())
    return raw2hex(s)
    
if __name__ == "__main__":
    main()
