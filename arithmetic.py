def fast_exp(a,b,n):
    if (b==0):
        return 1%n
    elif (b%2==0):
        return fast_exp(a*a,b/2)
    else :
        return (a*(fast_exp(a*a,b/2)))%n
