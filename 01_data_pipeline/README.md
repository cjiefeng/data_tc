# Data pipeline
1. Let's use kubernetes `CronJob` to trigger this job everyday.  
   This can help us ensure that job will run up to certain degree of machine failure.
   Default retry is 6 times and customizable if required in the event of network failure. 
2. Chose to schedule at 1:15am since job is not crucial to run on time everyday. 
   ```
   cronjob.yaml: 
   ...
   spec: 
     schedule: "15 1 * * *"
   ...
   ```
3. Added a convenience docker-compose.yml to test locally.
   ```
   $ docker compose run process_data
   ```
   `output.csv` will be generated in this directory.
4. Given that we are using kubernetes, file might be lost after job terminates (pod terminated).  
   We should upload the output file to a persistent location or pass on to the next job.
