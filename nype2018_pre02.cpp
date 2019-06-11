/*
�¸��� ã��
�켺�̴� īƮ���̴��� ���� �����̴�. 
�켺�̴� �׻� ģ���� ���� ������ ������ ���ٴ� ������ ��� �Ѵ�. 
������ ������ �÷��̾���� �����ð��� �־����� ��, 
��� ���� �̰������ ����ϴ� ���α׷��� ����� ����.

īƮ���̴��� ���������� ���ǵ����� �ִ�. 
���� ���� ���� ��� ���� ������, 
���� ���ǻ� �׻� 4:4 ���Ӹ� ����Ǿ��ٰ� �����Ѵ�.

���������� 1������ ���� ����� ���� ���� �¸��Ѵ�.

���ǵ����� ������� ������ �ջ��Ͽ� �� ���� ������ ȹ���� ���� �¸��Ѵ�.

A. ���� ������ ���ٸ�, 1������ ���� ����� ���� ���� �¸��Ѵ�.
B. ��� �� ȹ�� ������ �Ʒ��� ����.
1��	10��
2��	8��
3��	6��
4��	5��
5��	4��
6��	3��
7��	2��
8��	1��
��Ÿ�̾�(*)	0��
 C. 1��� 10�� �̻� ���̰� ���� ��Ÿ�̾�� 0���� ȹ���Ѵ�. 
 
�Է� ����
ù �ٿ� �׽�Ʈ ���̽��� �� T�� �־�����. (1 �� T �� 100)

�� �׽�Ʈ ���̽��� 9���� �ٷ� �����Ǿ� �ִ�. 
�׽�Ʈ ���̽��� ù �ٿ��� ������ ������ ������ ���̶�� ��item����, 
���ǵ� ���̶�� ��speed���� �Է����� �־�����. 
�� ��° �ٺ��� �� �ٸ��� �÷��̾��� ��(red, blue)�� 
�� �÷��̾ ������ �ð��� ��m:ss.xx���� ���·� �־�����. 
�� ������ red�� 4��, blue�� 4������ �����Ǿ� �ִ�. 
1��� ��Ȯ�� 10.00�� ���̳��� �Է��� �־����� ������, 
��� �÷��̾�� 10�� �̸��� �����Ͽ��ٰ� �����Ѵ�. 
�ϳ��� ���ӿ��� ��� �÷��̾��� ���� �ð��� �ٸ���.

��� ����
�� �׽�Ʈ ���̽��� ���� ��� ���� �̰������ ����Ѵ�. 
red ���� �̰�ٸ� red��, blue ���� �̰�ٸ� blue�� ����Ѵ�.

�Է� ���� 1
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

��� ���� 1
red
blue

����:
ù ��° ���� ���������̰� 3�� �÷��̾ ���� ���� �������Ƿ� red���� �¸��Ѵ�.

�� ��° ���� ���ǵ����̰�, 3->7->1->4->5->6->8->2 �� ������� �����Ͽ����� 
6, 8, 2�� ������ 10�� �̻� ���̰� ���� ��Ÿ�̾�� ������ ���� �� ����. 
red ���� 10 + 4 = 14 ���̰�, blue ���� 8 + 6 + 5 = 19 ���� ȹ���Ͽ� blue���� �¸��Ѵ�.

ä�� ���
�Է� ���̽����� ������ ���� ������ �����Ǹ�, 
�� ������ ���̽��� �� ���߾�� �� ������ ������ ������ ���� �� �ִ�.

���� 1 (15��): ������ ���� ����.
���� 2 (35��): �� �÷��̾ ������ �ð��� ������������ ���ĵ� ���·� �־���.
���� 3 (50��): ���ٸ� �������� ����.

�ؼ�  
�� ���� ����� ����� �޾� ��� ���� �¸��ߴ��� �˾Ƴ���� �Ѵ�. 
�¸��� ���� ���ϴ� ����� ��� ����� �켱������ �־��� �־� 
�״�� ���α׷��ϸ� ���� ���� �� �ִ�.
*/
//#define DEBUG 1
#include <stdio.h>
#include <stdlib.h>
int speedScore(int(*time)[8]);

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
