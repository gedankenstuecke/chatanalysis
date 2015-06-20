import sys
import os
import glob
from bs4 import BeautifulSoup

emoticons = [":D", ";)", ":)",":p", ":P", ":3", ":|", ":/", ":(", ":*", "<3"]
#username = "gedankenstuecke@jabber.phylomemetic-tree.de"
username = "WHOMTOEXPORT@jabber.com"

def get_logs(directory):
    '''
    Adium creates lots of xml logfiles, so we need to get all of them before we
    can start parsing them
    '''
    if directory[-1] != "/":
        directory += "/"
    files = glob.glob(directory+"*.chatlog")
    out_files = []
    for f in files:
        fa = f.split("/")
        out = f + "/" + fa[-1].replace("chatlog","xml")
        out_files.append(out)
    return out_files

def iterate_logs(directory,files):
    for i in files:
        print_emoticons(directory,i)

def print_emoticons(directory,fhandle):
    '''
    This will only return the number of emoticons, defined in line6 for
    each day, if you want to do something else/dump everything change the
    processing here
    '''
    f = open(fhandle,"r")
    soup = BeautifulSoup(f,"xml")
    messages = soup.findAll("message")
    for message in messages:
        if message["sender"] == username:
            line = message.text
            total_emo_count = 0
            date = message["time"][:10]
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
    iterate_logs(sys.argv[1],log_files)

main()
