#include <stdio.h>

int main(){
	// 구구단 프로그램 
	int n1=1;
	while(n1){
		scanf("%d", &n1);
		for(int i=1; i<10; i++){
			printf("%d * %d = %d\n", n1, i, n1*i);	
		}
	}

	return 1;
}
