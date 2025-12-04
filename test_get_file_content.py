from functions.get_file_content import get_file_content
from config import MAX_CHARS

def test_lorem_truncation():
    content = get_file_content("calculator", "lorem.txt")

    # Check the length is greater than MAX_CHARS (because of the appended message):
    assert len(content) > MAX_CHARS

    # Check that it ends with the truncation message:
    assert content.endswith(
        f'[...File "lorem.txt" truncated at {MAX_CHARS} characters]'
    )

if __name__ == "__main__":
    test_lorem_truncation()

    print(get_file_content("calculator", "main.py"))
    print(get_file_content("calculator", "pkg/calculator.py"))
    print(get_file_content("calculator", "/bin/cat"))
    print(get_file_content("calculator", "pkg/does_not_exist.py"))