timeinseconds = int(input())
hours = timeinseconds // 3600
minutes = (timeinseconds % 3600) // 60
seconds = timeinseconds - ((hours * 3600) + (minutes * 60))
print('the time is ',hours,':',minutes,':',seconds)