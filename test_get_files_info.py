from functions.get_files_info import get_files_info

print("Result for current directory:")
result = get_files_info("calculator", ".")
split_result = result.split('\n')
for line in split_result:
    print("  " + line)
""" 
Expected output:
Result for current directory:
  - main.py: file_size=719 bytes, is_dir=False
  - tests.py: file_size=1331 bytes, is_dir=False
  - pkg: file_size=44 bytes, is_dir=True
 """

print("Result for 'pkg' directory:")
result_2 = get_files_info("calculator", "pkg")
split_result_2 = result_2.split('\n')
for line in split_result_2:
    print("  " + line)
""" 
Expected output:
Result for 'pkg' directory:
  - calculator.py: file_size=1721 bytes, is_dir=False
  - render.py: file_size=376 bytes, is_dir=False
 """

print("Result for '/bin' directory:")
result_3 = get_files_info("calculator", "/bin")
split_result_3 = result_3.split("\n")
for line in split_result_3:
    print("  " + line)
""" 
Expected output:
Result for '/bin' directory:
    Error: Cannot list "/bin" as it is outside the permitted working directory
 """

print("Result for '../' directory:")
result_4 = get_files_info("calculator", "../")
split_result_4 = result_4.split("\n")
for line in split_result_4:
    print("  " + line)
""" 
Expected output:
Result for '../' directory:
    Error: Cannot list "../" as it is outside the permitted working directory
 """
