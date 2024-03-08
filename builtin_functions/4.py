import time
import math

number = int(input('numb: '))
milliseconds = int(input('millisec: '))

time.sleep(milliseconds / 1000)
result = math.sqrt(number)
print(f"Square root of {number} after {milliseconds} milliseconds is {result}")
