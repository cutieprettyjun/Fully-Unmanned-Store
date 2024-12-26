import os

def keySync(target, source): # 여러 딕셔너리들의 키를 맞춰줍니다. 물품이 추가/변경되어도 stock의 키만 추가/변경하면 됩니다.
    for i in source.keys():
        if i in target.keys():
            continue
        target[i] = None

def commands(command: str): # 입력되는 명령어들을 처리합니다.
    global day
    global standard
    if command == "standard":
        while True:
            os.system("clear")
            print("현재 설정된 기준은 다음과 같습니다 \n", standard)
            key = input("재고 기준을 설정하려는 물품의 종류(id)를 입력해주세요. 완료했으면 done을 입력하세요: ")
            if key == "done":
                os.system("clear")
                break
            key = int(key)

            if key not in stock.keys():
                input("invalid key")
                continue

            value = input("설정하려는 물품 %d의 수량을 입력하세요: " % key)
            value = int(value)
            keySync(standard, stock)
            standard[key] = value
            print("\n")

    elif command == "purchase":
        while True:
            print("현재 재고 상태는 다음과 같습니다")
            print(stock)
            key = input("구매(출고)하려는 물품의 종류(id)를 입력해주세요. 완료했으면 done을 입력하세요: ")
            if key == "done":
                os.system("clear")
                break
            key = int(key)
            value = int(input("구매(출고)하려는 물품 %d의 수량을 입력하세요: " % key))
            if stock[key] - value < 0:
                input("재고를 초과했습니다!")
                continue
            stock[key] -= value
            volume[key][day % 7] = value
            print("\n")
        
    elif command == "next":
        input("%d일차가 종료되었습니다." % day)
        if day % 7 == 0:
            order(stock)
            for i in volume.keys():
                for j in range(7):
                    volume[i][j] = 0
            keySync(volume, stock)
            keySync(standard, stock)
        day += 1
        input("%d일차가 시작되었습니다." % day)
    elif command == "help":
        input("""다음의 명령어가 있습니다
standard : 상품의 입고 기준을 설정합니다. 매 주 마지막 일에 재고량을 확인할 때, 입고 기준보다 적으면 발주를 넣습니다.
purchase : 제품을 구매합니다. 재고 현황에서 구매 개수만큼이 차감됩니다.
next : 다음 일로 넘어갑니다.""")
    else: input("invalid command")
        

def order(stock: list): # 부족량을 자동으로 계산해 수요에 맞춰 필요한 만큼 발주해줍니다.
    global standard
    id = list(stock.keys())
    inventory = list(stock.values())
    need = list(standard.values())

    request = [need[i] - inventory[i] for i in range(len(inventory))]
    os.system("clear")
    print(need) # debug
    print(inventory)
    print(request)
    print("다음의 발주를 요청합니다")
    for i in range(len(stock)):
        print(id[i], ":", request[i])

    answer = input("승인하시겠습니까?(confirm/deny): ")
    if answer == "confirm":
        for key, value in enumerate(stock.keys()):
            stock[value] += request[key]
    elif answer == "deny":
        while True:
            id = input("발주를 수정할 제품의 id를 입력하세요\n완료했으면 done을 입력하세요: ")
            if id == "done":
                break
            change = input("발주를 얼만큼 수정할지 입력하세요: ")
            request[int(id)] += int(change)
    else: input("invalid command"); order(stock)


# stock: 재고 현황입니다
# volume: 판매 개수를 기록합니다

day = 0
stock = {100001: 0, 100002: 0, 100003: 0, 100004: 0, 100005: 0, 100006: 0, 100007: 0, 100008: 0, 100009: 0, 100010: 0}
volume = {}
standard = stock.copy() # 참조하면 안됨 아아아아아아아아아아
keySync(volume, stock)
for key in stock.keys():
    volume[key] = [0 for i in range(7)]
os.system("clear")
commands("standard")
while True:
    os.system("clear")
    commands(input("명령어를 입력하세요: "))