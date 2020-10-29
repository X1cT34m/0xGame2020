// gcc src.c -o main -s
#include<stdio.h>
#include<malloc.h>
#include<string.h>
#include<stdlib.h>
void my_init()
{
	setvbuf(stdin,0LL,2,0LL);
	setvbuf(stdout,0LL,2,0LL);
	setvbuf(stderr,0LL,2,0LL);
	return alarm(0xF);
}

int main()
{
	my_init();
	puts("WelCome_To_0xCTF");
	system("/bin/sh");
}
