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
	
def zero_transform(matrix, constants, m, step_index):
    step_element = matrix[step_index][step_index]
    step_row = matrix[step_index]
    step_row_sol = constants[step_index]
    for row_index in range(step_index+1, m):
        row = matrix[row_index]
        row_sol = constants[row_index]
        factor = row[step_index]/step_element
        transformed_row = [item * factor for item in step_row]
        transformed_row_sol = step_row_sol * factor
        matrix[row_index] = [x-y for x,y in zip(row,transformed_row)]
        constants[row_index] = row_sol - transformed_row_sol
        matrix[row_index][step_index] = 0
    return [matrix, constants]
	
def gaussian_determinant(matrix, constants):
    m = len(matrix)
    for step_index in range(m-1):
        matrix, constants = zero_transform(matrix, constants, m, step_index)
    diagnols = []
    determinant = 1
    for index in range(m):
        diagnols.append(matrix[index][index])
        determinant *= matrix[index][index]
    determinant = int(determinant*(10**2))/(10**2)
    return determinant
	
def check_zero_diagnol(matrix):
    m = len(matrix)
    for index in range(m):
        item = matrix[index][index]
        if (item == 0):
            return True
    return False
	
def singularity_check(A,B):
    matrix = list(A)
    constants = list(B)
    m = len(matrix)
    determinant = gaussian_determinant(matrix, constants)
    if (determinant == 0):
        if (check_zero_diagnol(matrix)):
            if(matrix[m-1][m-1] == 0 and constants[m-1] == 0):
                return 0
            else:
                return -1
        else:
            return 0
    return 1
	
def solve_equations(test_case):
    m, A, B = parse_case(test_case)
    non_singularity = singularity_check(A,B)
    if (non_singularity == 0 or non_singularity == -1):
        return [non_singularity,[],[]]
    lower, upper = doolittle_algorithm(A)
    zero_diagnol = check_zero_diagnol(upper)
    if (zero_diagnol):
        return 0
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
    if(solution == 0 or solution == -1):
        output += str(solution) + '\n'
    else: 
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