from contextlib import contextmanager
from typing import TextIO


@contextmanager
def new_log_file(name):
    try:
        f: TextIO = open(name, 'w')
        f.write('---- begin of log ----\n')
        yield f
    finally:
        f.write('---- end of log ---\n')
        f.close()


if __name__ == '__main__':
    with new_log_file('tmp.logfile.tmp') as f:
        f.write("Test log 1\n")
        f.write("Test log 2\n")
        f.write("Test log 3\n")

# ---- begin of log ----
# Test log 1
# Test log 2
# Test log 3
# ---- end of log ---
