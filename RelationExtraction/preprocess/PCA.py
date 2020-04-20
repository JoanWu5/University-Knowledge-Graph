import numpy as np
from sklearn.decomposition import PCA

def main():
	nameList = []
	X = []
	with open('new_vector.txt', 'r',encoding='utf-8') as f:
		count = 0
		for line in f:
			arr = line.strip().split(' ')
			nameList.append(arr[0])
			X.append(arr[1:])
		# length = len(X[0])
		# for x1 in range(len(X)):
		# 	if length!=len(X[x1]):
		# 		print(x1)
	pca = PCA(n_components=50)
	newX = pca.fit_transform(X)
	print(pca.explained_variance_ratio_)  
	with open('new_vector_50.txt', 'w',encoding='utf-8') as f:
		for i in range(len(nameList)):
			f.write(str(nameList[i]))
			for p in newX[i]:
				f.write(' '+str(p).strip()[:7])
			f.write('\n')
			
main()