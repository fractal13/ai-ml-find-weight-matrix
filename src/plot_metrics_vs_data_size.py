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

    plt.clf()
    return

def plot_all( all_plot_data, names, pdfname="", labels=[] ):
    sp_rows = len( all_plot_data[0][0] ) - 1
    sp_cols = 1
    colors = [ "blue", "red", "green" ]
    fmts = [ "ob", "vg", "^r", "<c", ">m" ]

    #plt.suptitle( "Super Title" )
    plt.figure( 1, figsize=(6.5, 9) )

    for i in range( 1, len(all_plot_data[0][0]) ):
        x_name = names[0]
        y_name = names[i]
        ax = plt.subplot( sp_rows, sp_cols, i )

        plt.xscale( "log" )
        plt.ylabel( y_name )
        plt.xlabel( x_name )
        plt.locator_params( axis='both', tight=True )
        
        for j in range(len(all_plot_data)):
            if j >= len(labels):
                label = str(j)
            else:
                label = labels[j]
            plot_data = all_plot_data[j]
            color = colors[j%(len(colors))]
            fmt = fmts[j%(len(fmts))]
            X = get_column( plot_data, 0 )
            Y = get_column( plot_data, i )
            #plt.scatter( X, Y, s=1, color=color )
            #plt.bar( X, Y, color='blue' )
            plt.plot( X, Y, fmt, label=label )
        plt.legend()
    
    # for j in range(len(all_plot_data)):
    #     plot_data = all_plot_data[j]
    #     color = colors[j%(len(colors))]
    #     fmt = fmts[j%(len(fmts))]
    #     X = get_column( plot_data, 0 )
    #     x_name = names[0]
    #     for i in range( 1, len(plot_data[0]) ):
    #         y_name = names[i]
    #         ax = plt.subplot( sp_rows, sp_cols, i )
    #         Y = get_column( plot_data, i )
    #         if j == 0:
    #             plt.xscale( "log" )
    #             plt.ylabel( y_name )
    #             plt.xlabel( x_name )
    #             plt.locator_params( axis='both', tight=True )
    #         #plt.scatter( X, Y, s=1, color=color )
    #         #plt.bar( X, Y, color='blue' )
    #         plt.plot( X, Y, fmt )

    
    plt.tight_layout( )
    if pdfname:
        plt.savefig( pdfname )
    else:
        plt.show( )

    plt.clf()
    return

def make_a_demo_plot( which ):
    #counts = [ 10, 20, 40, 100, 200, 400, 1000, 2000, 4000, 10000 ]
    #repeats = 10
    counts = [  10, 20, 40, 100, 200, 400, 1000, 2000, 4000, 10000, 20000, 40000, 100000, 200000, 400000, 1000000 ]
    repeats = 1
    #counts = [ 10, 20, 40, 100, 200, 400 ]
    #counts = [ 10, 20, 40 ]
    plot_data = []
    plot_names = [ "Data Size", "Loss", "Prediction MAE", "Matrix MAE" ]
    params = { 'epochs': 10 }

    m0 = generate_data.create_demo_matrix( which )
    for count in counts:
        for i in range(repeats):
            data = generate_data.create_demo_data( m0, count )
            results = learn_matrix.fit_and_evaluate( m0, data, params )
            plot_data.append( [ count ] + results )

    print( plot_data, plot_names )
    ms = generate_data.matrix_to_string( m0 )
    file_name = "FitQualityVsDataSize" + str( generate_data.DEMO_names[ which ] ) + "." + ms + ".pdf"
    plot( plot_data, plot_names, file_name )
    return

def make_a_series_demo_plot( which ):
    #counts = [  10, 20, 40, 100, 200, 400, 1000, 2000, 4000, 10000 ]
    counts = [  10, 20, 40, 100, 200, 400, 1000, 2000, 4000, 10000, 20000, 40000, 100000, 200000, 400000, 1000000 ]
    series_size = 100
    repeats = 1
    #repeats = 10
    #counts = [ 10, 20, 40, 100, 200, 400 ]
    #counts = [ 10, 20, 40 ]
    plot_data = []
    plot_names = [ "Data Size", "Loss", "Prediction MAE", "Matrix MAE" ]
    params = { 'epochs': 10 }
    m0 = generate_data.create_demo_matrix( which )
    for count in counts:
        series_count = int( count / series_size )
        if series_count < 10:
            continue
        for i in range(repeats):
            data = generate_data.create_demo_data( m0, count )
            results = learn_matrix.fit_and_evaluate( m0, data, params )
            plot_data.append( [ count ] + results )

    print( plot_data, plot_names )
    ms = generate_data.matrix_to_string( m0 )
    file_name = "FitQualityVsDataSizeSeries" + str( generate_data.DEMO_names[ which ] ) + "." + ms + ".pdf"
    plot( plot_data, plot_names, file_name )
    return

