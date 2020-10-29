//gcc src.c -o main -z noexecstack -fstack-protector-all -pie -z now -s -m32
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
	int a;
	int b;
	my_init();
	puts("Ezzzzzzzzzzzzz,please input the magic number");
	scanf("%lld",&b);
	if(a == 0x2333)
		system("cat flag");
	
}
