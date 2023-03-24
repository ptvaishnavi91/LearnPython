import fileinput
import os
import sys

from FunctionsHW import norm_func as normalization

class File_Input():
    def __init__(self):

        #Task 1 : Define your input format (one or many records)
        self.input_choice = input('How do you want to enter the news feed? 1. Through console, 2. Using input file:\n')

    def input_func(self):
        if self.input_choice == '1':
            import ClassesHW
        elif self.input_choice == '2':

            # Task 2: Default folder or user provided file path
            ip_file_path = input('Enter the path of the input file:\n')
            # Use input file News_input.txt to test the file removal,
            # use News_input_test_normalize.txt to test case normalization of the input text

            sys_path = sys.path
            op_file_path = f'{sys_path[0]}\\News_output.txt'
            for line in fileinput.input(files=ip_file_path):
                #Task4: Apply case normalization functionality form Homework 3/4
                print(normalization(line))
                with open(op_file_path, 'a') as f:
                    f.write(normalization(line))
                    f.write('\n')

            #Task 3: Remove file if it was successfully processed
            ip_file = open(ip_file_path, 'r')
            op_file = open(op_file_path, 'r')

            ip_data = ip_file.readlines()
            op_data = op_file.readlines()

            i = 0
            for line1 in ip_data:
                if ip_data[i] == op_data[i]:
                    print(f'Line {i} is Identical\n\t Line: {ip_data[i]}')
                    compare = 'Identical'
                else:
                    print(f'Line {i} from input file is not matching with output file: \n\tInput:{ip_data[i]}\n\tOutput:{op_data[i]} ')
                    compare = 'Non-identical'
                i += 1
            ip_file.close()
            op_file.close()

            if compare == 'Identical':
                os.remove(ip_file_path)
        else:
            print('Incorrect input method selection, exiting')


file_ip = File_Input()
file_ip.input_func()



