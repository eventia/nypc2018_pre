#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int n, S[100000];

void print_array(){
	for (int i=0; i<n; i++)
		printf("%d ", S[i]);
	printf("\n");
}

void swap(int a, int b){
	int t = S[a];
	S[a] = S[b];
	S[b] = t;
}

selection_sort(void){
	for (int i=0; i<n-1; i++)
		for (int j=i+1; j<n; j++)
			if (S[i] > S[j])
				swap(i,j);
}

int main()
{
	srand(time(NULL));
	scanf("%d", &n);
	for (int i=0; i<n; i++)
		S[i] = rand();
		
	int start = clock();
	
	selection_sort();
	
	printf("result = %.3lf(sec)\n", (double)(clock()-start)/CLOCKS_PER_SEC);
		
	return 0;
}
