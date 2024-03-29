"""
캐릭터 경험치
캐릭터가 컨텐츠를 수행하고 경험치를 얻어 성장하는 모바일 게임이 있다. 제공된 컨텐츠
마다 이를 수행하기 위해 필요한 스태미나 소모량과 이 컨텐츠를 수행할 경우 얻을 수 있는
경험치가 정해져 있다. 이 게임에서 캐릭터는 자신이 보유하고 있는 스태미나로 제공된
컨텐츠들을 수행하여 경험치를 최대로 얻으려고 한다. 다만, 같은 컨텐츠는 반복해서 수행될
수 없다.

예를 들어, 캐릭터가 보유하고 있는 스태미나의 양이 100이고 제공된 3개의 컨텐츠가
(스태미나 소모량, 경험치)의 형식으로 (40,200), (50, 150), (30, 180) 와 같이 순서대로
주어져 있다고 하자. 이 상황에서 경험치를 가장 많이 얻는 방법은, 1번과 3번 컨텐츠를 각각
한번씩 수행하는 것이다. 이 경우 스태미나는 70을 소모하고 경험치는 380을 얻게 된다.

캐릭터가 보유하고 있는 스태미나의 양과 컨텐츠의 개수, 그리고 각 컨텐츠마다 스태미나
소모량과 얻는 경험치가 목록으로 주어졌을 때, 캐릭터가 얻을 수 있는 경험치의 최대값을
출력하는 프로그램을 작성하라.

입력 형식
첫째 줄에 캐릭터가 보유한 스테미나의 양을 나타내는 자연수 S가 주어진다.
(1 ≤ S ≤ 10,000) 다음 줄에 제공된 컨텐츠의 개수 N이 주어진다. (1 ≤ N ≤ 1,000)
다음 N개의 줄에 각 컨텐츠마다 스태미나 소모량 U와 얻는 경험치 E가 순서대로 주어진다.
(1 ≤ U ≤ 10,000, 1 ≤ E ≤ 100,000) 게임을 시작할 때, 캐릭터의 경험치는 0이다.

출력 형식
출력의 첫 줄에 캐릭터가 얻을 수 있는 경험치의 최대량을 출력한다. 다음 줄에 수행한
컨텐츠의 개수를 출력한다. 다음 줄에 수행한 컨텐츠의 번호를 중복없이 모두 출력한다.
컨텐츠들의 번호는 1이상 N이하이며, 컨텐츠 번호 출력 순서는 상관이 없다. 캐릭터가 얻을
수 있는 경험치의 최대량이 0인 경우는 없다. 답이 여러 가지인 경우 그 중 아무거나 하나
출력한다.

입력 예제
100
3
40 200
50 150
30 180
출력 예제
380
2
1 3
채점 방식
입력 케이스들 각각에 대해 동일한 점수가 배분된다. 특이사항으로, 만약 경험치의 최대량을
출력하였지만 수행한 컨텐츠 정보를 출력하지 않을 경우에는 테스트케이스 마다 배분된
점수의 50%를 받는다. 단, 틀린 컨텐츠 정보를 출력할 경우에는 점수를 받지 못한다.

해설
확인해야 하는 경우의 수가 많은 문제이다. 기본적으로 Knapsack과 유사한 구조를 가지고
있다. 동적 계획법을 이용해서 반복적으로 확인되는 경우들을 계산하는 양을 줄일 수 있다.
"""

data = [{'indexNumber': 0,'stamina' : 10000, 'exp' : 0, 'priority' : 0 }]
xNumbers, yNumbers = 0, 0
stamina = int(input())
contentNumber = int(input())

# 데이터 준비
for i in range(contentNumber):
	numbers = input().split()
	xNumbers = int(numbers[0])  # key : stamina
	yNumbers = int(numbers[1])  # value : exp
	priority = yNumbers // xNumbers  # 우선순위 (가치) = exp/stamina
	data = data + [{'indexNumber': i+1, 'stamina' : xNumbers, 'exp' : yNumbers, 'priority' : priority}]

# for i in range(6):
# 	print(data[i])

newdata = (sorted(data, key=lambda data: data['priority'], reverse=True))

for i in range(len(newdata)):
	print(newdata[i])
# {'indexNumber': 5, 'stamina': 15, 'exp': 250, 'priority': 16}
# {'indexNumber': 4, 'stamina': 20, 'exp': 155, 'priority': 7}
# {'indexNumber': 3, 'stamina': 30, 'exp': 180, 'priority': 6}
# {'indexNumber': 1, 'stamina': 40, 'exp': 200, 'priority': 5}
# {'indexNumber': 2, 'stamina': 50, 'exp': 150, 'priority': 3}
# {'indexNumber': 0, 'stamina': 10000, 'exp': 0, 'priority': 0}

print(stamina - newdata[0]['stamina'])

cnt = 0
while(stamina > 0) :
	if (stamina - newdata[cnt]['stamina'] < 0) :
		break
	stamina = stamina - newdata[cnt]['stamina']
	cnt += 1

print(stamina)
# 여기서 부터 .... 우선순위는 높지만 스태미나가 많은 경우를 처리...
