# This is the (mode=2) algorithm of zcfgBeWlanGenDefaultKey from libzcfg_be.so in the VMG8828 firmware.
# It's a variant of Zykgen, but does not quite fit within the standard algorithm with just a new charset
# much thanks to Selenium on the hashkiller forum for getting the library cross-compiled and running inside QEMU.

import hashlib
import argparse

def wind3_mode2(serial, pwd_len):

	ambiguous_chars = '120olijvyz'
	lead_replacements = '3479'
	post_replacements = 'bdfhxkmprstuw'
	
	md5 = hashlib.md5()
	md5.update(serial.encode())
	md5_hex = md5.hexdigest()

	new_string = "%sPSK_ra0" % (md5_hex)
	md52 = hashlib.md5()
	md52.update(new_string.encode())
	new_md5_hash = md52.digest()

	base = new_md5_hash[0] * 256 + new_md5_hash[1]
	base_binary = bin(base)[2:].zfill(16)[::-1]
	
	password = ""

	for i in range(pwd_len):
		if base_binary[i] == '1' and i > 0:
			c = new_md5_hash[i] % 26 + 97
		else: 
			c = new_md5_hash[i] % 10 + 48
		password += chr(c)
	
	password = list(password)
	for bad_char in range(len(ambiguous_chars)):
		for pos in range(2, pwd_len):
			pwd_letter = password[pos]
			bad_letter = ambiguous_chars[bad_char]
			if pwd_letter == bad_letter:
				new_letter_pos = (base + bad_char) % 13
				new_letter = post_replacements[new_letter_pos]
				password[pos] = new_letter
	
	pos = 0
	for bad_char in range(len(ambiguous_chars)):
		pwd_letter = password[pos]
		bad_letter = ambiguous_chars[bad_char]
		if pwd_letter == bad_letter:
			new_letter_pos = (base + bad_char) % 4
			new_letter = lead_replacements[new_letter_pos]
			password[pos] = new_letter

	print("".join(password))


parser = argparse.ArgumentParser(description='(mode=2) algorithm of zcfgBeWlanGenDefaultKey from libzcfg_be.so in the VMG8828 firmware.')
parser.add_argument('serial', help='Serial Number.')
parser.add_argument('-pwd_len', help='Password length.', default=16, type=int)
args = parser.parse_args()

wind3_mode2(args.serial, args.pwd_len)
