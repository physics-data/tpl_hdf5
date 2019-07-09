#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, time, os, subprocess, time, shutil, json, h5py
import numpy as np

testcases = [
    ('data/hdf5_1.in', 'data/hdf5_1.out'),
    ('data/hdf5_2.in', 'data/hdf5_2.out'),
    ('data/hdf5_3.in', 'data/hdf5_3.out'),
    ('data/hdf5_4.in', 'data/hdf5_4.out'),
    ('data/hdf5_5.in', 'data/hdf5_5.out')
]

if __name__ == '__main__':

    if sys.version_info[0] != 3:
        print("Please use python3")
        exit(1)

    program_file = 'hdf5.py'
    if len(sys.argv) > 1: 
        program_file = sys.argv[1]
    
    if not os.path.isfile(program_file):
        print('File {} not present!'.format(program_file))
        exit(1)

    success_count = 0

    for input, output in testcases:
        # remove the output file
        test_filename = 'test.output'
        try:
            os.remove(test_filename)
        except:
            pass
        p = subprocess.Popen([sys.executable, program_file, input, test_filename], stdout=open(os.devnull,'w'), stderr=subprocess.PIPE)
        message = ''
        success = True
        start_time = time.time()
        while p.poll() is None:
            if time.time() - start_time > 2:
                p.terminate()
                message = 'Time limit exceeded'
                success = False
                break
        else:
            if not os.path.isfile(test_filename):
                message = 'No output file found'
                success = False
            else:
                try:
                    std_file = h5py.File(output, 'r')
                    std_data = std_file["/PPHappy"]["PPMatrix"][()]

                    ans_file = h5py.File(test_filename, 'r')
                    ans_data = ans_file["/PPHappy"]["PPMatrix"][()]

                    if not np.array_equal(std_data, ans_data):
                        message = 'Data mismatch: should be \n\'{}\'\n, get \n\'{}\''.format(std_data, ans_data)
                        success = False
                except:
                    message = 'Could not find output data'
                    success = False
                    pass
        if success:
            success_count += 1
            if os.isatty(1):
                print('Testcase {}: PASS using {:.2f} seconds'.format(input, time.time() - start_time))
        else:
            if os.isatty(1):
                print('Testcase {}: {}'.format(input, message))
                stdout, stderr = p.communicate(timeout=1)
                if len(stderr) > 0:
                    print('       : your program exited with:')
                    sys.stdout.buffer.write(stderr)

        
        
    grade = int(100.0 * success_count / len(testcases))
    
    if os.isatty(1):
        print('Total Points: {}/100'.format(grade))
    else:
        print(json.dumps({'grade': grade}))

