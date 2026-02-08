#TempConvert.py
#Name:Zane Serhan
#Date: 2/7/2026
#Assignment:Lab3 TempConvert
#Purpose: Convert a user input temp from Fahrenheit to Celsius.

def main():
  #Prompt the user for a Fahrenheit temperature
  TempInput = int(input("Enter a temperature in Fahrenheit   "))
  #Convert that temperature to celsius, rounding to 1 decimal percision
  TempCel = (TempInput - 32) * (5/9)
  DecimalCel = round(TempCel, 1)
  #Output converted temperature
  print(TempInput, "is ", DecimalCel, "degrees celsius.")
if __name__ == '__main__':
  main()
