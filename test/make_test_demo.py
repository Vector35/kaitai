#!/usr/bin/env python3
# Generates test_demo.bin matching test/demo_format.ksy

import os
import struct

records = [
    (1, b'alpha', 100),
    (2, b'beta', 200),
    (3, b'gamma', 300),
]

out = bytearray()
out += b'DEMO'                       # magic
out += struct.pack('<B', 1)          # version
out += struct.pack('<B', len(records))  # num_records
for rec_id, name, value in records:
    out += struct.pack('<H', rec_id)     # record_id  (u2le)
    out += struct.pack('<B', len(name))  # name_len   (u1)
    out += name                          # name       (ascii)
    out += struct.pack('<I', value)      # value      (u4le)

path = os.path.join(os.path.dirname(__file__), 'test_demo.bin')
with open(path, 'wb') as fp:
    fp.write(out)

print(f'wrote {path} ({len(out)} bytes)')
