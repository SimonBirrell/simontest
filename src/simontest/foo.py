print "  importing bar_fn, baz_fn from simon_pythonsubpackage1"
from simon_pythonsubpackage1 import bar_fn, baz_fn
print "  imported bar_fn, baz_fn from simon_pythonsubpackage1"

def main():
	print " executing main() in foo.py"
	bar_fn()
	baz_fn()

if __name__ == '__main__':
    main()
