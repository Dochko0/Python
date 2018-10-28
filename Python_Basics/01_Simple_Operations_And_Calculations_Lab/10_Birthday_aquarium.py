l = float(input())
w = float(input())
h = float(input())
percent = float(input())/100
volume= l*w*h*0.001
volume = (volume-volume*percent)
print(f'{volume:.3f}')
