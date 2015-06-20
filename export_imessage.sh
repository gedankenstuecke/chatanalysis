#!/bin/bash
# here go the usernames you want exported.
# either the email-address or the phone number (in +01... format)
user="user1
user2
user3
user4"

# here's the actual export, iterate over all users
for i in $user;
do
# connect to sqlite, get correct chat-ID
sqlite3 ~/Library/Messages/chat.db "
select datetime(date,'unixepoch','31 years','localtime'),is_from_me,replace(text,'
','') from message where handle_id=(
select handle_id from chat_handle_join where chat_id=(
select ROWID from chat where guid='iMessage;-;$i')
)"
# writes directly to bash for now, so use pipes. gives 3 rows, separated by |
# Timestamp|my_message?|text
done
