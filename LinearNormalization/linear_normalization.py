from string import ascii_lowercase

input_file_name = 'input.txt'

def normalize(arr):
    max_x = max(arr)
    min_x = min(arr)
    result = []
    for x in arr:
        result.append((x - min_x)/float(max_x - min_x))
    print('min = ', min_x, ' max = ', max_x, ' delta = ', (max_x - min_x))
    return result

def main():
    file = open(input_file_name, "r")
    col1 = []
    col2 = []
    col3 = []
    for line in file:
        cols = line.split()
        col1.append(int(cols[1]))
        col2.append(int(cols[2]))
        col3.append(int(cols[3]))
    normalizedcol1 = normalize(col1)
    normalizedcol2 = normalize(col2)
    normalizedcol3 = normalize(col3)
    print('Col1', col1, '\n\n', normalizedcol1)
    print('Col2', col2, '\n\n', normalizedcol2)
    print('Col3', col3, '\n\n', normalizedcol3)

    final_result = {}
    for i in range(0, len(normalizedcol1)):
        final_result[ascii_lowercase[i]] = normalizedcol1[i] + normalizedcol2[i] + normalizedcol3[i]
        print('i = ', i, ' res ', final_result)
    print(sorted(final_result.items(), key=lambda x: x[1], reverse = True))
    

if __name__ == '__main__':
    main()
