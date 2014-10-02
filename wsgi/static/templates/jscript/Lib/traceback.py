import sys
def print_exc(file=sys.stderr):
    exc = __BRYTHON__.exception_stack[-1]
    file.write(exc.__name__)
    if exc.message:
        file.write(': '+exc.message+'\n'+exc.info)
    file.write('\n')
