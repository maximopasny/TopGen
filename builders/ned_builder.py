f = open('attempt.ned', 'w')
f.write('simple my_net_element\n' +
        '{\n' +
        '\tparameters\n' +
        '\t\t@display("i=block/routing");\n' +
        '\t\tint vertex_color;\n' +
        '\t\tint x_coord;\n' +
        '\t\tint y_coord;\n' +
        '\tgates\n' +
        '\t\tinout gate[];\n' +
        '}\n')

