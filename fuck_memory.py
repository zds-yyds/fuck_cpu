def consume_memory_mb(mb):
    # 1 MB = 1024 KB = 1024 * 1024 bytes
    one_mb_data = b'0' * (1024 * 1024)

    data = b''
    for _ in range(mb):
        data += one_mb_data

if __name__ == '__main__':
    # 消耗 100 MB 内存
    consume_memory_mb(1024)