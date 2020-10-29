//gcc src.c -o main -z noexecstack -fstack-protector-explicit -no-pie -z now -s
#include<stdio.h>
#include<string.h>
#include<stdlib.h>

void func()
{
	char buf[0x20];
	memset(buf,0,0x20);
	puts("D0 U KnOw PLT&GOT?");
	read(0,buf,0x50);
	// scanf("%s",buf);
}
void my_init()
{
	setvbuf(stdin,0LL,2,0LL);
	setvbuf(stdout,0LL,2,0LL);
	setvbuf(stderr,0LL,2,0LL);
//	return alarm(0xF);
}
int main()
{
	my_init();
	func();
}
