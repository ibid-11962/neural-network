#!/usr/bin/env python3

import math

if __name__ == "__main__":
	nnfile = input("name of initial neural network file: ")
	trainfile = input("name of training set file: ")
	outfile = input("name of output file: ")
	epochs = int(input("number of epochs: "))
	alpha = float(input("learning rate: "))

	f = open(nnfile)
	[ni,nh,no]=[int(s) for s in f.readline().split(' ')]
	wh = []
	for _ in range(nh):
		wh.append([float(s) for s in f.readline().split(' ')])
	wo = []
	for _ in range(no):
		wo.append([float(s) for s in f.readline().split(' ')])
	f.close()
	
	for _ in range(epochs):
		f = open(trainfile)
		[nt,ni,no]=[int(s) for s in f.readline().split(' ')]
		for _ in range(nt):
			line = f.readline().split(' ')
			a1 = [float(s) for s in line[:ni]]
			y = [int(s) for s in line[ni:]]
			a2 = []
			for i in range(nh):
				a2.append(1/(1+math.exp(-sum(w*a for w,a in zip(wh[i],[-1]+a1)))))
			del3 = []
			for i in range(no):
				aj = 1/(1+math.exp(-sum(w*a for w,a in zip(wo[i],[-1]+a2))))
				del3.append(aj*(1-aj)*(y[i]-aj))
			del2 = []
			for i in range(nh):
				aj = 1/(1+math.exp(-sum(w*a for w,a in zip(wh[i],[-1]+a1))))
				del2.append(aj*(1-aj)*sum(w*d for w,d in zip((j[i+1] for j in wo),del3)))
			wo = [[wi + alpha * ai * delj for wi,ai in zip(wj,[-1]+a2)] for wj,delj in zip(wo,del3)]
			wh = [[wi + alpha * ai * delj for wi,ai in zip(wj,[-1]+a1)] for wj,delj in zip(wh,del2)]
	f.close()
	
	f = open(outfile,"wt")
	f.write(str(ni)+' '+str(nh)+' '+str(no))
	for weights in wh:
		f.write('\n'+" ".join(f'{w:.3f}' for w in weights))
	for weights in wo:
		f.write('\n'+" ".join(f'{w:.3f}' for w in weights))
	f.write('\n')
	f.close()