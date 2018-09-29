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

	global keysize, keyfile, inputfile, outputfile, mode

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
	elif (keyfile == None or inputfile == None or outputfile == None):
		if (keyfile == None):
			print("ERROR: Missing keyfile")
		if (inputfile == None):
			print("ERROR: Missing inputfile")
		if (outputfile == None):
			print("ERROR: Missing outputfile")
		sys.exit()
	elif (mode != "encrypt" and mode != "decrypt"):
		print("ERROR: Please enter a correct mode <encrypt or decrypt>")
		sys.exit()

#
def key_expansion():
	return
#
def encrypt():
	return
#
def decrypt():
	return
#
def add_round_key():
	return
#
def sub_bytes():
	return
#
def shift_rows():
	return
#
def mix_columns():
	return

# Main function, starts everything up
def main():
	setArgs()

	print(keysize)
	print(keyfile)
	print(inputfile)
	print(outputfile)
	print(mode)

	# Opens and reads the files sent in from argv
	# "rb" means to read the file in binary
	# "wb" means to write the file in binary
	key_file = open(keyfile, 'rb')
	input_file = open(inputfile, 'rb')
	output_file = open(outputfile, 'wb')

	# The following function uses 'bytearray' returns an array of bytes 
	# thats reads from key_file or input_file into the 
	# following variables: key_file_bytes and input_file_bytes
	key_file_bytes = bytearray(key_file.read())
	input_file_bytes = bytearray(input_file.read())



	# Closes the files
	key_file.close()
	input_file.close()
	output_file.close()

if __name__ == "__main__":
	main()
