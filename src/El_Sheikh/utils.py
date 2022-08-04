from config import *
def compute_percent_dict(Owners):
    percent_dict = {}
    for i in range(len(Owners)):
        if i <2:
            percent_dict.update({Owners[i][0]:0.125})
        else:
            percent_dict.update({Owners[i][0]:0.25})
    return percent_dict