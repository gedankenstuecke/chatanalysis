import re
import codecs
import sys

# this one is a bit more wild, it uses the dumps from imessage to text and extracts
# all emoji it finds, along with the time stamp they were sent on.


# first of all. which ucs build are we on?

try:
    # Wide UCS-4 build
    myre = re.compile(u'['
        u'\U0001F300-\U0001F64F'
        u'\U0001F680-\U0001F6FF'
        u'\u2600-\u26FF\u2700-\u27BF]+',
        re.UNICODE)
except re.error:
    # Narrow UCS-2 build
    myre = re.compile(u'('
        u'\ud83c[\udf00-\udfff]|'
        u'\ud83d[\udc00-\ude4f\ude80-\udeff]|'
        u'[\u2600-\u26FF\u2700-\u27BF])+',
        re.UNICODE)

#this is our header row
print "datetime;date;hour;emoji"
#now let's iterate the file
for line in codecs.open(sys.argv[1], "r", "utf-8"):
    line_array = line.strip().split("|")
    # and find all emoji
    rematch = re.search(myre,line_array[2])
    # did we find at least one?
    if rematch != None:
        # great! let's split those emoji we got up into single items.
        # it's super ugly because just using "split" doesn't work...
        emoji_array = rematch.group(0).encode('unicode-escape').split("\\")
        for i in emoji_array:
            if i != "":
                j = "\\" + i
                datetime = line_array[0].encode("utf-8")
                date = datetime.split(" ")[0]
                hour = datetime.split(" ")[1].split(":")[0]
                print datetime + ";" + date + ";" + hour + ";" + j.decode("unicode-escape").encode("utf-8")
