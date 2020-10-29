//g++ src.c -o main -z noexecstack -fstack-protector-all -no-pie -z now -s
#include <unistd.h>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
char buf[4];
char ar[0x60];
void func()
{
	char buf[0x60];
	puts("Leave Some Message to me");
	read(0,buf,0x60);
	sprintf(ar,buf,buf);
	if(!memcmp(::buf,"FMYY",4))
	{
		printf(ar);
		system("/bin/sh");
	}
}
void my_init()
{
	setvbuf(stdin,0LL,2,0LL);
	setvbuf(stdout,0LL,2,0LL);
	setvbuf(stderr,0LL,2,0LL);
}
int main()
{
	my_init();
	func();
}
