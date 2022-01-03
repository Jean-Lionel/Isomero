#include "studio.h"

int main(int argc, char const *argv[])
{
	// Déclaration des variables
	int i,j, limit = 12;

	for(i=0; i<= 12; i++){
		for(j=0; j <= 12; j++)
			printf("%d X %d = %d \n",i,j,(i*j) );
		
		printf("\n===========================\n");
	}
	return 0;
}