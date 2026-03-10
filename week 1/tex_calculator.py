num = float(input('please enter your pay: '))
if num <= 5000:
    tex = num * 0.02
    print('your tex is',tex)
elif num <= 10000:
    tex = num * 0.03
    print('your tex is',tex)
elif num <= 15000:
    tex = num * 0.04
    print('your tex is',tex)
elif num <= 20000:
    tex = num * 0.05
    print('your tex is',tex)
elif num > 20000:
    tex = num * 0.10
    print('your tex is',tex)