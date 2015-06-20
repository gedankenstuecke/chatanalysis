import re
import codecs
import sys
import unicodedata as uni

# this one is a bit more wild, it uses the dumps from imessage to text and
# looks for all messages that contain >1 emoji.
# for those messages it creates all possible pairs of emojis and dumps those
# line by line, ideal for doing a co-occurrence analysis


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

print "emo1\temo2"

def pairs(seq):
    for i in range(0, len(seq)-1):
        for j in range(i+1, len(seq)):
            yield (seq[i], seq[j])

for line in codecs.open(sys.argv[1], "r", "utf-8"):
    line_array = line.strip().split("|")
    rematch = re.search(myre,line_array[2])
    if rematch != None:
        out_array = []
        emoji_array = rematch.group(0).encode('unicode-escape').split("\\")
        for i in emoji_array:
            if i != "":
                j = "\\" + i
                datetime = line_array[0].encode("utf-8")
                date = datetime.split(" ")[0]
                hour = datetime.split(" ")[1].split(":")[0]
                out_array.append(j)
        for k in pairs(out_array):
           print k[0].decode("unicode-escape").encode("utf-8") + "\t" + k[1].decode("unicode-escape").encode("utf-8")
