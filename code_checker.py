import sys
import constants

def check_input(args):
  if args.code == 'decode':
    check_codes(args, "A comma separated list of numbers between 0 through 9 must be used for '09' and 1 through 26 for 'a1z26.'")
  else:
    check_codes(args, 'Only alpha characters must be supplied when encoding.')

def check_codes(args, message):
  try:
    if args.code == 'decode':
      test_decode(args)

    if args.code == 'encode':
      test_encode(args)
  except:
    print(message)
    sys.exit(1)

def test_decode(args):
  if args.code == 'decode':
        codes = args.input.split(',')
        for code in codes:
          less_than_zero_when_not_zero_nine = (
              int(code) < 0 or 
              (int(code) == 0 and args.keyType == constants.A1Z26)
            )
          greater_than_nine_when_zero_nine = (
            (int(code) > 9 and args.keyType == constants.ZERO_NINE)
          )
          greater_than_twenty_six =  int(code) > 26

          is_not_valid = not code.isdigit() or less_than_zero_when_not_zero_nine or greater_than_nine_when_zero_nine or greater_than_twenty_six

          if is_not_valid:
            raise Exception

def test_encode(args):
  if args.code == 'encode':
        codes = args.input
        for code in codes:
          if not code.isalpha():
            raise Exception