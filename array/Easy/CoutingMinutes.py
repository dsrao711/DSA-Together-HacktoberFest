
def time_convert(time):
    time_elements = time[:-2].split(":") 
    time_elements = [int(time_elements[0]), int(time_elements[1])] if time[-2:] == "am" else [int(time_elements[0])+12, int(time_elements[1])]
    time_elements[0] = time_elements[0] if (time_elements[0]!=12 and time_elements[0]!=24) else time_elements[0]-12
    return time_elements


def CountingMinutes(str): 
  start,end = [time_convert(time) for time in str.split("-")]
  if (start[0] <= end[0]):
  	return 60* (end[0] - start[0]) + end[1] - start[1]
  else:
  	return 60 * (24 - start[0] + end[0]) - start[1] + end[1] 

time = input()
output = CountingMinutes(time)
print(output)