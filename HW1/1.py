import numpy as np

if __name__ == "__main__":
	A = np.array([[1, 2, 3], [2, 1, 4]])
	B =	np.array([[1, 0], [2, 1], [3, 2]])
	C = np.array([[3, -1, 3], [4, 1, 5], [2, 1, 3]])
	D = np.array([[2, -4, 5],[0, 1, 4],[3, 2, 1]])
	E = np.array([[3, -2],[2, 4]])
	
	subproblems = [
			["a)", "(2 * A).T"],
			["b)", "(A - B).T"],
			["c)", "(3 * B.T - A).T"],
			["d)", "(-1 * A).T * E"],
			["e)", "(C + 2 * D.T + E).T"]
		]
	
	for index, expression in subproblems:
		try:
			print(index)
			print(eval(expression))
		except ValueError:
			print("Not possible")
		except:
			print("Error in program")
		print()
