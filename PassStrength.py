print("""Password Strength Test
(Checks if password is long enough or if it has any match with username or if it has characters in same sequence; eg-4567,bcde)
""")
a=input("""Please enter your Username
""")
b=input("""Please enter your Password
""")
def len_check(u,p):
    if len(p)>=8:
        return True
def pass_match(u,p):
    un,us,pn,ps="","","",""
    for i in u:
        if i.isdigit()==True:
            un=un+i
        else:
            us=us+i
    for i in p:
        if i.isdigit()==True:
            pn=pn+i
        else:
            ps=ps+i
    if ps in u or pn in u:
        return False
    else:
        return pn,ps
def diff_check(func_match):
    pn,ps=func_match
    for i in range(len(pn)):
        if i <= 1:
            x=int(pn[1])-int(pn[0])
        else:
            if int(pn[i])-int(pn[i-1])==x:
                return True
            else:
                x=int(pn[i])-int(pn[i-1])
def seq_check(func_match):
    pn,ps=func_match
    for i in range(len(ps)):
        if i <= 1:
            x=ord(ps[1])-ord(ps[0])
        else:
            if ord(ps[i])-ord(ps[i-1])==x:
                return True
            else:
                x=ord(ps[i])-ord(ps[i-1])
if len_check(a,b)==True:
    if pass_match(a,b)==False:
        print("Oops! your Password is somewhat simillar to username")
    else:
        if diff_check(pass_match(a,b))==True or seq_check(pass_match(a,b))==True:
            print("Oops! your Password contains characters or numbers in sequence")
        else:
            print("""Your Password is STRONG enough!!
It have successfully passed through all our tests""")
else:
    print("Oops! your Password is too short")
print("""

Thank You""",a,"""for using us.""")