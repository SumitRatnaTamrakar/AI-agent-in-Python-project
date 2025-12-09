from functions.write_file_content import write_file_content

def test():
    result = write_file_content("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result)

    result = write_file_content("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result)

    result = write_file_content("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result)


if __name__ == "__main__":
    test()