'''Tchisla solver'''
'''Developed by Tianyi Feng'''

import math
import numpy as np

#############################################

MAXNUM = 20
RANGE = 1000

def _factorial(column, factor):
	res = []

	fac = int(math.factorial(factor))
	if fac < RANGE:
		res.append(fac)
		res += _sqrt(column, fac)
	
	return res

def _sqrt(column, factor):
	res = []

	while factor > 1 and isSqrt(factor):
		r = int(math.sqrt(factor))
		res.append(r)
		res += _factorial(column, r)
		factor = r

	return res

def isSqrt(num):
	r = int(math.sqrt(num))

	return (r*r == num)

def _freak(factor, num):
	res=[]
	
	f = int("1"*num)*factor
	if f < RANGE:
		res.append(f)

	return res

def _sum(column, factor, fst, sec):
	res = []

	s = int(fst+sec)
	if s < RANGE:
		res.append(s)
		res += _factorial(column, s)
		res += _sqrt(column, s)

	return res

def _prod(column, factor, fst, sec):
	res = []

	p = int(fst*sec)
	if p < RANGE:
		res.append(p)
		res += _factorial(column, p)
		res += _sqrt(column, p)

	return res

def _diff(column, factor, fst, sec):
	res = []

	d = int(fst-sec)
	if d >= 1 and d < RANGE:
		res.append(d)
		res += _factorial(column, d)
		res += _sqrt(column, d)

	return res

def _quot(column, factor, fst, sec):
	res = []

	if fst%sec != 0:
		return res

	q = int(fst/sec)
	if q >= 1 and q < RANGE:
		res.append(q)
		res += _factorial(column, q)
		res += _sqrt(column, q)

	return res

def _pow(column, factor, base, exp):
	res = []

	if base > 1 and exp > math.log(RANGE, base):
		return res

	pw = int(math.pow(base, exp))
	if pw < RANGE:
		res.append(pw)
		res += _factorial(column, pw)
		res += _sqrt(column, pw)

	return res

def computeGallery(gallery, factor):
	targets = {}

	column = gallery[:,factor-1]

	targets[1] = set()
	targets[1].add(factor)
	targets[1].update(_factorial(column, factor))
	targets[1].update(_sqrt(column, factor))

	for target in targets[1]:
		if target <= MAXNUM:
			gallery[target-1][factor-1] = 1

	num = 2
	while num <= MAXNUM:
		targets[num] = set()
		targets[num].update(_freak(factor, num))
		for i in range(1, num/2+1):
			for j in targets[i]:
				for k in targets[num-i]:
					targets[num].update(_sum(column, factor, j, k))
					targets[num].update(_prod(column, factor, j, k))
					if j >= k:
						targets[num].update(_diff(column, factor, j, k))
						targets[num].update(_quot(column, factor, j, k))
					else:
						targets[num].update(_diff(column, factor, k, j))
						targets[num].update(_quot(column, factor, k, j))
					targets[num].update(_pow(column, factor, j, k))
					targets[num].update(_pow(column, factor, k, j))
					
		for target in targets[num]:
			if target <= MAXNUM and gallery[target-1][factor-1] == 0:
				gallery[target-1][factor-1] = num

		num += 1

	return 

def showGallery():
	gallery = np.zeros((MAXNUM,9))

	factors = [1, 2, 3, 4, 5, 6, 7, 8, 9]

	# compute the gallery 
	for factor in factors:
		computeGallery(gallery, factor)

	print "----------Tchisla Gallery----------"
	print gallery

if __name__ == "__main__":
	showGallery()

