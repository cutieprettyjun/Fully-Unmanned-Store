import os
import random


def keySync(target, source): # target 딕셔너리의 키가 source 딕셔너리의 키를 참조하도록 합니다.
    for i in source.keys():
        if i in target.keys():
            continue
        target[i] = None

def commands(command: str): # 입력되는 명령어들을 처리합니다.
    global day
    if command == "store":
        while True:
            key = input("입고하려는 물품의 종류(id)를 입력해주세요. 완료했으면 done을 입력하세요: ")
            if key == "done":
                os.system("clear")
                break
            key = int(key)

            value = int(input("입고하려는 물품 %d의 수량을 입력하세요: " % key))
            stock[key] += value
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
            print("\n")
        
    elif command == "next":
        input("%d일차가 종료되었습니다." % day)
        if day % 7 == 0:
            order(stock)
            volume.clear()
            keySync(volume, stock)
        day += 1
        input("%d일차가 시작되었습니다.")
    else: input("invalid command")
        

def order(stock): # 부족량을 자동으로 계산해 수요에 맞춰 필요한 만큼 발주해줍니다.
    id = list(stock.keys())
    inventory = list(stock.values())

    # request = [inventory[]]
    print("다음의 발주를 요청합니다")
    for i in range(len(stock)):
        print(id[i], ":", request[i])

    answer = input("승인하시겠습니까?(confirm/deny): ")
    if answer == "confirm":
        for key, value in enumerate(stock.keys()):
            stock[value] += request[key]
    elif answer == "deny":
        while True:
            id, change = input("발주 수정 사항을 입력하세요(id, amount)\n완료했으면 done, 0을 입력하세요: ")
            if id == "done":
                break
            request[i] += int(change)
    

# stock: 재고 현황입니다
# volume: 주당 판매 개수입니다. 주마다 초기화합니다.

day = 0
stock = {100001: 0, 100002: 0, 100003: 0, 100004: 0, 100005: 0, 100006: 0, 100007: 0, 100008: 0, 100009: 0, 100010: 0}
volume = {}
keySync(volume, stock)

while True:
    os.system("clear")
    commands(input("명령어를 입력하세요: "))