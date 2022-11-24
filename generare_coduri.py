def permute(list, s):
   if list == 1:
      return s
   else:
      return [
         y + x
         for y in permute(1, s)
         for x in permute(list - 1, s)
      ]
f = open('coduri.txt', 'a')
f.write(('\n'.join(permute(5, ['0','1','2']))))

