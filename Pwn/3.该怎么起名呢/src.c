// gcc src.c -o main
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
	puts("Please input your shellcode");
	char *p  = malloc(0x1000);
	mprotect((p-0x10),0x1000,7);
	read(0,p,0xFFF);
	((void (*)(void))(p + 0x20))();
}
