import argparse
from pathlib import Path

parser = None
args = None
input_path = None
output_path = None
input_file = None
output_file = None

def init_args():
    global parser, args
    parser = argparse.ArgumentParser(description = 'This app makes Minetest\'s debug file easier to use in other scripts.')
    parser.add_argument('--input_file', type = str, help = 'Path to "debug.txt". Default is "[HOME]/.minetest/debug.txt".')
    parser.add_argument('--output_file', type = str, help = 'Where to save the output. Default is "[HOME]/mtexported.txt".')
    args = parser.parse_args()

def get_input_path():
    global input_path
    if args.input_file != None:
        input_path = Path(args.input_file)
        if input_path.exists():
            if not input_path.is_file:
                print(f"{input_path} is not a file.")
                raise
        else:
            print(f"{input_path} is not a valid path.")
            raise
    else:
        input_path = Path(f"{Path.home()}/.minetest/debug.txt")
        if not input_path.exists():
            print(f"Uh oh! {input_path} doesn't exist. This may be caused by running as root or by not having installed Minetest. Retry setting --input_file.")
            raise

def get_output_path():
    global output_path
    if args.output_file != None:
        output_path = Path(args.output_file)
        if output_path.exists():
            if not output_path.is_file:
                print(f"{output_path} is not a file.")
                raise
        else:
            print(f"{output_path} is not a valid path.")
            raise
    else:
        output_path = Path(f"{Path.home()}/mtexport.txt")
    if output_path.exists:
        if input(f"{output_path} already exists. Continuing will overwrite it. Are you sure? (Y/n) ").upper() != "Y":
            raise

def open_files():
    global input_file, output_file
    input_file = open(input_path, mode = "rt")
    output_file = open(output_path, mode = "wt")

def fix_res_dict(f_data, year, month, day, hour, minute, second):
    try:
        f_data[year]
    except:
        f_data[year] = dict()
    try:
        f_data[year][month]
    except:
        f_data[year][month] = dict()
    try:
        f_data[year][month][day]
    except:
        f_data[year][month][day] = dict()
    try:
        f_data[year][month][day][hour]
    except:
        f_data[year][month][day][hour] = dict()
    try:
        f_data[year][month][day][hour][minute]
    except:
        f_data[year][month][day][hour][minute] = dict()
    try:
        f_data[year][month][day][hour][minute][second]
    except:
        f_data[year][month][day][hour][minute][second] = list()
    return f_data

def elaburate_data():
    input_read = input_file.read()
    input_read = input_read.split(sep="\n")
    data = list()
    for x in input_read:
        if x.find("ACTION") != -1:
            y = x.split(":")
            if y[4].find(".") == -1 and y[4].find("[") == -1 and y[4].find("MOD") == -1:
                data.append(x)
            elif y[4].find("joins game") != -1:
                data.append(x)
    
    f_data = dict()
    for x in data:
        f_data = fix_res_dict(f_data, x[:4], x[5:7], x[8:10], x[11:13], x[14:16], x[17:19])
        if x[35:].find("Server:") == -1:
            f_data[x[:4]][x[5:7]][x[8:10]][x[11:13]][x[14:16]][x[17:19]].append(x[37:])
        else:
            f_data[x[:4]][x[5:7]][x[8:10]][x[11:13]][x[14:16]][x[17:19]].append(x[35:])
    
    output_file.write(str(f_data))

def close_files():
    input_file.close()
    output_file.close()

init_args()
get_input_path()
get_output_path()
open_files()
elaburate_data()
close_files()