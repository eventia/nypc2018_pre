#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int n, S[100000];

int main()
{
	srand(time(NULL));
	scanf("%d", &n);
	for (int i=0; i<n; i++)
		S[i] = rand();
	return 0;
}
