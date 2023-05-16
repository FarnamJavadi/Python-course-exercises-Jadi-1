import csv
from statistics import mean 
from collections import OrderedDict

def calculate_averages(input_file_name, output_file_name):
    f = open(input_file_name)
    w = open(output_file_name , 'w')
    lines = f.readlines()
    dic = OrderedDict()
    for line in lines:
        line = line.split(',')
        name = line[0]
        marks = line[1:]

        counter = -1
        for number in marks:
            counter += 1
            marks[counter] = float(number)
        
        avrage = mean(marks)
        avrage = str(avrage)
        
        dic[name] = avrage
        w.write(name)
        w.write(',')
        w.write(avrage)
        w.write('\n')
    w.close()
    f.close()

def calculate_sorted_averages(input_file_name, output_file_name):
    f = open(input_file_name)
    w = open(output_file_name , 'w')
    lines = f.readlines()
    dic = OrderedDict()

    for line in lines:
        line = line.split(',')
        name = line[0]
        marks = line[1:]

        counter = -1
        for number in marks:
            counter += 1
            marks[counter] = float(number)
        
        avrage = mean(marks)
        dic[name] = avrage

    sorted_dic = sorted(dic.items(), key = lambda x: (x[1] , x[0]))
    
    tcount = -1
    for this_one in sorted_dic:
        tcount += 1
        n = this_one[0]
        m = str(this_one[1])
        w.write(n)
        w.write(',')
        w.write(m)
        w.write('\n')

    w.close()
    f.close()

def calculate_three_best(input_file_name, output_file_name):
    f = open(input_file_name)
    w = open(output_file_name , 'w')
    lines = f.readlines()
    dic = OrderedDict()

    for line in lines:
        line = line.split(',')
        name = line[0]
        marks = line[1:]

        counter = -1
        for number in marks:
            counter += 1
            marks[counter] = float(number)
        
        avrage = mean(marks)
        dic[name] = avrage
    
    sorted_dic = sorted(dic.items() , key = lambda x: (-x[1] , x[0]))
    
    first = sorted_dic[0]
    second = sorted_dic[1]
    third = sorted_dic[2]

    w.write(first[0])
    w.write(',')
    w.write(str(first[1]))
    w.write('\n')
    w.write(second[0])
    w.write(',')
    w.write(str(second[1]))
    w.write('\n')
    w.write(third[0])
    w.write(',')
    w.write(str(third[1]))

    w.close()
    f.close()


def calculate_three_worst(input_file_name, output_file_name):
    f = open(input_file_name)
    w = open(output_file_name , 'w')
    lines = f.readlines()
    avrages = []

    for line in lines:
        line = line.split(',')
        name = line[0]
        marks = line[1:]

        counter = -1
        for number in marks:
            counter += 1
            marks[counter] = float(number)
        
        avrage = mean(marks)
        avrages.append(avrage)

    avrages.sort()
    first = str(avrages[0])
    second = str(avrages[1])
    third = str(avrages[2])

    w.write(first)
    w.write('\n')
    w.write(second)
    w.write('\n')
    w.write(third)

    w.close()
    f.close()

def calculate_average_of_averages(input_file_name, output_file_name):
    f = open(input_file_name)
    w = open(output_file_name , 'w')
    lines = f.readlines()
    avrages = []

    for line in lines:
        line = line.split(',')
        name = line[0]
        marks = line[1:]

        counter = -1
        for number in marks:
            counter += 1
            marks[counter] = float(number)
        
        avrage = mean(marks)
        avrages.append(avrage)

    result = mean(avrages)
    result = str(result)

    w.write(result)
    w.close()
    f.close()