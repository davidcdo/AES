Name: David Do
UTEID: dcd954
Email: davidcdo12@gmail.com
Class: CS361
Assignment: AES Crypto
Date Completed - Sunday, September 30

Introduction:
	This program is an AES program that will encrypt or decrypt files using 128 bit 	keys or 256 bit keys. 
	
	For 128 bit keys, there will be 10 rounds and 14 rounds for 256 bit keys.

	Each encryption/decryption will consist of an initial round, the cycle of rounds, 	and the final round.

	The initial round will only set up the ‘state’ and the first ‘round_key’.
	The cycle of rounds consists of subBytes, shiftRows, mixColumns, and addRoundKeys
	The final round is similar to the cycles but excludes mixColumns

Function and Methods:
	setArgs() - gets the arguments entered by the user and sets up the global 		variables 

	checkArgs() - gets for correct arguments

	getArgs() - parses the arguments entered by user
	
	get_key_expansion() - generate the key_expansions that acts as a ‘key scheduler’ 	for each round

	get_output() - produces an output from encrypting/decrypting

	decrypt()/encrypt() - decrypts/encrypts in blocks of 16bytes
	
	subByte/inSubByte() - subs using S_CON/INV_S_CON
	
	shiftRows/invShiftRows() - shifts x amount, depending on current row

	mixColumns - mixes columns using the MUL lookup table and the polynomial equation
	
	addRoundKeys - Adds another roundly to the current state (used to generate an 		output)
	
Execute:
	The following AES program can be executed in the following way:

	python AES.py --keysize <128 or 256> --keyfile <KEYFILE> --inputfile <INPUTFILE>
		--outputfile <OUTFILENAME> --mode $<encrypt or decrypt>

	Example call: 

	python AES.py --keysize 128 --keyfile key --inputfile input
		--outputfile output --mode encrypt

Project References:
	PDF file - 
	https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.197.pdf

	YouTube Videos - 
	https://www.youtube.com/watch?v=K2Xfm0-owS4
	https://www.youtube.com/watch?v=7uRK9iOk4uk
	https://www.youtube.com/watch?v=dRYHSf5A4lw
	https://www.youtube.com/watch?v=bERjYzLqAfw
	https://www.youtube.com/watch?v=4pmR49izUL0