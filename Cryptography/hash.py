import hashlib

'''  -- Hashing Example --
name = 'Sanaullah'
hash_object = hashlib.sha256(name.encode())
hex_dig = hash_object.hexdigest()
print(f'SHA-256 hash of "{name}" is: {hex_dig}')
'''

def hash_file(file_path):
  h = hashlib.new('sha256')
  with open(file_path,'rb') as file:
    while True:
      chunk = file.read(1024)
      if not chunk:
        break
      h.update(chunk)
  return h.hexdigest()

def verify_integrity(file1, file2):
  hash1 = hash_file(file1)
  hash2 = hash_file(file2)
  print(f"\nChecking the integrity between '{file1}' and '{file2}':")
  if hash1 == hash2:
    return "File is intact. No changes detected."
  return "File has been altered or corrupted."

if __name__ == "__main__":
  file_path = 'crypto/sample_files/sample_text.txt'
  print(f'SHA-256 hash of file "{file_path}" is:\n{hash_file(file_path)}')
  print(verify_integrity(r'crypto/sample_files/sample_text.txt', r'crypto/sample_files/sample2.txt'))