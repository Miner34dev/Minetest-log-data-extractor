def import_mt_log(file_path):
    from datetime import datetime
    input_data = open(file_path, mode = "rt").read().split(sep="\n")
    result = list()
    for x in input_data:
        if x[21:36]=="ACTION[Server]:":
            date = datetime(int(x[:4]), int(x[5:7]), int(x[8:10]), int(x[11:13]), int(x[14:16]), int(x[17:19]))
            result.append({"when":date, "what":x[37:]})
    return result
