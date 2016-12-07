#Author: Phil Bradford
#Solution for http://adventofcode.com/2015/day/12

import sys
import re
import json

def red_math(filename):
  total = 0
  re_numbers = re.compile('(-?\d+)')
  re_object = re.compile('{.*}')
  re_red = re.compile(r':\"red\"')
  #parse all numbers not within { }
  #input = open(filename, 'rU')
  with open(filename) as f:
    parsed_file = json.load(f)
  print rsum(parsed_file)
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