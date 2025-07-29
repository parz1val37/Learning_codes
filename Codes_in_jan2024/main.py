# import subprocess

# process = subprocess.run("python logic.py", capture_output=True)

# counter = 0
# while float(process.stdout.strip()) < 50:
#     print(process.stdout.strip())
#     process = subprocess.run("python logic.py", capture_output=True)
#     counter += 1
    
# print(f"Got percentage higher than 50%: {process.stdout.strip()}, counted: {counter}")