from crontab import CronTab

class CronJobManager:
    def __init__(self):
        self.cron = CronTab(user=True)

    def add_cron_job(self, program_names, unique_id, schedule):
        # Iterate over the program names and create a cron job for each
        for program_name in program_names:
            # Construct the command for running the program
            command = f'python3 /home/jeevesh/cron/{program_name}.py'

            # Add a new cron job with the unique ID
            job = self.cron.new(command=command)
            job.set_comment(unique_id)

            # Set the cron schedule
            job.setall(schedule)

        # Write the updated crontab
        self.cron.write()

    def delete_cron_job(self, unique_id):
        # Iterate over each cron job
        for job in self.cron:
            # Check if the job's comment matches the unique ID
            if job.comment == unique_id:
                # Remove the job
                self.cron.remove(job)

        # Write the updated crontab
        self.cron.write()

manager = CronJobManager()
program_names = ['hello', 'hello', 'hello']
unique_id = input("Enter a unique id")
schedule = '*/2 * * * *'
manager.add_cron_job(program_names, unique_id, schedule)  # Add cron jobs for multiple programs with the same unique ID
#manager.delete_cron_job(unique_id)  # Delete the cron jobs with the unique ID