def make_a_demo_plot_from_list( which_ones ):
    #counts = [ 10, 20, 40, 100, 200, 400, 1000, 2000, 4000, 10000 ]
    #repeats = 10
    counts = [  10, 20, 40, 100, 200, 400, 1000, 2000, 4000, 10000, 20000, 40000, 100000, 200000, 400000, 1000000 ]
    counts = [  10, 20, 40, 100, 200, 400, 1000 ]
    repeats = 1
    #counts = [ 10, 20, 40, 100, 200, 400 ]
    #counts = [ 10, 20, 40 ]
    all_plot_data = []
    all_ms = ""
    plot_names = [ "Data Size", "Loss", "Prediction MAE", "Matrix MAE" ]
    params = { 'epochs': 10 }
    
    for which in which_ones:
        plot_data = []
        m0 = generate_data.create_demo_matrix( which )
        for count in counts:
            for i in range(repeats):
                data = generate_data.create_demo_data( m0, count )
                results = learn_matrix.fit_and_evaluate( m0, data, params )
                plot_data.append( [ count ] + results )
        ms = generate_data.matrix_to_string( m0 )
        all_plot_data.append( plot_data )
        if len(all_ms) > 0:
            all_ms += ":"
        all_ms += str( generate_data.DEMO_names[ which ] ) + "." + ms

    file_name = "FitQualityVsDataSize" + all_ms + ".pdf"
    plot_all( all_plot_data, plot_names, file_name )
    return

def make_a_demo_plot_from_param_list( which, params_list ):
    #counts = [ 10, 20, 40, 100, 200, 400, 1000, 2000, 4000, 10000 ]
    #repeats = 10
    counts = [  10, 20, 40, 100, 200, 400, 1000, 2000, 4000, 10000, 20000, 40000, 100000, 200000, 400000, 1000000 ]
    counts = [  10, 20, 40, 100, 200, 400, 1000 ]
    repeats = 1
    #counts = [ 10, 20, 40, 100, 200, 400 ]
    #counts = [ 10, 20, 40 ]
    all_plot_data = []
    all_ms = ""
    plot_names = [ "Data Size", "Loss", "Prediction MAE", "Matrix MAE" ]
    labels = []
    for params in params_list:
        plot_data = []
        m0 = generate_data.create_demo_matrix( which )
        for count in counts:
            for i in range(repeats):
                data = generate_data.create_demo_data( m0, count )
                results = learn_matrix.fit_and_evaluate( m0, data, params )
                plot_data.append( [ count ] + results )
        ms = generate_data.matrix_to_string( m0 )
        all_plot_data.append( plot_data )
        # if len(all_ms) > 0:
        #     all_ms += ":"
        all_ms = str( generate_data.DEMO_names[ which ] ) + "." + ms
        label = "e"+str( params['epochs'] )
        labels.append(label)

    file_name = "FitQualityVsParams" + all_ms + ".pdf"
    plot_all( all_plot_data, plot_names, file_name, labels )
    return

def main():

    param_list = [ { 'epochs': 2 }, { 'epochs': 4 }, { 'epochs': 8 },  { 'epochs': 10 },
                   { 'epochs': 20 }, { 'epochs': 40 }, { 'epochs': 80 }, { 'epochs': 100 } ]
    make_a_demo_plot_from_param_list( generate_data.DEMO_2_x_2_random, param_list )

    #make_a_demo_plot_from_list( [ generate_data.DEMO_2_x_2_random, generate_data.DEMO_2_x_2_a, generate_data.DEMO_2_x_2_b ] )
    # make_a_demo_plot( generate_data.DEMO_2_x_2_random )
    # make_a_demo_plot( generate_data.DEMO_2_x_2_a )
    # make_a_demo_plot( generate_data.DEMO_2_x_2_b )
    return

def main2():
    make_a_series_demo_plot( generate_data.DEMO_2_x_2_random )
    make_a_series_demo_plot( generate_data.DEMO_2_x_2_a )
    make_a_series_demo_plot( generate_data.DEMO_2_x_2_b )
    return

if __name__ == "__main__":
    main()

    
