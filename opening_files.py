# indent your Python code to put into an email
import glob

python_files = glob.glob('four.py')
for file_name in sorted(python_files):
    print('Opening file:', file_name, '\n')

    with open(file_name) as f:
        for line in f:
            print('     ' + line.rstrip())

    print()