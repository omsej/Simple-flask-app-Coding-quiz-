import io
import sys

def get_level_info(level):
    levels = {
        1: {
            'description': 'Level 1: Print "Hello, World!"',
            'hint': 'Use the print() function.',
            'test_code': 'print("Hello, World!")',
            'test_output': 'Hello, World!\n'
        },
        2: {
            'description': 'Level 2: Assign a value of 5 to a variable and print it.',
            'hint': 'Use the assignment operator (=) and print() function.',
            'test_code': 'x = 5\nprint(x)',
            'test_output': '5\n'
        },
        3: {
            'description': 'Level 3: Perform basic arithmetic operations. If a = 10 and b = 5 first add a and b then subtract b from a then multiply a by b then divide a over b',
            'hint': 'Use +, -, *, and / to perform arithmetic operations.',
            'test_code': 'a = 10\nb = 5\nprint(a + b)\nprint(a - b)\nprint(a * b)\nprint(a / b)',
            'test_output': '15\n5\n50\n2.0\n'
        },
        # Add more levels here...
    }
    return levels.get(level, {'description': 'Congratulations! You have completed all levels.', 'hint': '', 'test_code': '', 'test_output': ''})

def check_code(level, user_code):
    level_info = get_level_info(level)
    expected_output = level_info['test_output']
    
    # Redirect standard output to capture the user's code output
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    try:
        exec(user_code)
        output = new_stdout.getvalue()
        sys.stdout = old_stdout  # Reset standard output
        if output == expected_output:
            return f'Success! Output: {output}', True
        else:
            return f'Incorrect Output: {output}. Expected: {expected_output}', False
    except Exception as e:
        sys.stdout = old_stdout  # Reset standard output even if there's an error
        return f'Error in your code: {e}', False
