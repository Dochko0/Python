pen = float(input())
price_Pen = pen*5.8
marker = float(input())
price_Marker = marker*7.2
preparat = float(input())
price_Preparat = preparat*1.2
percent = float(input())
all = (price_Pen+price_Marker+price_Preparat) * ((100-percent)/100)

print(f'{all:.3f}')