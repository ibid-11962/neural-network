#!/usr/bin/env python3

import math

if __name__ == "__main__":
	netfile = input("name of neural network file: ")
	testfile = input("name of test set file: ")
	resfile = input("name of results file: ")

	f = open(netfile)
	[ni,nh,no]=[int(s) for s in f.readline().split(' ')]
	wh = []
	for _ in range(nh):
		wh.append([float(s) for s in f.readline().split(' ')])
	wo = []
	for _ in range(no):
		wo.append([float(s) for s in f.readline().split(' ')])
	f.close()
	
	f = open(testfile)
	[nt,ni,no]=[int(s) for s in f.readline().split(' ')]
	A = [0 for _ in range(no)]
	B = [0 for _ in range(no)]
	C = [0 for _ in range(no)]
	D = [0 for _ in range(no)]
	acc = [0 for _ in range(no)]
	pre = [0 for _ in range(no)]
	rec = [0 for _ in range(no)]
	for _ in range(nt):
		line = f.readline().split(' ')
		a1 = [float(s) for s in line[:ni]]
		y = [int(s) for s in line[ni:]]
		a2 = []
		for i in range(nh):
			a2.append(1/(1+math.exp(-sum(w*a for w,a in zip(wh[i],[-1]+a1)))))
		a3 = []
		for i in range(no):
			aj = 0 if 1/(1+math.exp(-sum(w*a for w,a in zip(wo[i],[-1]+a2)))) < 0.5 else 1 #round() doesn't work here because it rounds .5 to even.
			if aj and y[i]:
				A[i]+=1
			elif aj and not y[i]:
				B[i]+=1
			elif not aj and y[i]:
				C[i]+=1
			else:
				D[i]+=1
	f.close()
	
	TotAcc=TotPre=TotRec=0
	f = open(resfile,"wt")
	for i in range(no):
		acc = (A[i]+D[i])/(A[i]+B[i]+C[i]+D[i])
		pre = A[i]/(A[i]+B[i])
		rec = A[i]/(A[i]+C[i])
		f1 = (2*pre*rec)/(pre+rec)
		[TotAcc,TotPre,TotRec]=[i+j for i,j in zip([TotAcc,TotPre,TotRec],[acc,pre,rec])]
		f.write((" ".join(f'{metric}' for metric in [A[i],B[i],C[i],D[i]])+' '))
		f.write((" ".join(f'{metric:.3f}' for metric in [acc,pre,rec,f1])+'\n'))
	micacc = (sum(A)+sum(D))/(sum(A)+sum(B)+sum(C)+sum(D))
	micpre = sum(A)/(sum(A)+sum(B))
	micrec = sum(A)/(sum(A)+sum(C))
	micf1 = (2*micpre*micrec)/(micpre+micrec)
	f.write((" ".join(f'{metric:.3f}' for metric in [micacc,micpre,micrec,micf1])+'\n'))
	f.write((" ".join(f'{metric:.3f}' for metric in [TotAcc/no,TotPre/no,TotRec/no,(2*TotPre*TotRec/no)/(TotPre+TotRec)])+'\n'))
	f.close()