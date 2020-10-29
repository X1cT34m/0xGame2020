//g++ src.cpp -o main -lpthread -no-pie -fstack-protector-all -z noexecstack -z now
#include <iostream>
#include <cstring>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/prctl.h>
#include <linux/filter.h>
#include <linux/seccomp.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

void my_init();
void *pthread();
void sandbox();
void get_input(char *p,unsigned short int size);
unsigned int get_end(char p[],unsigned int nbytes);
int size;
int fd[2];
int main(int argc,char *argv[])
{

	my_init();
	pthread_t thread;
	if ((pthread_create(&thread, NULL,(void *(*)(void *))pthread,NULL)) == -1)
	
	{
		std::cerr<< "Create Error   :(" << std::endl;
		return 1;
	}
	
	if(pthread_join(thread,NULL))
	{
		std::cout << "Thread Ended   :)" << std::endl;
		return 0;
	}
	
	return 0;
}

void my_init()
{
	setvbuf(stdin,0LL,2,0LL);
	setvbuf(stdout,0LL,2,0LL);
	setvbuf(stderr,0LL,2,0LL);
	sandbox();
}


void sandbox()
{
    prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0);
    struct sock_filter sfi[] ={
        {0x20,0x00,0x00,0x00000004},
        {0x15,0x00,0x05,0xC000003E},
        {0x20,0x00,0x00,0x00000000},
        {0x35,0x00,0x01,0x40000000},
        {0x15,0x00,0x02,0xFFFFFFFF},
        {0x15,0x01,0x00,0x0000003B},
        {0x06,0x00,0x00,0x7FFF0000},
        {0x06,0x00,0x00,0x00000000}
    };
    struct sock_fprog sfp = {8, sfi};
    prctl(PR_SET_SECCOMP, SECCOMP_MODE_FILTER, &sfp);
}

unsigned int get_end(char *p,unsigned int nbytes)
{
	unsigned int i = 0;
	char *t = p;
	for(; i<nbytes ; i++,t++) {
		if(*t == '\x00' || *t =='\n')
			return i;
	}
	return i;
}

void get_name(char *p,unsigned short int size)
{
	char c;
	int n = 0;
	while(n <size)
	{
		int ret = read(0,&c,1);
		if(!ret || c == '\n'){
			*((char*)p + n) = 0;
			break;
		}
		*((char*)p + n) = c;
		n++;
		
	}
}
void *pthread()
{
	char name[0x20];
	char message[0x100];
	unsigned int i = 0;
	unsigned int m = 0;
	unsigned short int nbytes = 0;
	memset(name,0,0x20);
	memset(message,0,0x100);
	std::cout << "WelC0me To 0xGame Final Week" << std::endl;
	std::cout << "The more you do it first, the more rewards you get" << std::endl;
	std::cout << "Hint1 : seccomp and orw" << std::endl;
	std::cout << "Hint2 : TLS Struct and Canary" << std::endl;
	std::cout << "\t\t\t\t\t\tBY FMYY" << std::endl;
	
	fd[0] = open("./name.txt",O_WRONLY|O_APPEND);
	fd[1] = open("./message.txt",O_WRONLY|O_CREAT|O_TRUNC);
	std::cout << "Now,you can write your id into the name.txt,only write and 24 bytes" << std::endl;
	std::cout << "Write your name: ";
	get_name(name,0x18);
	m = get_end(name,0x18);
	write(fd[0],name,m);
	write(fd[0],"\n",1);
	std::cout << "Then,Leave Some message into message.txt" << std::endl;
	std::cout << "Enter the size of message: ";
	std::cin >> size;
	if( size >= 0xF8) {
		std::cerr << "NO!,message size is too large" << std::endl;
		exit(0);
	}
	std::cout << "OK,now you can write message: ";
	nbytes = (unsigned short int)size;
	read(0,message,nbytes);
	m = get_end(message,0xF8);
	write(fd[1],message,m);
	
	std::cout << "ALL Done!\t" << "Good Bye~" << std::endl;
	close(fd[0]);
	close(fd[1]);
	return NULL;
}
