#!/usr/bin/env python3
import sys
import numpy as np
import tensorflow as tf
import tensorflow.keras as keras
import generate_data

def create_square_matrix( size ):
    activation = "linear"
    model = keras.models.Sequential( )
    model.add( keras.layers.Dense( size, activation=activation, input_shape=(size,) ) )

    # model.add( keras.layers.InputLayer( batch_input_shape=(1, size) ) )
    # for i in range( size ):
    #     model.add( keras.layers.Dense( size, activation=activation ) )
    # model.add( keras.layers.Dense( size, activation="linear" ) )
    model.compile( loss="mse",
                   optimizer="adam",
                   metrics=[ "mae" ] )
    return model

def fit_model( model, input_data, output_data ):
    model.fit( x=input_data, y=output_data, epochs=10, verbose=0 )
    return

def evaluate_model( model, input_data, output_data ):
    results = model.evaluate( input_data, output_data )
    return results

def matrix_vs_model_mean_absolute_error( m0, model ):
    total = 0.0

    w =  model.layers[0].get_weights()[0]
    for row in range(w.shape[1]):
        for col in range(w.shape[0]):
            dw = abs(w[col][row] - m0[row][col])
            total += dw
            
    count = w.shape[0]*w.shape[1]
    mae = total/count
    return mae

def fit_and_evaluate( m0, data ):
    count = data[0].shape[0]
    if data[1].shape[0] != count:
        raise Exception( "data sizes don't match!" )

    train_count = int( 0.80*count )
    train_data = data[0][:train_count], data[1][:train_count]
    test_data = data[0][train_count:], data[1][train_count:]

    model = create_square_matrix( m0.shape[0] )
    
    fit_model( model, train_data[0], train_data[1] )
    results = evaluate_model( model, test_data[0], test_data[1] )
    matrix_error = matrix_vs_model_mean_absolute_error( m0, model )
    return results + [ matrix_error ]

if __name__ == "__main__":

    count = 10000
    m0, data = generate_data.create_demo( generate_data.DEMO_2_x_2_a, count )
    results = fit_and_evaluate( m0, data )
    print( results )
    sys.exit(0)
    # train_data = data[0][:8000], data[1][:8000]
    # test_data = data[0][8000:], data[1][8000:]


    # model = create_square_matrix( 2 )
    # print( model )
    # print( model.layers )
    # for layer in model.layers:
    #     print( layer.get_weights() )
    # print( model.inputs )
    # print( model.outputs )
    
    # fit_model( model, train_data[0], train_data[1] )

    # print( "----------------------------------------" )
    # print( model )
    # print( model.layers )
    # for layer in model.layers:
    #     l = layer.get_weights()
    #     w = l[0]
    #     print( w.shape )
    #     print( w )
    #     for row in range(w.shape[1]):
    #         s = ""
    #         for col in range(w.shape[0]):
    #             s += str(w[col][row])
    #             s += ", "
    #         print( s )
        
    # print( model.inputs )
    # print( model.outputs )
    
    # #test_results = model.evaluate( test_data[0], test_data[1] )
    # print( )
    # print( evaluate_model( model, test_data[0], test_data[1] ) )
    # print( )
    # print( )
    # print( m0 )
    # print( )
    
    # print( "----------------------------------------" )
    # a = np.array( [[1,0],[0,1],[1,1],[0,0]] )
    # print( a )
    # print( model.predict( a ) )
    # print( "----------------------------------------" )
