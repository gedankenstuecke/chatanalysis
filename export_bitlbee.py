import sys
import os
import glob

# again, this script is mainly concerned with different ascii emoticons,
# but it should be easy to adjust this. also: the files here are already plain
# text in any case, so there's no magic in this case

emoticons = [":D", ";)", ":)",":p", ":P", ":3", ":|", ":/", ":(", ":*", "<3"]

username = "user1"
not_user = "my_own_handle"


def get_logs(directory):
    if directory[-1] != "/":
        directory += "/"
    files = glob.glob(directory+"*.log")
    return files

def iterate_logs(directory,files,year):
    for i in files:
        date = year + "-" + i.split(".")[1]
        print date
        print_emoticons(date,directory,i)

def print_emoticons(date,directory,fhandle):
    f = open(fhandle,"r")
    for line in f:
#        if line.find(username) != -1: # this is my text!
        if line.find(username) != -1 and line.find(not_user) == -1:
            total_emo_count = 0
            for i in emoticons:
                emo = " " + i
                emo_count = line.count(emo)
                total_emo_count += emo_count
                if emo_count > 0:
                    j = 0
                    while j < emo_count:
                        print date + "\t"+ emo[1:]
                        j += 1
            if total_emo_count == 0:
                print date + "\t" + "-"

def main():
    log_files = get_logs(sys.argv[1])
    iterate_logs(sys.argv[1],log_files,sys.argv[2])

main()
