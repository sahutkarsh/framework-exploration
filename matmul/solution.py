input_file = open('input.txt','r')
input_lines = input_file.readlines()
input_file.close()

lines = []
for line in input_lines:
    if (line!='\n'):
        line = line.strip()
    lines.append(line)

num_cases = lines[0]
del lines[0]
lines.append('\n')
test_cases = []
case = []

for line in lines:
    if (line!='\n'):
        case.append(line)
    if (line=='\n'):
        test_cases.append(case)
        case = []

def parse_case(test_case):
    m, n = test_case[0].split()
    m = int(m)
    n = int(n)
    j, k = test_case[m+1].split()
    j = int(j)
    k = int(k)
    a = []
    b = []
    for row_index in range(m):
        row = list(map(int, test_case[row_index+1].split()))
        a.insert(row_index, row)
    for row_index in range(j):
        row = list(map(int, test_case[row_index+m+1].split()))
        b.insert(row_index, row)
    return [m,n,j,k,a,b]

def multiply_matrix(test_case):
    m, n, j, k, a, b = parse_case(test_case)
    if (n!=j):
        return -1
    product = []
    zero_row = []
    for x in range(k):
        zero_row.append(0)
    for x in range(m):
        product.append(zero_row)
    for x in range(m):
        for y in range(k):
            for z in range(n):
                product[x][y] += a[x][z] * b[z][y]
    return product

products = []
for test_case in test_cases:
    product = multiply_matrix(test_case)
    products.append(product)

output_file = open('output.txt', 'w')

output = ''
for product in products:
    for row in product:
        row_str = [str(item) for item in row]
        row_str = ' '.join(row_str)
        output += row_str+'\n'
    output += '\n'

output = output.strip()
output_file.write(output)

output_file.close()
