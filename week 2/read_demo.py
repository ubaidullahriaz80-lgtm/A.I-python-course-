for i in range(50):
    print(f.write)
     f = open('demo.txt','a')
    f.write('hello')
   f.close()

    f = open('demo.txt','r')
   text = f.read()
   print(text)
   f.close()