
def validator(txt):

	stack = []

	open_syms = {'{','[','('}
	close_syms = {'}':'{',']':'[', ')':'('}

	for c in txt:
		if c in open_syms:
			stack.append(c)

		elif c in close_syms:

			if not stack:
				return False

			k = stack.pop()

			if close_syms[c] != k:
				return False

	return not stack
