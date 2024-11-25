#Inputs
def jaro(s1, s2):
  #d denotes as the distance transpositions are allowed to be
  #Note: d can be a decimal; thus, it must be (typically) floored (as char distance cannot be a float)
  d=(max(len(s1), len(s2))//2)-1
  
  #Match index #s
  a, b, = {}, {}
  
  t=0
  #Check for matches
  for i, v in enumerate(s1):
    #Lower/upper bounds to stay within index
    lb=max(i-d, 0)
    ub=min(len(s2), i+d+1)
    
    #Find characters that match
    for j in range(lb, ub):
      if j not in b and i not in a and s2[j]==v:
        a[i]=b[j]=v
        
  #m is just the num. of matches
  m=len(b)
  
  if m==0:
    return
  
  #Calculate tranpositions
  for i, j in zip([s1[i] for i in range(len(s1)) if i in a],  [s2[i] for i in range(len(s2)) if i in b]):
    #If matched characters are different in the same index
    if i!=j:
      t+=1
  
  #Abide to equation
  t//=2
  
  #Final equation
  return ((m/len(s1))+(m/len(s2)+((m-t)/m)))/3
