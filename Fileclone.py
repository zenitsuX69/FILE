import marshal, base64, zlib
exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))