def longest_substring():
  s='azcbobobegghakl'
 # Paste your code into this box 
  tmp1=''
  tmp2=''
  for char in s:
      if(tmp2==''):
          tmp2=char
      elif(tmp2[-1]<=char):
          tmp2+=char
      elif(tmp2[-1]>char):
          if(len(tmp1)<len(tmp2)):
             tmp1=tmp2
             tmp2=char
          else:
             tmp2=char
  if (len(tmp2) > len(tmp1)):
      tmp1=tmp2
      print "Longest substring in alphabetical order is: "+tmp1
  else:
      print "Longest substring in alphabetical order is: "+tmp1 

def main():
	longest_substring()

if __name__ == '__main__':
  main()


