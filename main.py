import sys
from os import path, getcwd
from time import perf_counter

HAS_TO_HAVE = [
  'byr',  # (Birth Year)
  'ecl',  # (Eye Color)
  'eyr',  # (Expiration Year)
  'hcl',  # (Hair Color)
  'hgt',  # (Height)
  'iyr',  # (Issue Year)
  'pid',  # (Passport ID)
  # 'cid',   (Country ID)
]

def read_file(filename):
  try:
    with open(filename) as f:
        content = f.readlines()

    # I converted the file data to integers because I know 
    # that the input data is made up of numbers greater than 0
    content = [info.strip() for info in content]

  except:
    print('Error to read file')
    sys.exit()

  return content

def handle_refactor_info_item(data_input):
  """
  Expected format: Information blocks divided by a blank line
  """
  result = []
  data_line = dict()

  for line in data_input:
    if line != '':
      for item in line.split(' '):
        key, value = item.split(':')
        data_line[key] = value
     
    else:
      result.append(data_line)
      data_line = dict()
  
  if data_line != {}:
    result.append(data_line)

  return result

def find_valid_passports(data):
  count_valid_passports = 0
  
  for item in data:
    item_sorted = sorted(item, key=str.lower)
    items = [item for item in item_sorted if item != 'cid']

    if set(HAS_TO_HAVE) == set(items):
      count_valid_passports += 1

  return count_valid_passports

if __name__ == "__main__":
    start_timer = perf_counter()

    filename = path.join(getcwd(), 'inputData.txt')
    input_data = read_file(filename)

    data_refactored = handle_refactor_info_item(input_data)

    print(data_refactored)

    result = find_valid_passports(data=data_refactored)

    print(f'Result: {result}')

    end_timer = perf_counter()
    print(f'Time of execution {round(end_timer - start_timer, 5)} seconds')
    print('End of script')
    sys.exit(0)