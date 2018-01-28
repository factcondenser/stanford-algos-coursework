import sys

if len(sys.argv) != 3:
    print 'Usage: python karatsuba.py x y'
    sys.exit(1)

# num1 = int(sys.argv[1])
# num2 = int(sys.argv[2])
#
# def karatsuba(x,y):
# 	if len(str(x)) == 1 or len(str(y)) == 1:
# 		return x*y
# 	else:
# 		n = max(len(str(x)),len(str(y)))
# 		nby2 = n / 2
#
# 		a = x / 10**(nby2)
# 		b = x % 10**(nby2)
# 		c = y / 10**(nby2)
# 		d = y % 10**(nby2)
#
# 		ac = karatsuba(a,c)
# 		bd = karatsuba(b,d)
# 		ad_plus_bc = karatsuba(a+b,c+d) - ac - bd
#
#         	# this little trick, writing n as 2*nby2 takes care of both even and odd n
# 		prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd
#
# 		return prod
#
# print karatsuba(num1, num2)

arg1 = sys.argv[1]
arg2 = sys.argv[2]

def karatsuba(x, y):
    lenx = len(x)
    leny = len(y)
    dif = lenx - leny
    if dif > 0:
        y = ('0' * dif) + y
    elif dif < 0:
        x = ('0' * -dif) + x

    n = len(x) # both are same length at this point due to leading 0's
    if len(x.lstrip('0')) <= 1 or len(y.lstrip('0')) <= 1:
        return int(x) * int(y)
    else:
        m = n - (n/2)

        a = x[:m]
        b = x[m:]
        c = y[:m]
        d = y[m:]
        lg = karatsuba(a, c)
        sm = karatsuba(b, d)
        md = karatsuba(str(int(a) + int(b)), str(int(c) + int(d))) - lg - sm
        return ((10**(n/2*2)) * lg) + ((10**(n/2)) * md) + sm

print karatsuba(arg1, arg2)
