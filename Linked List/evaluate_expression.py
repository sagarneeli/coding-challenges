# Python3 program to evaluate a given 
# expression where tokens are 
# separated by space. 

# Function to find precedence 
# of operators. 
def precedence(op): 
	
	if op == '+' or op == '-': 
		return 1
	if op == '*' or op == '/': 
		return 2
	return 0

# Function to perform arithmetic 
# operations. 
def applyOp(a, b, op): 
	
	if op == '+': return a + b 
	if op == '-': return a - b 
	if op == '*': return a * b 
	if op == '/': return a // b 

# Function that returns value of 
# expression after evaluation. 
def evaluate(tokens): 
	
	# stack to store integer values. 
	values = [] 
	
	# stack to store operators. 
	ops = [] 
	i = 0
	
	while i < len(tokens): 
		
		# Current token is a whitespace, 
		# skip it. 
		if tokens[i] == ' ': 
			i += 1
			continue
		
		# Current token is an opening 
		# brace, push it to 'ops' 
		elif tokens[i] == '(': 
			ops.append(tokens[i]) 
		
		# Current token is a number, push 
		# it to stack for numbers. 
		elif tokens[i].isdigit(): 
			val = 0
			
			# There may be more than one 
			# digits in the number. 
			while (i < len(tokens) and tokens[i].isdigit()):
				val = (val * 10) + int(tokens[i]) 
				i += 1
			
			values.append(val) 
		
		# Closing brace encountered, 
		# solve entire brace. 
		elif tokens[i] == ')': 
		
			while len(ops) != 0 and ops[-1] != '(': 
			
				val2 = values.pop() 
				val1 = values.pop() 
				op = ops.pop() 
				
				values.append(applyOp(val1, val2, op)) 
			
			# pop opening brace. 
			ops.pop() 
		
		# Current token is an operator. 
		else: 
		
			# While top of 'ops' has same or 
			# greater precedence to current 
			# token, which is an operator. 
			# Apply operator on top of 'ops' 
			# to top two elements in values stack. 
			while (len(ops) != 0 and
				precedence(ops[-1]) >= precedence(tokens[i])): 
						
				val2 = values.pop() 
				val1 = values.pop() 
				op = ops.pop() 
				
				values.append(applyOp(val1, val2, op)) 
			
			# Push current token to 'ops'. 
			ops.append(tokens[i]) 
		
		i += 1
	
	# Entire expression has been parsed 
	# at this point, apply remaining ops 
	# to remaining values. 
	print(values)
	print(ops)
	while len(ops) != 0: 
		
		val2 = values.pop() 
		val1 = values.pop() 
		op = ops.pop() 
		print(val2)
		print(val1)
		print(ops)
		values.append(applyOp(val1, val2, op)) 
	
	# Top of 'values' contains result, 
	# return it. 
	return values[-1] 

# Driver Code 

	
# print(evaluate("10 + 2 * 6")) 
# print(evaluate("100 * 2 + 12")) 
print(evaluate("(1+(4+5+2)-3)+(6+8)")) 
# print(evaluate("3 + 2 * 2"))

# This code is contributed 
# by Rituraj Jain 