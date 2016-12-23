#!/bin/python3

import sys

n,q = input().strip().split(' ')
n,q = [int(n),int(q)]
matrix = [[0 for x in range(1, n + 1, 1)] for y in range(1, n + 1, 1)]
#
# def compute_hackonacci(n):
#     hackonacci[1] = 1
#     hackonacci[2] = 2
#     hackonacci[3] = 3
#     for i in range(4,(n*n*n*n)+1,1):
#         hackonacci[i] = (1*hackonacci[i-1]) + (2*hackonacci[i-2]) + (3*hackonacci[i-3])
#
# def build_matrix(n):
#     compute_hackonacci(n)
#     for i in range(n):
#         for j in range(n):
#             term = ((i+1)*(i+1)*(j+1)*(j+1))
#             if hackonacci[term] %2 == 0:
#                 matrix[i][j] = 'X'
#             else:
#                 matrix[i][j] = 'Y'
#     print_matrix(n)
#     #return matrix

def build_matrix(n):
    hackonaci = ['Y','X','Y','X','X','Y','Y']
    for i in range(n):
        for j in range(n):
            term = ((i+1)*(i+1)*(j+1)*(j+1))
            ind = term % 7
            if ind == 0:
                matrix[i][j] = hackonaci[6]
            else:
                matrix[i][j] = hackonaci[ind-1]
    return matrix


def print_matrix(n):
    for i in range(n):
        for j in range(n):
            print((matrix[i][j]), end= " ")
        print("\n")

def rotate_matrix(m):
    MATRIX = []
    temp_matrix = m
    for times in range(1,5,1):
        new_matrix = [[0 for x in range(1, n + 1, 1)] for y in range(1, n + 1, 1)]
        for i in range(n):
            for j in range(n):
                new_matrix[j][(n-1)-i] = temp_matrix[i][j]
        temp_matrix = new_matrix
        MATRIX.append(diff_cells(m,new_matrix))
    return MATRIX

def diff_cells(m,rm):
    cells = 0
    for i in range(n):
        for j in range(n):
            if m[i][j] != rm[i][j]:
                cells += 1
    return cells


m = build_matrix(n)
rm = rotate_matrix(m)
#print_matrix(n)
#build_matrix(n)
for a0 in range(q):
    angle = int(input().strip())
    # your code goes here
    num = angle / 90
    print(rm[int(num % 4) - 1])
