//gcc src.c -o main -z noexecstack -fstack-protector-explicit -no-pie -z now  -masm=intel -g -s
#include<stdio.h>
#include<string.h>
#include<stdlib.h>

void func()
{
	__asm__("sub rsp,0x20;"
			"mov rsi,rsp;"
			"mov rdi,0;"
			"mov rdx,0x100;"
			"mov rbx,0;"
			"push rbx;"
			"pop rax;"
			"syscall;"
			"add rsp,0x20;");
}
void my_init()
{
	return alarm(0xF);
}
int main()
{
	puts("[!] Can U Get the /bin/sh");
	func();
}
