//gcc src.c -o main -z noexecstack -fstack-protector-explicit -no-pie -z now -s -masm=intel -g
#include <unistd.h>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
char buf[8];
void func2()
{
	size_t r;
	size_t t;
	int fd = open("/dev/urandom",0);
	read(fd,&r,8);
	close(fd);
	puts("Please input A Number");
	scanf("%lld",&t);
	if( t == r)
	{
		system("echo C0ngratulations");
	}
}
void func()
{
	char buf[0x49];
	puts("Have A Good Time!");
	read(0,buf,0x100);
	__asm__("xor rdi,rdi;"
			"xor rsi,rsi;"
			"xor rdx,rdx;"
			"xor rcx,rcx;"
			"xor rbx,rbx;"
			"xor rax,rax;"
			"xor R8,R8;"
			"xor R9,R9;"
			"xor R10,R10;"
			"xor R11,R11;"
			"xor R12,R12;"
			"xor R13,R13;"
			"xor R14,R14;"
			"xor R15,R15;");
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
