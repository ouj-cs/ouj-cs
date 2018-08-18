import string
def encode(s):
    s=[c for c in s.upper() if c in string.ascii_uppercase]
    def morse_code():
        return ("A .- B -... C -.-. D -.. E . F ..-. G --. H .... I .. J .--- "
                "K -.- L .-.. M -- N -. O --- P .--. Q --.- R .-. S ... T - "
                "U ..- V ...- W .-- X -..- Y -.-- Z --..")
    def get_dict():
        ss=morse_code().split()
        return dict((key, value) for key,value in zip(ss[0::2],ss[1::2]))
    def encode_character(dic,char):
        lis=[]
        for c in dic[char]:
            if c==".":
                lis+=[(0.2,True),(0.2,False)]
            elif c=="-":
                lis+=[(0.6,True),(0.2,False)]
            else:
                assert(False)
        return lis
    lis=[]
    for c in s:
        lis+=encode_character(get_dict(),c)
        # lis+=[(0.6,False)]
    return lis
