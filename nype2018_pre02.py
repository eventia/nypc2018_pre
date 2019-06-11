"""
승리팀 찾기
우성이는 카트라이더를 즐기는 유저이다. 우성이는 항상 친구가 많기 때문에 개인전 보다는 팀전을 즐겨 한다. 게임의 종류와 플레이어들의 도착시간이 주어졌을 때, 어느 팀이 이겼는지를 계산하는 프로그램을 만들어 보자.

카트라이더는 아이템전과 스피드전이 있다. 팀은 레드 팀과 블루 팀이 있으며, 문제 편의상 항상 4:4 게임만 진행되었다고 가정한다.

아이템전은 1등으로 들어온 사람이 속한 팀이 승리한다.

스피드전은 등수별로 점수를 합산하여 더 높은 점수를 획득한 팀이 승리한다.

A. 만약 점수가 같다면, 1등으로 들어온 사람이 속한 팀이 승리한다.
B. 등수 별 획득 점수는 아래와 같다.
1등	10점
2등	8점
3등	6점
4등	5점
5등	4점
6등	3점
7등	2점
8등	1점
리타이어(*)	0점
 C. 1등과 10초 이상 차이가 나면 리타이어로 0점을 획득한다.
입력 형식
첫 줄에 테스트 케이스의 수 T가 주어진다. (1 ≤ T ≤ 100)

각 테스트 케이스는 9개의 줄로 구성되어 있다. 테스트 케이스의 첫 줄에는 게임의 종류가
아이템 전이라면 ‘item’이, 스피드 전이라면 ‘speed’가 입력으로 주어진다.
두 번째 줄부터 각 줄마다 플레이어의 팀(red, blue)과 각 플레이어가 도착한 시간이
‘m:ss.xx’의 형태로 주어진다. 각 게임은 red팀 4명, blue팀 4명으로 구성되어 있다.
1등과 정확히 10.00초 차이나는 입력은 주어지지 않으며, 모든 플레이어는 10분 미만에
골인하였다고 가정한다. 하나의 게임에서 모든 플레이어의 도착 시간은 다르다.

출력 형식
각 테스트 케이스에 대해 어느 팀이 이겼는지를 출력한다. red 팀이 이겼다면 red를, blue 팀이 이겼다면 blue를 출력한다.

입력 예제 1

2
item
blue 2:01.12
red 2:13.44
red 1:56.33
blue 2:03.31
red 2:04.84
red 2:06.67
blue 1:58.14
blue 2:07.31
speed
blue 2:01.12
red 2:13.44
red 1:56.33
blue 2:03.31
red 2:04.84
red 2:06.67
blue 1:58.14
blue 2:07.31
출력 예제 1
red
blue
설명:
첫 번째 경기는 아이템전이고 3번 플레이어가 제일 먼저 들어왔으므로 red팀이 승리한다.

두 번째 경기는 스피드전이고, 3->7->1->4->5->6->8->2 번 순서대로 골인하였지만 6, 8, 2번 유저는 10초 이상 차이가 나서 리타이어로 점수를 받을 수 없다. red 팀은 10 + 4 = 14 점이고, blue 팀은 8 + 6 + 5 = 19 점을 획득하여 blue팀이 승리한다.

채점 방식
입력 케이스들은 다음과 같은 종류로 구별되며, 한 종류의 케이스를 다 맞추어야 그 종류에 배정된 점수를 받을 수 있다.

종류 1 (15점): 아이템 전만 있음.
종류 2 (35점): 각 플레이어가 도착한 시간이 오름차순으로 정렬된 상태로 주어짐.
종류 3 (50점): 별다른 제약조건 없음.
해설
두 팀이 경기한 결과를 받아 어느 팀이 승리했는지 알아내어야 한다. 승리한 팀을 정하는 방법이 몇가지 방법과 우선순위로 주어져 있어 그대로 프로그램하면 답을 구할 수 있다.
"""

# memberData = {}
count = int(input())   # count = 2
rteam, bteam = [], []
for caseNumber in range(count):

    mode = input()
#    print(mode)  # item
    for memberData in range(8):
        memberData = input()    # "blue 2:01.12"
        teamTime = memberData.split()
        checkTime = (int(teamTime[1][0])*60 + int(teamTime[1][2:4]))*100+int(teamTime[1][5:7])
        if (teamTime[0]=="blue"):
            bteam.append(checkTime)
        else :
            rteam.append(checkTime)

#    print("bteam = ", bteam)
#    print("rteam = ", rteam)
    allteam = bteam + rteam
