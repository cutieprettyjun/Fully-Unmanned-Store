# Fully-Unmanned-Store
2024년 2학기말 프로젝트 - 팀 소비에트

 이 프로젝트의 주제는 완전 무인 편의점입니다. 무인 편의점은 현재도 존재하나, 완전한 형태의 무인이라고 말하기엔 이릅니다. 여전히 각 지점마다 관리할 사람 한두명씩은 필요하고, 무인 시스템이라 한들 사람이 자리를 비웠을 때만 잠시 켜놓지, 24시간동안 지속적으로 유지하는 경우는 극히 드뭅니다. 저희 팀은 관리자가 필요없이 사실상 단독으로 반영구적으로 운영 가능한 편의점을 기획하고자 하였습니다.

  무엇을 구현할 것인가?
  
 당연히 일주일 남짓동안 편의점을 하나 차릴 순 없으므로, 선택적인 일부분을 구현하고자 합니다. 우리의 구현 목표는 편의점의 관리 시스템 총체입니다. 물품 입출고, 재고 관리부터 물품이 부족할 경우 자동으로 외부에 발주를 넣는 시스템까지를 구현할 것입니다.

어떤 방식으로 구현할 것인가? - 읽지 마세요

 기본적으로 Python을 이용합니다. 우선 간이로 구현해보는 것이므로 10개정도의 물품 목록을 미리 만들어 놓습니다. 예컨데 이클립스 페퍼민트향의 제품 ID가 100001, 칸쵸가 100002, ...... 이렇게 있다고 합시다. 각각의 제품 ID(key)에 그의 개수(value)를 대응시키는 구조이므로 dictionary를 사용하는 것이 유용할 것입니다. 만약 이클립스 페퍼민트향이 829개, 칸쵸가 423개 있다고 한다면, 재고 딕셔너리는 다음과 같이 생겼을 것입니다: {100001: 829, 100002: 423}. 만약 칸쵸(100002)가 추가로 한 개 입고된다면 재고[100002] += 1, 제가 칸쵸를 네 개 구매하였다면 재고[100002] -= 4 이런 식으로 구현하면 될 것입니다. 그렇다면 재고 관리 및 발주 시스템은 어떻게 구현할까요? 매 주 발주를 넣는다고 한다면, 다음 발주량을 정하기 위해선 이번 주의 수요를 바탕으로 다음 주의 수요를 예측해야 합니다. 다음 주의 수요를 예측하기 위해선 이번 주에 얼마나 많은 양이 얼마나 빠른 속도로 팔렸는가를 알아야 합니다. 얼마나 빠른 속도로 팔렸는가는 상당히 중요한 고려 대상입니다. 예컨대 이번 주에 밤 티라미수가 출시되어 시범적으로 100개정도 입고했다고 칩시다. 그런데 이럴수가 100개가 하루만에 다 팔려버렸습니다. 그렇다면 밤 티라미수는 아주아주 인기가 많다는 뜻일 겁니다. 즉 주당 판매 비율(sales rate per week, 줄여서 spw라고 합시다)뿐만 아니라 일당 판매 비율(sales rate per day, spd) 역시 아주아주 중요한 고려 요소일 것입니다. 그렇다면 둘 중 뭐가 더 중요할까요? 일반적인 경우에는 주당 판매 비율이 중요할 것입니다. 주당 판매 비율이 전체의 100%가 아니라면 주당 판매 비율만으로도 충분히 수요를 계산할 수 있습니다. 만약 주당 판매 비율이 100%일 경우, 일당 판매 비율을 고려해야 합니다. 예컨데 전체 재고가 일주일 중 3일에 걸쳐 34%, 33%, 33%가 빠져나갔다고 합시다. 그렇다면 다음 번 발주에서는 이번 발주량의 233.33333%를 발주하면 될 것입니다. 시간에 따라 물품의 수요가 줄어드는걸 감안하고 싶다면, 위와 같이 계산한 233%에 원하는 수를 곱해 그만큼 발주하면 될 것입니다. 그렇다면 이걸 어떻게 계산할까요? 판매일만을 고려해서 평균을 내면 되지 않을까요? 하지만 그러면 이러한 경우에는 어떨까요? 어떤 물품의 전체 재고가 나흘에 걸쳐 30%, 40%, 25%, 5%가 빠져나갔다고 생각해봅시다. 이럴 경우 마지막 날에는 일찍이 재고가 동나 일당 판매 비율이 낮은 것이라고 생각할 수 있습니다. 이러한 상황에서 평균을 내면 그 다음 주에도 재고 부족 현상이 발생할 것입니다. 즉 위와 같은 경우에는 평균값보단 중앙값이 더 적절할 것입니다. 물론 이틀만에 동나는 경우에는 따로 조치를 취해야 할 것입니다. 이틀의 경우는 예외적으로, 이틀중 하루에만 80% 이상의 재고가 쏠릴 경우 사실상 하루만에 다 팔린 것으로 간주하고, 그 이하일경우 그냥 똑같이 중앙값을 내면 큰 문제는 발생하지 않을 것입니다.
 실제 편의점에서는 바코드 스캐너가 자동으로 제품의 바코드를 스캔해 재고 현황을 자동으로 입력받겠지만, 동준쌤께서 어떻게 하는지 알려주시지 않았으므로 그냥 제품 아이디를 노가다로 입력한다고 합시다. 또한 제품의 판매 또한 결제 현황을 통해 자동적으로 조정하겠지만, 동준쌤께서 어떻게 하는지 알려주시지 않았으므로 역시 제품 아이디를 노가다로 입력한다고 칩시다. 발주 요청은 파일 입출력을 통해 구현하고 싶으나, 동준쌤께서 어떻게 하는지 알려주시지 않았으므로 그냥 print를 통해 필요한 개수를 출력하는 형식으로 구현하도록 합시다.
