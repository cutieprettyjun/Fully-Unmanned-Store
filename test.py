def keySync(target, source):
    for i in source.keys():
        if i in target.keys():
            continue
        target[i] = None

day = 1
stock = {100001: 0, 100002: 0, 100003: 0, 100004: 0, 100005: 0, 100006: 0, 100007: 0, 100008: 0, 100009: 0, 100010: 0}
volume = {}
keySync(volume, stock)
print(volume)
stock[100011] = 0
volume[100001] = 4
print(stock)
keySync(volume, stock)
print(volume)