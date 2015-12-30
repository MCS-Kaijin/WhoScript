#!/usr/bin/env python

import re
import sys
import math

code = ''
with open(sys.argv[1], 'r') as f:
	code = f.read().strip()

stdin = ''
is_stdin = False
try:
	stdin = ' '.join(sys.argv[2::])
	is_stdin = len(sys.argv) >= 3
except:
	pass

stack = []
tmpv = []
tmpp = []
tmp = []
if not code:
	print 'Reverse the polarity of the neutron flow!'
	sys.exit(1)
if not code[0] == '1':
	tmp = re.findall((r'@.+'), code)
	for occurrence in tmp:
		code = code.replace(occurrence, '')
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
			val2, val1 = float(stack.pop()), float(stack.pop())
			stack.append(val1+val2)
		elif line[0] == '-':
			val2, val1 = float(stack.pop()), float(stack.pop())
			stack.append(val1-val2)
		elif line[0] == '*':
			val2, val1 = float(stack.pop()), float(stack.pop())
			stack.append(val1*val2)
		elif line[0] == '/':
			val2, val1 = float(stack.pop()), float(stack.pop())
			stack.append(val1/val2)
		elif line[0] == '^':
			val2, val1 = float(stack.pop()), float(stack.pop())
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
		elif line[0] == 'truncate':
			stack.append(math.floor(stack.pop()))
		elif line[0] == 'integer':
			stack.append(int(stack.pop()))
		elif line[0] == 'switch':
			val1, val2 = stack.pop(), stack.pop()
			stack.append(val1)
			stack.append(val2)
		elif line[0] == 'pop':
			tmp.append(stack.pop())
		elif line[0] == 'push':
			stack.append(tmp.pop())
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
					while not 'TARDIS else' in code.split('\n')[i] and not 'TARDIS landing' in code.split('\n')[i]: i += 1
			elif line[1] == 'else':
				if stack.pop():
					while not 'TARDIS landing' in code.split('\n')[i] and not 'TARDIS if' in code.split('\n')[i]: i += 1
		elif line[0] == 'psychic_paper':
			if line[1] == 'write':
				if line[~0] == '#': sys.stdout.write(str(stack.pop()))
				else: sys.stdout.write(chr(stack.pop()))
			elif line[1] == 'read':
				try:
					if line[~0] == '#':
						if not stdin and not is_stdin:
							stack.append(int(raw_input('>>> ').strip(), 16))
						else:
							stack.append(int(stdin[0]+stdin[1], 16))
							stdin = stdin[2::]
					else:
						if not stdin and not is_stdin:
							stack.append(ord(raw_input('>>> ').strip()[0]))
						else:
							stack.append(ord(stdin[0]))
							stdin = stdin[1::]
				except IndexError as e:
					stack.append(-1)
			elif line[1] == 'flush':
				if line[~0] == '#': sys.stdout.write(' '.join(map(str, stack)))
				else: sys.stdout.write(''.join(map(chr, stack)))
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
			val2, val1 = float(stack.pop()), float(stack.pop())
			stack.append(val1+val2)
		elif line[0] == '-':
			val2, val1 = float(stack.pop()), float(stack.pop())
			stack.append(val1-val2)
		elif line[0] == '*':
			val2, val1 = float(stack.pop()), float(stack.pop())
			stack.append(val1*val2)
		elif line[0] == '/':
			val2, val1 = float(stack.pop()), float(stack.pop())
			stack.append(val1/val2)
		elif line[0] == '^':
			val2, val1 = float(stack.pop()), float(stack.pop())
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
		elif line[0] == 'c':
			stack.append(math.floor(stack.pop()))
		elif line[0] == 'i':
			stack.append(int(stack.pop()))
		elif line[0] == 'w':
			val1, val2 = stack.pop(), stack.pop()
			stack.append(val1)
			stack.append(val2)
		elif line[0] == '>':
			tmp.append(stack.pop())
		elif line[0] == '<':
			stack.append(tmp.pop())
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
					while not code[i] == 'tl' and not code[i] == 'te': i += 1
			elif line[0] == 'e':
				if stack.pop():
					while not code[i] == 'tl' and not code[i] == 'ti': i += 1
		elif line[0] == 'p':
			line = line[1::].split(' ')
			if line[0] == 'w':
				try:
					line[1]
					sys.stdout.write(str(stack.pop()))
				except:
					sys.stdout.write(chr(stack.pop()))
			elif line[0] == 'r':
				try:
					try:
						line[1]
						if not stdin and not is_stdin:
							stack.append(int(raw_input('>>> ').strip(), 16))
						else:
							stack.append(int(stdin[0]+stdin[1], 16))
							stdin = stdin[2::]
					except:
						if not stdin and not is_stdin:
							stack.append(ord(raw_input('>>> ').strip()[0]))
						else:
							stack.append(ord(stdin[0]))
							stdin = stdin[1::]
				except IndexError as e:
					stack.append(-1)
			elif line[0] == 'f':
				try:
					line[1]
					sys.stdout.write(' '.join(map(str, stack)))
				except:
					sys.stdout.write(''.join(map(chr, stack)))
		i += 1
