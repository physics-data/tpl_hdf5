#!/usr/bin/python3
# -*- coding: utf-8 -*-

import h5py
import sys
import numpy as np

# sys.argv[1] is input file
# sys.argv[2] is output file
input_file = h5py.File(sys.argv[1], 'r')
output_file = h5py.File(sys.argv[2], 'w')

# TODO: access group named "/PPHappy"

# TODO: access dataset named "PPMatrix"
# HINT: you can use dataset.value to read data as numpy.array

# TODO: transpose the matrix
# HINT: you can use numpy tranpose()
result_matrix = np.array([])

# write result to output file under "PPMatrix" dataset of "/PPHappy" group
output_group = output_file.create_group("PPHappy")
output_dataset = output_group.create_dataset("PPMatrix", data=result_matrix)
