#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 10:45:36 2025

@author: hugoo
"""

import numpy as np

#qa
null_vector = np.zeros(10)
null_vector[4]=1

#qb
ranging_vector = np.arange(10,50,1)

#qc
reversed_vector = np.flip(ranging_vector)

#qd
firstvector=np.arange(0,3)
first_matrix = np.matrix([np.arange(0,3), np.arange(3,6), np.arange(6,9)])

#qe
v = np.array([1,2,0,0,4,0])
non_zero = np.array(np.where(v != 0))[0]

#qf
mean_of_rand = np.mean(np.random.random(30))

#qg
a=5
one_matrix = np.ones([a,a])
zero_matrix = np.zeros([a-2,a-2])
one_matrix[1:a-1,1:a-1]=zero_matrix
#print(one_matrix)

#qh
a=8
board = np.zeros([a,a])
index_sum=[]
for i in range(1,a+1):
    for j in range(1,a+1):
        index_sum.append(i+j)
decision_matrix = np.array(index_sum).reshape([a,a])
board[np.where(decision_matrix % 2 == 0)] = 1
#print(board)

#qi
first_row = np.array([[0,1,0,1,0,1,0,1]])
checkerboard = np.tile(np.concatenate((first_row, np.flip(first_row))), (4,1))
#print(checkerboard)

#qj
Z = np.arange(11)
negator = np.ones(11)
negator[2:9] = -1
Z = Z * negator
#print(Z)

#qk
Z = np.random.random(10)
Z = np.sort(Z)
#print(Z)

#ql
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = A==B
#print(equal)

#qm
Z = np.arange(10, dtype=np.int32)
#print(Z.dtype)
Z *= Z
#print(Z.dtype)

#qn
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D=np.diag(C)
#print(D)

