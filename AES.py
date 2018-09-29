#Imports the Systems and Arrays
import sys
import array

# Define and initializes constants
keysize = None
keyfile = None
inputfile = None
outputfile = None
mode = None

# Sets the values from the args to the initializes constants
def setArgs():
	args = getArgs(sys.argv)

	global keysize, kefile, inputfile, outputfile, mode

	keysize = int(args['--keysize'])
	keyfile = args['--keyfile']
	inputfile = args['--inputfile']
	outputfile = args['--outputfile']
	mode = args['--mode']

	checkArgs()

# Parse the arguments from sys.argv
def getArgs(argv):
	list_args = {}
	while argv:
		if argv[0][0] == '-' and argv[0][1] == '-':
			list_args[argv[0]] = argv[1]
		argv = argv[1:]
	return list_args

# Helper method to setArgs that checks for correct arguments
def checkArgs():
	if (keysize != 128 and keysize != 256):
		print("ERROR: Please enter the correct keysize <128 or 256>")
		sys.exit()
	elif (keyfile == "None" or inputfile == "None" or outputfile == "None"):
		print("ERROR: Please enter the following files: keyfile, inputfile, outputfile")
		sys.exit()
	elif (mode != "encrypt" and mode != "decrypt"):
		print("ERROR: Please enter a correct mode <encrypt or decrypt>")
		sys.exit()

#
def encrypt:

#
def decrypt:

#
def add_round_key:

#
def sub_bytes:

#
def shift_rows:

#
def mix_columns:

# Main function, starts everything up
def main():
	setArgs()

	print(keysize)
	print(keyfile)
	print(inputfile)
	print(outputfile)
	print(mode)

if __name__ == "__main__":
	main()
