from math import pow

y = "34, 45, 40, 38, 44, 41, 42, 52, 53, 56, 59, 61, 47, 48, 60, 58, 51, 62, 67, 54, 57, 72, 68, 65, 66".split(", ")
y = [int(i) for i in y]

def find_a_b():
    sum_x_mul_y = 0
    sum_x = 0
    sum_squared_x = 0
    sum_y = 0
    for i in range(1, len(y) + 1):
        #print("i = ", i, ", x = ", i, ", y = ", y[i - 1])
        sum_x_mul_y += i * y[i -1]
        sum_x += i
        sum_y += y[i - 1]
        sum_squared_x += pow(i, 2)
    a = (len(y) * sum_x_mul_y - sum_x * sum_y)/float(len(y) * sum_squared_x - sum_x * sum_x)
    b = (sum_y - a * sum_x) / float(len(y))
    return a, b

def find_f(a, b):
    f = list(map(lambda x: a * x + b, range(1, len(y) + 1)))
    return f

def calcr2(a, b):
    y_avg = sum(y) / float(len(y))
    numerator = 0
    denumenator = 0
    f = find_f(a, b)
    for i in range(0, len(y)):
        numerator += pow(y[i] - f[i], 2)
        denumenator += pow(y[i] - y_avg, 2)
    return 1 - numerator / float(denumenator)
    

def main():
    a, b = find_a_b()
    print('a = ', a, 'b = ', b)
    r2 = calcr2(a, b)
    print('r2 = ', r2)
    

if __name__ == '__main__':
    main()
