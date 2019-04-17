account = [
  {
    'user' : 'trung312',
    'pass': 'trung312'
      },
  {
    'user':'trung123',
    'pass':'trung123'

     },
  {
    'user':'trung321',
    'pass':'trung321'
  }
]
a= input('nhập')
b= input('nhập')
c = 0
for i in account :
    if a == i['user'] and b == i['pass'] :
      c = 1
      print(c)
print(c)
      
if c== 1:
  print('chuẩn')
else :
  print('sai ')

