#Author: Phil Bradford
#Solution for http://adventofcode.com/2015/day/12

import sys
import re
import json

def red_sum(item):
  if type(item) is dict:
    #loaded a dict, go deeper
    if "red" in item.values():
      return 0
    else:
      return sum(map(red_sum, item.values() ))
  elif type(item) is list:
    #loaded a list, go deeper
    return sum(map(red_sum, item))
  elif type(item) is int:
    return item
  return 0

def red_math(filename):
  total = 0
  #open the file in json to make stuff objects and whatever
  with open(filename) as f:
    parsed_file = json.load(f)
  #calculate all reds
  total = red_sum(parsed_file)
  return total

def elf_math(filename):
  total = 0
  re_numbers = re.compile('(-?\d+)')
  #parse all numbers from a file and add them together
  input = open(filename, 'rU').read()
  numbers = re.findall(re_numbers, input)
  for x in numbers:
    total += int(x)
  return total

def main():
  if len(sys.argv) != 2:
    print 'Please specify an input file'
    sys.exit(1)

  #a = elf_math(sys.argv[1])
  #print "Elf math: " + str(a)
  
  b = red_math(sys.argv[1])
  print "Elf math: " + str(b)

if __name__ == '__main__':
  main()