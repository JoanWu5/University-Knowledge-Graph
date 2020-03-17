import numpy as np
from sklearn.decomposition import PCA

def main():
	nameList = []
	X = []
	with open('vector.txt', 'r',encoding='utf-8') as f:
		for line in f.readlines():
			arr = line.strip().split(' ')
			nameList.append(arr[0])
			X.append(arr[1:])
	pca = PCA(n_components=15)
	newX = pca.fit_transform(X)
	print(pca.explained_variance_ratio_)  
	with open('vector_15_1.txt', 'w',encoding='utf-8') as f:
		for i in range(len(nameList)):
			f.write(str(nameList[i]))
			for p in newX[i]:
				f.write(' '+str(p).strip()[:7])
			f.write('\n')
			
main()