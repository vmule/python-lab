import math

def convertDegreesToRadians(degrees):
    # 360 :  2*3.1415 = degrees : x
    x = (2 * 3.1415 * degrees) / 360
    return round(x, 4)

def getSmallestClockAngle(timeString, unit):
  hour = timeString.split(':')[0]
  minutes = timeString.split(':')[1]
  # 12 = 0, 1 = 30, 2 = 60, 3 = 90, 6 = 180
  if int(hour) == 12:
      hourDegrees = 0
  else:
      hourDegrees = int(hour) * 30 + int(minutes) * 6 / 12
  # 12 = 0, 1 = 6, 2 = 12
  if int(minutes) == 0:
      minutesDegrees = 0
  else:
      minutesDegrees = int(minutes) * 6
      
  angle = abs(hourDegrees - minutesDegrees)
  if angle > 180:
      angle = abs(angle - 360)
    

  result = angle
  if unit == 'radians':
      return convertDegreesToRadians(result)
  return 
