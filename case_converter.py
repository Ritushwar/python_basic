#Converting PascalCase to snake_case
def main():
    print(convert_to_snake('IAmUsingGithub'))

def convert_to_snake(case_to_snake):
    snake_case = [
        '_' + char.lower() if char.isupper()
        else char
        for char in case_to_snake
    ]
    return ''.join(snake_case).strip('_')

main()