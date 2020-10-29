//gcc src.c -o main -z noexecstack -fstack-protector-explicit -no-pie -z now -s -m32
#include<stdio.h>
#include<string.h>
#include<stdlib.h>

char buf[8];
void func()
{
	char buf[0x80];
	puts("Leave Your Name");
	read(0,buf,0x100);
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
	system("echo Welcome To Here,How to get the argument?");
	read(0,buf,8);
	func();
}
