list = ['(', '[', ']', '[', ')', '(', ')']
stack = []

for i in list:
  if i == '(' or i == '[':
    stack.append(i)
  else:
    if len(list) == 0:
      print "unbalanced"
      exit(0)
    else:
      if (stack[-1] == '[' and i == ']'):
        stack.pop()
      elif (stack[-1] == '(' and i == ')'):
        stack.pop()
      else:
        print "unbalanced"
        exit(0)
if len(stack) == 0:
  print "balanced"
else:
  print "unbalanced"
