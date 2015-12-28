import re
import sys

code = ''
with open(sys.argv[1], 'r') as f:
	code = f.read().strip()

stack = []
tmpv = []
tmpp = []
out = ''
if not code:
	print 'Reverse the polarity of the neutron flow!'
	raise KeyboardInterrupt
if not code[0] == '1':
	i = 0
	while i < len(code.split('\n')):
		line = re.findall((r'[\w#@+*/\^!&|=<>-]+'), code.split('\n')[i])
		if not line: line = '@'
		if line[0] == '#':
			for word in line:
				try:
					word = int(word, 16)
					stack.append(word)
				except:
					if word == '@': break
		elif line[0] == '@':
			pass
		elif line[0] == '+':
			val2, val1 = stack.pop(), stack.pop()
			stack.append(val1+val2)
		elif line[0] == '-':
			val2, val1 = stack.pop(), stack.pop()
			stack.append(val1-val2)
		elif line[0] == '*':
			val2, val1 = stack.pop(), stack.pop()
			stack.append(val1*val2)
		elif line[0] == '/':
			val2, val1 = stack.pop(), stack.pop()
			stack.append(val1/val2)
		elif line[0] == '^':
			val2, val1 = stack.pop(), stack.pop()
			stack.append(val1**val2)
		elif line[0] == '!':
			stack.append(~stack.pop())
		elif line[0] == '&':
			val2, val1 = stack.pop(), stack.pop()
			stack.append(val1&val2)
		elif line[0] == '|':
			val2, val1 = stack.pop(), stack.pop()
			stack.append(val1|val2)
		elif line[0] == 'x':
			val2, val1 = stack.pop(), stack.pop()
			stack.append(val1^val2)
		elif line[0] == 'duplicate':
			stack.append(stack[~0])
		elif line[0] == 'time_vortex':
			tmpv.append(i)
		elif line[0] == 'paradox':
			i = tmpv.pop()-1
		elif line[0] == 'opening':
			while not 'paradox' in code.split('\n')[i]: i += 1
		elif line[0] == 'TARDIS':
			if line[1] == '_':
				i = tmp.pop()
			elif line[1] == '=':
				val2, val1 = stack.pop(), stack.pop()
				if val1 == val2: stack.append(1)
				else: stack.append(0)
			elif line[1] == '<':
				val2, val1 = stack.pop(), stack.pop()
				if val1 < val2: stack.append(1)
				else: stack.append(0)
			elif line[1] == '>':
				val2, val1 = stack.pop(), stack.pop()
				if val1 > val2: stack.append(1)
				else: stack.append(0)
			elif line[1] == 'if':
				if not stack.pop():
					while not 'TARDIS landing' in code.split('\n')[i] or 'TARDIS else' in code.split('\n')[i]: i += 1
				break
			elif line[1] == 'else':
				if stack.pop():
					while 'TARDIS landing' in code.split('\n')[i] or 'TARDIS if' in code.split('\n')[i]: i += 1
				break
		elif line[0] == 'psychic_paper':
			if line[1] == 'write':
				if line[len(line)-1] == '#': out += str(stack.pop())
				else: out += chr(stack.pop())
			elif line[1] == 'read':
				if line[len(line)-1] == '#': stack.append(int(raw_input('>>> ').strip(), 16))
				else: stack.append(ord(raw_input('>>> ').strip()[0]))
			elif line[1] == 'flush':
				if line[len(line)-1] == '#': out += ' '.join(stack)
				else: out += ''.join(map(chr, stack))
		i += 1
else:
	tmp = re.findall((r'"[^"]+"'), code)
	if tmp:
		for occurrence in tmp:
			string = occurrence.replace('"', '')
			vals = map(hex, map(ord, list(string)))
			for i in range(0, len(vals)):
				vals[i] = vals[i][2::]
			code = code.replace(occurrence, '#'+' '.join(vals))
	code = code[1::].split(';')
	i = 0
	while i < len(code):
		line = code[i]
		if line[0] == '#':
			line = line[1::].split(' ')
			for val in line:
				stack.append(int(val, 16))
		elif line[0] == '+':
			val2, val1 = stack.pop(), stack.pop()
			stack.append(val1+val2)
		elif line[0] == '-':
			val2, val1 = stack.pop(), stack.pop()
			stack.append(val1-val2)
		elif line[0] == '*':
			val2, val1 = stack.pop(), stack.pop()
			stack.append(val1*val2)
		elif line[0] == '/':
			val2, val1 = stack.pop(), stack.pop()
			stack.append(val1/val2)
		elif line[0] == '^':
			val2, val1 = stack.pop(), stack.pop()
			stack.append(val1**val2)
		elif line[0] == '!':
			stack.append(~stack.pop())
		elif line[0] == '&':
			val2, val1 = stack.pop(), stack.pop()
			stack.append(val1&val2)
		elif line[0] == '|':
			val2, val1 = stack.pop(), stack.pop()
			stack.append(val1|val2)
		elif line[0] == 'x':
			val2, val1 = stack.pop(), stack.pop()
			stack.append(val1^val2)
		elif line[0] == 'e':
			stack.append(stack[~0])
		elif line[0] == 'v':
			tmpv.append(i)
		elif line[0] == 'd':
			i = tmpv.pop()-1
		elif line[0] == 'o':
			while not code[i] == 'd': i += 1
		elif line[0] == 't':
			line = line[1::]
			if line[0] == '=':
				val2, val1 = stack.pop(), stack.pop()
				if val1 == val2: stack.append(1)
				else: stack.append(0)
			elif line[0] == '<':
				val2, val1 = stack.pop(), stack.pop()
				if val1 < val2: stack.append(1)
				else: stack.append(0)
			elif line[0] == '>':
				val2, val1 = stack.pop(), stack.pop()
				if val1 > val2: stack.append(1)
				else: stack.append(0)
			elif line[0] == 'i':
				if not stack.pop():
					while not code[i] == 'tl' or code[i] == 'te': i += 1
				break
			elif line[0] == 'e':
				if stack.pop():
					while not code[i] == 'tl' or code[i] == 'ti': i += 1
				break
		elif line[0] == 'p':
			line = line[1::].split(' ')
			if line[0] == 'w':
				try:
					line[1]
					out += str(stack.pop())
				except:
					out += chr(stack.pop())
			elif line[0] == 'r':
				try:
					line[1]
					stack.append(int(raw_input('>>> ').strip(), 16))
				except:
					stack.append(ord(raw_input('>>> ').strip()[0]))
			elif line[0] == 'f':
				try:
					line[1]
					out += ' '.join(stack)
				except:
					out += ''.join(map(chr, stack))
		i += 1

print out
