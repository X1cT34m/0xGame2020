//g++ src.c -o main -z noexecstack -fstack-protector-all -no-pie -z now -s
#include <unistd.h>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
size_t n = 0;
void func()
{
	char buf[0x20];
	puts("easyfmt for U");
	read(0,buf,0x20);
	printf(buf);
	if(n == 0x233)
	{
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
