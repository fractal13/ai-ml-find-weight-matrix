#!/usr/bin/env python3

import generate_data
import learn_matrix
import matplotlib.pyplot as plt

def get_column( data, i ):
    column = [ ]
    for row in data:
        column.append( row[i] )
    return column

def plot( plot_data, names, pdfname="" ):
    sp_rows = len( plot_data[0] ) - 1
    sp_cols = 1

    #plt.suptitle( "Super Title" )
    plt.figure( 1, figsize=(6.5, 9) )
    X = get_column( plot_data, 0 )
    x_name = names[0]
    for i in range( 1, len(plot_data[0]) ):
        y_name = names[i]
        plt.subplot( sp_rows, sp_cols, i )
        Y = get_column( plot_data, i )
        plt.xscale( "log" )
        plt.scatter( X, Y, s=1, color='blue' )
        #plt.bar( X, Y, color='blue' )
        #plt.plot( X, Y, color='blue' )
        plt.ylabel( y_name )
        plt.xlabel( x_name )
        plt.locator_params( axis='both', tight=True )
        
    plt.tight_layout( )
    if pdfname:
        plt.savefig( pdfname )
    else:
        plt.show( )
    return

def main():
    counts = [ 10, 20, 40, 100, 200, 400, 1000, 2000, 4000, 10000 ]
    repeats = 10
    #counts = [ 10, 20, 40, 100, 200, 400 ]
    plot_data = []
    plot_names = [ "Data Size", "Loss", "Prediction MAE", "Matrix MAE" ]
    for count in counts:
        for i in range(repeats):
            m0, data = generate_data.create_demo( generate_data.DEMO_2_x_2_a, count )
            results = learn_matrix.fit_and_evaluate( m0, data )
            plot_data.append( [ count ] + results )

    print( plot_data, plot_names )
    plot( plot_data, plot_names, "FitQualityVsDataSize.pdf" )
    return

if __name__ == "__main__":
    main()
    
