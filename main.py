#!/usr/bin/python3

import sys
import argparse
import code_checker
import mapping
import constants

from itertools import permutations

def main():
  parser = argparse.ArgumentParser(description='A1Z26 & 09 encoder/decoder')

  parser.add_argument(
    '-c', 
    '--code',
    type=str,
    choices=(constants.ENCODE, constants.DECODE),
    help="Specifies if the script encodes or decodes the user's input.",
    required=True
  )

  parser.add_argument(
    '-k', 
    '--keyType',
    type=str.lower, 
    choices=(constants.A1Z26, constants.ZERO_NINE),
    help='A1Z26 encoding/decoding. \n09 for 0-9 encoding/decoding.',
    required=True
  )

  parser.add_argument(
    '-i', 
    '--input', 
    type=str.lower,
    help='Input to be encoded/decoded. Encoding turns comma separated numbers into text. Decoding transforms letters into text.',
    required=True
  )

  args = parser.parse_args()
  code_checker.check_input(args)

  if args.keyType == constants.A1Z26:
    result = []
    if args.code == constants.ENCODE:
      encoder_mapping = mapping.create_encode_a1z26_map()
      for letter in args.input:
        result.append(encoder_mapping[letter])
    elif args.code == constants.DECODE:
      decoder_mapping = mapping.create_decode_a1z26_map()
      numbers = args.input.split(',')
      for number in numbers:
        result.append(decoder_mapping[number])
    print(result)

  elif args.keyType == constants.ZERO_NINE:
    results = []
    if args.code == constants.ENCODE:
      encoder_mapping = mapping.create_encode_09_map()
      for letter in args.input:
        results.append(encoder_mapping[letter])
    elif args.code == constants.DECODE:
      decoder_mapping = mapping.create_decode_09_map()
      numbers = args.input.split(',')
      for number in numbers:
        letters = decoder_mapping[int(number)]
        results.append(list(permutations(letters)))
    container = []
    for result in results:
      for letters in result:
        container.append(''.join(list(letters)))
    print(list(permutations(container, len(args.input.split(',')))))

if __name__ == '__main__':
  main()