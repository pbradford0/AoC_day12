#Author: Phil Bradford
#Solution for http://adventofcode.com/2015/day/12

import sys
import re
import json

def red_sum(file):
  reds = 0
  if isinstance(file, dict):
    #loaded a dict, go deeper
    if "red" in file.values:
      #it's red, add all numbers
  elif isintance(file, list):
    #loaded a list, go deeper
  return reds

def red_math(filename):
  total = 0
  red_total = 0
  re_numbers = re.compile('(-?\d+)')
  re_object = re.compile('{.*}')
  re_red = re.compile(r':\"red\"')
  #parse all numbers not within { }
  #input = open(filename, 'rU')
  #calculate the grand total
  total = elf_math(filename)
  #open the file in json to make stuff objects and whatever
  with open(filename) as f:
    parsed_file = json.load(f)
  #calculate all reds
  reds = red_sum(parsed_file)
  #get all red numbers, subtract from total
  #red_vals = re.findall(re_numbers, reds)
  #for x in red_vals
    #red_total += int(x)
  total = total - red_total
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