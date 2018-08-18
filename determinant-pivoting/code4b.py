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
    matrix = []
    for row_index in range(m):
        row = list(map(float, test_case[row_index+1].split()))
        matrix.insert(row_index, row)
    return [m,n,matrix]

def pivoting(matrix, m, step_index):
    step_element = matrix[step_index][step_index]
    step_column = [row[step_index] for row in matrix]
    step_column_required = step_column[step_index:]
    
    max_element = max(step_column_required, key=abs)
    swap = False
    if (abs(step_element) >= max_element):
        return [matrix, swap]
    swap = True
    
    max_value = max(step_column_required)
    min_value = min(step_column_required)
    if abs(max_value) > abs(min_value):
        max_abs_value = max_value
    else:
        max_abs_value = min_value
    
    max_index = step_column.index(max_abs_value)
    
    temp_row = matrix[step_index]
    matrix[step_index] = matrix[max_index]
    matrix[max_index] = temp_row
    
    return [matrix, swap]

def zero_transform(matrix, m, step_index):
    step_element = matrix[step_index][step_index]
    step_row = matrix[step_index]
    for row_index in range(step_index+1, m):
        row = matrix[row_index]
        factor = row[step_index]/step_element
        transformed_row = [item * factor for item in step_row]
        matrix[row_index] = [x-y for x,y in zip(row,transformed_row)]
        matrix[row_index][step_index] = 0
    return matrix
	
def gaussian_determinant(test_case):
    m,n,matrix = parse_case(test_case)
    if (m!=n):
        return 'Invalid Shape. Square matrices only.'
    
    swap_coefficient = 1
    for step_index in range(m-1):
        matrix, swap = pivoting(matrix, m, step_index)
        matrix = zero_transform(matrix, m, step_index)
        if (swap):
            swap_coefficient *= -1
    
    diagnols = []
    determinant = 1
    for index in range(m):
        diagnols.append(matrix[index][index])
        determinant *= matrix[index][index]
    determinant *= swap_coefficient
    determinant = round(determinant,2)
    return determinant

determinants = []
for test_case in test_cases:
    determinant = gaussian_determinant(test_case)
    determinants.append(determinant)
	
output_file = open('output.txt', 'w')
output = ''
for determinant in determinants:
    output += str(determinant)+'\n'

output = output.strip()
output_file.write(output)
output_file.close()