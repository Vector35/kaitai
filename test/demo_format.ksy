meta:
  id: demo_format
  title: Demo format for testing the Kaitai Binja plugin
  endian: le
  file-extension: demo
doc: |
  A tiny made-up container: a "DEMO" magic, a header, then a repeated
  array of variable-length records. Designed to exercise the tree view
  (nesting + arrays) and hex<->tree highlighting.
seq:
  - id: magic
    contents: "DEMO"
  - id: version
    type: u1
  - id: num_records
    type: u1
  - id: records
    type: record
    repeat: expr
    repeat-expr: num_records
types:
  record:
    seq:
      - id: record_id
        type: u2
      - id: name_len
        type: u1
      - id: name
        type: str
        size: name_len
        encoding: ASCII
      - id: value
        type: u4
