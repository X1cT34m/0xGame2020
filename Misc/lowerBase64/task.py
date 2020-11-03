from base64 import b64encode
from secret import flag

assert min([i in "abcdefghijklmnopqrstuvwxyz0123456789-{}" for i in flag])

print((b64encode(flag.encode()).decode().lower()))
# mhhnyw1lezviodq1ntkxltmwmditngjlny1hzgi5lwu4m2q1ntcymtblnx0=
