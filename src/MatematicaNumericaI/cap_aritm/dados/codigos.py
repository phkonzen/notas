import numpy as np

def packBitsInt(ld, n=8):
    x = -ld[n-1] * 2**(n-1)
    for i, d in enumerate(ld[:n-1]):
        x += d * 2**i
    return x


def unpackBitsInt(x, n=8):
    ld = n*[0]
    if (x < 0):
        ld[n-1] = 1
        x += 2**(n-1)
    for i in range(n-1):
        ld[i] = x % 2
        x //= 2
    return ld

def unpackBitsDouble(x):
    ld = 64*[0]
    if ( x == 0):
        return ld
    elif (x < 0):
        ld [0] = 1
    x = np.fabs(x)
    c = int(np.log2(x) + 1023)
    m = x/2**(c - 1023)
    for i in range(11):
        ld [11 - i] = c % 2
        c //= 2
    m -= 1
    for i in range(52):
        m *= 2
        ld [12+ i] = int(m)
        m %= 1
    return ld

def packBitsFloat32(ld):
    c = 0
    for i,d in enumerate(ld[1:9]):
        c += d * 2**(7-i)
    m = 1.
    for i,d in enumerate(ld[9:]):
        m += d * 2**(-(i+1))
    x = m * 2**(c-127)
    return -x if ld[0] else x
    
