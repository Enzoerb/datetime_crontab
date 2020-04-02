from crontab import CronTab
import os
import getpass

username = getpass.getuser()
actual_path = os.getcwd()
python_file_path = os.path.join(actual_path, 'get_date.py')
output_path = os.path.join(actual_path, 'saida.txt')
cron_command = f'python3 {python_file_path} >> {output_path}'

my_user_cron = CronTab(user=username)
new_job = my_user_cron.new(command=cron_command)
new_job.minute.every(1)
my_user_cron.write()
