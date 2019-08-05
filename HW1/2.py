import numpy as np

if __name__ == "__main__":
	A = np.array([[1, 4], [3, 2]])
	B = np.array([[2, -1], [-3, 4]])
	
	AB = np.matmul(A, B)
	BA = np.matmul(B, A)

	if np.array_equal(AB, BA):
		print("AB == BA")
	else:
		print("AB != BA")
	print()
	print("AB:")
	print(AB)
	print()
	print("BA:")
	print(BA)
