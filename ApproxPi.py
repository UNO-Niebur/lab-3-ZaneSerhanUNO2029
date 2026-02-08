#ApproxPi.py
#Name: Zane Serhan
#Date: 2/7/2026
#Assignment: Lab3 ExtraCredit Pi
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #ask user for decimal percision (up to 10)

  decimal = int(input("Enter decimal precision (1-10)"))
  factor = 10 ** decimal
  start = time.time()

  #calculate pi using the approximation technique

  pi = math.pi
  pi = pi * factor
  pi = int(pi)
  pi = pi / factor

  end = time.time()

  elapsedTime = end - start
  print("New pi is:", pi)
  print("Elapsed time is:", elapsedTime)

if __name__ == '__main__':
  main()
