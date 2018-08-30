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
    m = int(test_case[0])
    A = []
    for row_index in range(m):
        row = list(map(float, test_case[row_index+1].split()))
        A.insert(row_index, row)
    B = list(map(float, test_case[m+1].split()))
    return [m,A,B]

def doolittle_algorithm(A):
    n = len(A)
    lower = [[0] * n for index in range(n)]
    upper = [[0] * n for index in range(n)]
    
    for i in range(n):
        for k in range(i,n):
            summation = 0
            for j in range(i):
                summation += lower[i][j] * upper[j][k]
            upper[i][k] = A[i][k] - summation
        
        for k in range(i,n):
            if (i == k):
                lower[i][i] = 1
            else:
                summation = 0
                for j in range(0,i):
                    summation += lower[k][j] * upper[j][i]
                lower[k][i] = (A[k][i] - summation) / upper[i][i]
    return [lower,upper]
	
def LY_B(lower,B):
    n = len(lower)
    Y = [0 for i in range(n)]
    summation = 0
    for i in range(n):
        summation = 0
        for j in range(i):
            summation += lower[i][j] * Y[j]
        Y[i] = B[i] - summation    
    return Y
	
def UX_Y(upper,Y):
    n = len(upper)
    X = [0 for i in range(n)]
    summation = 0
    for i in range(n):
        summation = 0
        for j in range(n-i,n):
            summation += upper[n-i-1][j] * X[j]
        X[n-i-1] = (Y[n-i-1] - summation)/upper[n-i-1][n-i-1]
    return X
	
def solve_equations(test_case):
    m, A, B = parse_case(test_case)
    lower, upper = doolittle_algorithm(A)
    Y = LY_B(lower,B)
    X = UX_Y(upper,Y)
    return [X, upper, lower]
	
results = []
for test_case in test_cases:
    result = solve_equations(test_case)
    results.append(result)
	
def array_to_string(array):
    string = ''
    for item in array:
        string += str(item)+' '
    string = string.strip()
    return string
	
output = ''
for result in results:
    solution, upper, lower = result
    output += array_to_string(solution) + '\n'
    for row in upper:
        output += array_to_string(row) + '\n'
    for row in lower:
        output += array_to_string(row) + '\n'
    output += '\n'
output = output.strip()

output_file = open('output.txt', 'w')
output_file.write(output)
output_file.close()