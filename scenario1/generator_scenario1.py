import csv
import socket
import struct
import random

node_path = 'router.csv'
node_header = ['id:ID(Router)', 'ip:STRING', 'creationDate:LONG']

relation_path = 'relation.csv'
relation_header = [':START_ID(Router)', ':END_ID(Router)']

T7_SIZE = 1 << 20  # 1M
N = 64*1024  # 64K:1

with open(node_path, 'w', encoding='utf-8') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(node_header)
    for i in range(T7_SIZE+T7_SIZE//N):
        id = i
        ip = random.randint(0, T7_SIZE*8)
        ip = socket.inet_ntoa(struct.pack('I', socket.htonl(ip)))
        creationDate = random.randint(0, T7_SIZE*16)
        row = [str(id), ip, str(creationDate)]
        csv_writer.writerow(row)

with open(relation_path, 'w', encoding='utf-8') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(relation_header)
    for i in range(T7_SIZE):
        start_id = i
        end_id = random.randint(T7_SIZE, T7_SIZE+T7_SIZE//N-1)
        row = [str(start_id), str(end_id)]
        csv_writer.writerow(row)
