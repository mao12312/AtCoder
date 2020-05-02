import os

num = int(input())
new_dir_path = 'ABC/{}/'.format(num)
os.makedirs(new_dir_path)

file_path_list = ['a.py', 'b.py', 'c.py', 'd.py']

for i in file_path_list:
    file_path = '{0}{1}'.format(new_dir_path, i)
    with open(file_path, mode='x') as f:
        f.write(file_path)