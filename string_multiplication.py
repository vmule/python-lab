def string_multiplication(a, b):
    result = 0
    for i in range(len(a)):
        for j in range(len(b)):
            result += (ord(a[i])-ord('0'))*(10**(len(a)-i-1))*(ord(b[j])-ord('0'))*(10**(len(b)-j-1))
    return result

number_one = 193283492420348904832902348908239048823480823
number_two = 3248234890238902348823940990234
print(number_one*number_two)
print(string_multiplication(str(number_one), str(number_two)))
