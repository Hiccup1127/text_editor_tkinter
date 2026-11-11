# File saving made me to think a lot about how to implement file saving
# properly, so here's the actual python file saving as how
# it's supposed to work (as how I figured it out anyway)

def save_file(path: str=None, text: str=None, force=False):
    try:
        if path is None or force==True: # rewriting the current path
            path = str(input("Path to save the file: "))
        with open(path, 'w') as f:
            f.write(text)
        return path
    except Exception as e:
        print(f"Can't save the file, {e}")
        return e;

def open_file(path: str=None):
    try:
        if path is None:
            path = str(input("Path to open the file: "))
        with open(path, 'r') as f:
            output = f.read()
        return output
    except Exception as e:
        print(f"Can't save the file, {e}")
        return e;

# The main thing is that it handles if file does have the path or no.
# If the file is new, it asks where to save it, if it's not
# new, it saves it on given path; If we want to force saving the
# file, for example if we want to save it somewhere else, we can use
# the force flag to produce it (basically copying the current file).

# The process of opening the file is the same, only that here we read
# the text from the file and return this instead of the path

# In filedialogs.py the problem is that I have notebook instead of
# the python strings. But it's ok now.