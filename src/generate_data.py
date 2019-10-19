#!/usr/bin/env python3

import numpy as np

def create_square_matrix( size ):
    #             (rows,columns)
    m = np.zeros( (size,size), np.float32 )
    return m

DEMO_2_x_2_a = 1
DEMO_2_x_2_b = 2
DEMO_2_x_2_random = 99

DEMO_names = {
    DEMO_2_x_2_a: "DEMO_2_x_2_a",
    DEMO_2_x_2_b: "DEMO_2_x_2_b",
    DEMO_2_x_2_random: "DEMO_2_x_2_random",
}

def matrix_to_string( m0 ):
    s = ""
    for row in range( m0.shape[0] ):
        for col in range( m0.shape[1] ):
            if len(s) > 0:
                s += "."
            sv = str(m0[row,col])
            s += sv
    return s

#
# Generates a square matrices (size x size), either
# from predefined matrix values, or from random values.
#
# The matrix is a numpy.ndarray of shape = (size,size) of float32s
#
def create_demo_matrix( which ):
    if which == DEMO_2_x_2_a:
        m = create_square_matrix( 2 )
        m[0,0] = 0.5
        m[0,1] = 0.25
        m[1,0] = -0.1
        m[1,1] = -0.3
    elif which == DEMO_2_x_2_b:
        m = create_square_matrix( 2 )
        m[0,0] = 0.89
        m[0,1] = -0.21
        m[1,0] = -0.43
        m[1,1] = 0.35
    elif which == DEMO_2_x_2_random:
        m = create_square_matrix( 2 )
        m[0,0] = np.random.random( ) * 2.0 - 1.0
        m[0,1] = np.random.random( ) * 2.0 - 1.0
        m[1,0] = np.random.random( ) * 2.0 - 1.0
        m[1,1] = np.random.random( ) * 2.0 - 1.0
    else:
        m = None
        raise Exception( "use a correct value for which" )
    return m

#
# Creates data points by randomly choosing `series_count` input
# points with each coordinate in the range -1:1, and calculating
# a sequence of `series_size` output points using the `matrix`.
#
# Returns a python 2-tuple of numpy.ndarray objects.
# Each array has shape = (series_count,series_size,size), where `size`
# is the size of the square matrix and `series_count` is
# the number of sequences of data points requested, and `series_size`
# is the size of sequence requested.
#
# Each entry in the input array is an input point,
# and each entry in the output array is an output point.
#
def create_demo_series_data( matrix, series_count, series_size ):
    size = matrix.shape[0]
    input_data  = np.empty( (series_count, series_size, size), np.float32 )
    output_data = np.empty( (series_count, series_size, size), np.float32 )
    
    for i in range( series_count ):
        input_vector = np.random.random( size ) * 2.0 - 1.0
        for j in range( series_size ):
            output_vector = matrix.dot( input_vector )
            input_data[i,j,:] = input_vector
            output_data[i,j,:] = output_vector
            input_vector = output_vector
    return input_data, output_data

#
# Creates data points by randomly choosing `count` input
# points with each coordinate in the range -1:1, and calculating
# the corresponding output points using the `matrix`.
#
# Returns a python 2-tuple of numpy.ndarray objects.
# Each array has shape = (count,size), where `size`
# is the size of the square matrix and `count` is
# the number of data points requested.
#
# Each entry in the input array is an input point,
# and each entry in the output array is an output point.
#
# All data points are unrelated.
#
def create_demo_data( matrix, count ):
    size = matrix.shape[0]
    input_data  = np.empty( (count, size), np.float32 )
    output_data = np.empty( (count, size), np.float32 )
    
    for i in range( count ):
        input_vector = np.random.random( size ) * 2.0 - 1.0
        output_vector = matrix.dot( input_vector )
        input_data[i,:] = input_vector
        output_data[i,:] = output_vector
    return input_data, output_data

def create_demo_series( which, series_count, series_size ):
    m = create_demo_matrix( which )
    data = create_demo_series_data( m, series_count, series_size )
    return m, data

def create_demo( which, count ):
    m = create_demo_matrix( which )
    data = create_demo_data( m, count )
    return m, data

def main( ):
    m, data = create_demo( DEMO_2_x_2_a, 10 )
    print( m )
    print( data )
    return

def main2():
    matrix = create_demo_matrix( DEMO_2_x_2_a )
    series_count = 3
    series_size = 4
    data = create_demo_series_data( matrix, series_count, series_size )
    print(data)
    return

def main3():
    m, data = create_demo_series( DEMO_2_x_2_a, 4, 10 )
    print( m )
    print( data )
    return

if __name__ == "__main__":
    main3()


