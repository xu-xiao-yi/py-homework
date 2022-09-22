# 跳出本次循环，即本次循环不参与运算所以使用continue，如果到这次循环就结束则使用break
# 这里默认的范围是0-100 首尾都取，所以range(0,101);
for i in range(0,101):
    if i==21:
        continue
    else:
        print('当前数字为',i)