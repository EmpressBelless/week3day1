import re
with open('regex.txt') as file:
  new_data = file.readlines()
  print(new_data)
  
  my_pattern = re.compile(' [^.] [^\s.\s] ([A-z])')
  matches = my_pattern.finditer(new_data)
  print(matches)

for match in matches:
  if match:
    print(match.group(1))
  else:
    print(None)