#!/usr/bin/env python3

#
# demo data is generated as a square (size x size) matrix (m)
# and two matrix (count x size) of data points, one
# of (size) elements per row as the input vector, 
# and the one of (size) elements per row as
# the output vector (output_vector = m.dot(input_vector))
#

import numpy as np

def create_square_matrix( size ):
    #             (rows,columns)
    m = np.zeros( (size,size), np.float32 )
    return m

DEMO_2_x_2_a = 1

def create_demo_matrix( which ):
    if which == DEMO_2_x_2_a:
        m = create_square_matrix( 2 )
        m[0,0] = 0.5
        m[0,1] = 0.25
        m[1,0] = -0.1
        m[1,1] = -0.3
    else:
        m = None
        raise Exception( "use a correct value for which" )
    return m

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

def create_demo( which, count ):
    m = create_demo_matrix( which )
    data = create_demo_data( m, count )
    return m, data

if __name__ == "__main__":
    m, data = create_demo( DEMO_2_x_2_a, 10 )
    print( m )
    print( data )
    


