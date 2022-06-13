def mod_inverse(a, m):
	m0 = m
	y = 0
	x = 1
	if (m == 1):
		return 0

	while (a > 1):
		q = a // m

		t = m
		m = a % m
		a = t
		t = y
		y = x - q * y
		x = t

	if (x < 0):
		x = x + m0
	return x

def doubling(A):
    s = (3*A[0]**2+a)*mod_inverse((2*A[1])%p,p)%p
    x = (s**2-2*A[0])%p
    y = (s*(A[0]-x)-A[1])%p
    return (x, y)

def add(A,B):
    if A==B: 
        return doubling(A)
    s = (A[1]-B[1])*mod_inverse((A[0]-B[0])%p,p)%p
    x = (s**2-A[0]-B[0])%p
    y = (s*(A[0]-x)-A[1])%p
    return (x, y)

def double_and_add(A,d):
    A_bin = []
    while d>0:
        A_bin.append(d%2)
        d = d//2
        
    B = A
    for i in range(len(A_bin)-2,-1,-1):
        B = doubling(B)
        if A_bin[i]==1:
            B = add(A,B)

    return B

#config
p = 29
a = 4
b = 20
P = (8,10)
Q = (14,23)
P_inverse = (8,19)
Q_inverse = (14,6)

#1
P16 = add(P,Q)
print(f"1. {P16}")

#2
P38 = add(P16,Q_inverse)
print(f"2. {P38}")

#3
P53 = add(P38,Q)
print(f"3. {P53}")

#4
print(f"4. {add(add(P53,Q_inverse),P_inverse)}")

#5
print(f"5. {add(add(P,P),P)}")
