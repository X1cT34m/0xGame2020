//gcc src.c -o main -z noexecstack -fstack-protector-explicit -pie -z now -s -m32
#include<stdio.h>
#include<string.h>
#include<stdlib.h>

void shell()
{
	puts("C0ngratulation!!!");
	system("cat flag");
}
void func()
{
	char buf[0x80];
	memset(buf,0,0x20);
	puts("D0 U know asm?");
	read(0,buf,0x100);
}
void my_init()
{
	setvbuf(stdin,0LL,2,0LL);
	setvbuf(stdout,0LL,2,0LL);
	setvbuf(stderr,0LL,2,0LL);
	printf("give u a magic_address %p\n",shell);
//	return alarm(0xF);
}
int main()
{
	my_init();
	func();
}
