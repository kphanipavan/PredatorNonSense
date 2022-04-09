import time
EC_IO_FILE = '/sys/kernel/debug/ec/ec0/io'

try:
    open(EC_IO_FILE, 'rb')
except PermissionError:
    print('Run the file with sudo permissions')
    exit(1)
except FileNotFoundError:
    print('Write Support Not Enabled for the EC...')
    import subprocess as sp
    sp.Popen(['modprobe', 'ec_sys', 'write_support=1'])
    print('Try restarting the application, Changes made to EC...')



def ec_write(addr, value):
    with open(EC_IO_FILE, "rb+") as f:
        f.seek(addr)
        old_value = ord(f.read(1))
        if(value != old_value):
            print("                %3d => %3d" % (old_value, value))
            f.seek(addr)
            f.write(bytearray([value]))
        else:
            print("                     = %3d" % value)


def ec_read(addr):
    with open(EC_IO_FILE, "rb") as f:
        f.seek(addr)
        return ord(f.read(1))


if __name__ == '__main__':
    addr = int('0x21', 0)
    value = int('0x60', 0)
    ec_write(addr, value)

    time.sleep(0.25)
    value = int('0x50', 0)
    ec_write(addr, value)