#    print("allteam = ", allteam)

    if mode == ('item'):
        # 각 팀의 1등끼리만 비교
        if(min(bteam) > min(rteam)):
            print("blue")
        else :
            print("red")
    else :
        # 각 팀의 순위를 매기고 점수를 결정
        rteamRecord = [8,8,8,8]
        bteamRecord = [8,8,8,8]
        rteamScore = 0
        bteamScore = 0

        refGrade = min(min(bteam), min(rteam))
        for myGrade in range(4):
            for othersGrade in range(8):
                if (rteam[myGrade] < allteam[othersGrade]) :
                    rteamRecord[myGrade] -= 1
                if (bteam[myGrade] < allteam[othersGrade]) :
                    bteamRecord[myGrade] -= 1

        for cnt in range(4):
            scoreTable = {1:10, 2:8, 3:6, 4:5, 5:4, 6:3, 7:2, 8:1}
            for i in range(8):
                if (rteamRecord[cnt] == i) & (rteam[cnt]- refGrade < 1000):
                    rteamScore += scoreTable[i+1]
                if (bteamRecord[cnt] == i) & (bteam[cnt]- refGrade < 1000):
                    bteamScore += scoreTable[i+1]

#        print(bteamRecord, rteamRecord, bteamScore, rteamScore)
        if (bteamScore<rteamScore):
            print("blue")
        else :
            print("red")




"""
int main(){
	int numberOfTest, firstTime, bScore, rScore;
	char playtype[10];
	char str1[10], str2[20];
	int typeNumber, time[4][8]={0,};

	// test counter
	scanf("%d", &numberOfTest);
	#ifdef DEBUG
	printf("%d\n", numberOfTest);
	#endif

	// loop of test counter
	for (int i=0; i<numberOfTest; i++){

		// if - playtype is item or speed ?
		// typeNumber = {item : 0, speed : 1}
		scanf("%s", playtype);
		if (playtype[0]=='i') {
			typeNumber = 0;
			#ifdef DEBUG
			printf("itemplayer\n");
			#endif
		}
		else {
			typeNumber = 1;
			#ifdef DEBUG
			printf("speedplayer\n");
			#endif
		}

		// record 8 runners data
		for (int i=0; i<8; i++){

			// each runners' team name and time record
			scanf("%s %s", str1, str2);

			if (str1[0]=='b') time[0][i] = 0; // [0][] :: blue = 0, red = 1
			else time[0][i] = 1;
			#ifdef DEBUG
			printf("%d\n", time[0][i]);
			#endif

			// time[1][] :: tick
			time[1][i] = (str2[0]-'0')*6000+(str2[2]-'0')*1000+(str2[3]-'0')*100+(str2[5]-'0')*10+(str2[6]-'0')*1;
			#ifdef DEBUG
			printf("%d\n", time[1][i]);
			#endif
		}

		// initialize
		for (int i=0; i<8; i++) time[2][i] = 0;

		for (int i=0; i<8; i++){
			// sequence numbering
			for (int j=0; j<8; j++){
				if (time[1][i] > time[1][j]) time[2][i]++;
			}
		}



		// for item league, the winner is ...
		if(playtype[0] == 'i') {
			for(int i=0; i<8; i++)
				if(time[2][i]==0){

					firstTime = time[1][i] ;
					#ifdef DEBUG
					printf("firstTime = %d\n", firstTime); // 11633
					#endif
					if(time[0][i]==0) {
						#ifdef DEBUG
						printf("item ");
						#endif
						printf("blue\n");
					}
					else {
						#ifdef DEBUG
						printf("item ");
						#endif
						printf("red\n");
					}
				}
		}
		else {
			for(int i=0; i<8; i++){
				if(time[1][i] - firstTime < 1000) {
					if(time[2][i]==0) time[3][i] = 10;
					if(time[2][i]==1) time[3][i] = 8;
					if(time[2][i]==2) time[3][i] = 6;
					if(time[2][i]==3) time[3][i] = 5;
					if(time[2][i]==4) time[3][i] = 4;
					if(time[2][i]==5) time[3][i] = 3;
					if(time[2][i]==6) time[3][i] = 2;
					if(time[2][i]==7) time[3][i] = 1;
				}
			}



			bScore = 0;
			rScore = 0;
			for(int i=0; i<8; i++){
				if (time[0][i]==0) {
					bScore += time[3][i];
				}
				else rScore += time[3][i];
			}

			#ifdef DEBUG
			printf("blue = %d, red = %d\n",bScore, rScore );
			#endif
			if (bScore > rScore) printf("blue\n");
			else printf("red\n");
		}
		// print sequence
		#ifdef DEBUG
		for(int i=0; i<8; i++) printf("sequence :: %d %d %d %d\n", time[0][i],time[1][i],time[2][i], time[3][i] );
		#endif
	}
	return 0;
}

// for later study ...
int speedScore(int(*time)[8]){
	printf("bluuuuue\n");
	return 0;
}
"""
