import string

# from text to numbers
def create_encode_a1z26_map():
  return ({chr(i+96):i for i in range(1,27)})

def create_decode_09_map():
  return {
    0: ['a', 'k', 'u'],
    1: ['b', 'l', 'v'],
    2: ['c', 'm', 'w'],
    3: ['d', 'n', 'x'],
    4: ['e', 'o', 'y'],
    5: ['f', 'p', 'z'],
    6: ['g', 'q'],
    7: ['h', 'r'],
    8: ['i', 's'],
    9: ['j', 't']
  }

# from numbers to text
def create_decode_a1z26_map():
  encoder_mapping = create_encode_a1z26_map()
  return dict([(str(value), key) for key, value in encoder_mapping.items()])

def create_encode_09_map():
  encoder_mapping = create_decode_09_map()
  decoder_mapping = {}
  for key, values in encoder_mapping.items():
    for value in values:
      decoder_mapping[value] = key

  return decoder_mapping
  