import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    f = open(input_file_name)
    w = open(output_file_name , 'w')

    lines = f.readlines()

    for line in lines:
        line = line.split(',')
        name = line[0]
        hx = line[1]
        if hx[-1] == '\n':
            hx = hx[:-1]
        hx = hx.lower()
        
        
        for password in range(1000 , 9999 + 1):
            hash_i = hashlib.sha256(str(password).encode()).hexdigest()
            if hash_i == hx:
                w.write(name)
                w.write(',')
                w.write(str(password))
                w.write('\n')

    w.close()
    f.close()