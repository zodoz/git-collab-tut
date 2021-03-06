#!/usr/bin/python

import sys, re, string

# solves the stack iteratively
def solver(stack):
	nums = []
	item = stack.pop()
	while item:
		if re.match("\\d",item):
			nums.append(string.atoi(item))
		elif item == "+":
			nums.append(
					add(
						nums.pop(),
						nums.pop()
						)
					)
		elif item == "-":
			nums.append(
					subtract(
						nums.pop(),
						nums.pop()
						)
					)
		elif item == "*":
			nums.append(
					multiply(
						nums.pop(),
						nums.pop()
						)
					)
		elif item == "/":
			nums.append(
					divide(
						nums.pop(),
						nums.pop()
						)
					)
		elif item == "^":
			nums.append(
					exponent(
						nums.pop(),
						nums.pop()
						)
					)
		if len(stack)>0:
			item = stack.pop()
		else:
			item = False
	return nums.pop()

# adds left to right
def add(left,right):
	return left+right

# subtracts left from right
def subtract(left,right):
	return left-right

# multiplies left and right
def multiply(left,right):
	return left*right

# divides left by right
def divide(left,right):
	return left/right

# exponents left by right
def exponent(left,right):
	return left**right

# recursive function to find the mathstack from a valid math expression
def toStack(input, stack=[]): # stack starts as an integer array
	if input == "":  #base case
		return stack
	c = input[0]
	# if input[0] is a number
	if re.match("\\d",input):
		iNonNum = re.search("[+\\-*/^\\[\\]()]",input)
		if iNonNum:  #did we get any match?
			iNonNum = iNonNum.start()
			if re.match("[+\\-*^/]",input[iNonNum]):
				stack.append(input[iNonNum])
		else:        #no? then this number should be the last entry
			iNonNum = len(input)
		stack.append(input[:iNonNum])
		return toStack(input[iNonNum+1:],stack)
	# handle parentheses and brackets
	if re.match("[(\\[]",input):
		iParen = matchParen(input)
		if len(input)-1>iParen and re.match("[+\\-*^/]",input[iParen+1]):
			stack.append(input[iParen+1])
		return toStack(input[1:iParen],
				toStack(input[iParen+2:],stack))
	else:
		raise "error!!!"

# matches parentheses
def matchParen(input):
	depth = 1
	index = 1
	matches = input[0]
	while depth > 0:
		c = input[index]
		if c == "(" or c == "[":
			depth += 1
			matches += input[index]
		elif c == ")" or c == "]":
			m = matches[len(matches)-1]
			if c == ")" and m != "(":
				raise "paren error"
			elif c == "]" and m != "[":
				raise "bracket error"
			depth -= 1
			matches = matches[:len(matches)-1]
		index += 1
	return index-1

# gets the input until "exit"
def getInput():
	input = ""
	while True:
		sys.stdout.write("Enter some math> ")
		input = sys.stdin.readline()
		input.replace(" ","")                  #remove all white space
		input.replace("\n","")                 #remove new line charater
		if input.startswith("exit"):
			return
		mathstack = toStack(input,[])
		result = solver(mathstack)
		print result

getInput()
