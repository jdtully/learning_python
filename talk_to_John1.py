def func(x):
    """ i had to write out the range  and go through this step by step watching the values  and
    predicting  what they were  going to be.  I had  forgotten that range made a list,  so i 
    annotated  the  line  to include the 4 things  in the list and  then it made  sense """
  res = 0
  for i in range(x): #range is 0,1,2,3
     res += i
  return res

print(func(4))