import mymodule 

result = mymodule.graffiti()
print(result)
print('attempting to clean...')
try:
   mymodule.clean()
except mymodule.myError:
   print('there was an error cleaning the camera T1000\'s have been dispatched')
finally:
   print('this always occurs')