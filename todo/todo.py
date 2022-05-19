# python script for taking notes through command line and exporting as txt file

# get user to input task
# save task into list (mutable)
# export/write into txt

# task function
# write task
# delete task
# view task
# export task


import sys
import datetime

# help list
def help():
    sa = """Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics"""
    sys.stdout.buffer.write(sa.encode('utf8'))

# add task
def add(task):
    # append new task to the last line of txt
    f = open('task.txt', "a")
    f.write(task)
    f.write("\n")
    f.close()
    task = """+task+"""
    print(f"New task added {task}")
    
