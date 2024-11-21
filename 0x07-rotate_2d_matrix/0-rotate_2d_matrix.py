#!/usr/bin/python3
'''
Rotate 2D Matrix
'''


def rotate_2d_matrix(matrix):
    '''
    Rotate two dimension matrix 90 degrees clockwise
    
    
    Args:
        matrix (list[[list]]): a matrix
    '''
    n = len(matrix)
    for layer in range(int(n / 2)):
        end = (n - layer - 1)
        for i in range(layer, end):
            offset = (n - 1 - i)
            tmp = matrix[layer][i]
            matrix[layer][i] = matrix[offset][layer]
            matrix[offset][layer] = matrix[end][offset]
            matrix[end][offset] = matrix[i][end]
            matrix[i][end] = tmp
