import jenkins
from jenkins import JenkinsException

def trigger_jenkins_job_build(server_url, username, password, job_name):
    try:
        # Connect to Jenkins server
        server = jenkins.Jenkins(server_url, username=username, password=password)

        # Check if the job exists
        if server.job_exists(job_name):
            # Trigger a build for the job
            server.build_job(job_name)
            print(f"Build triggered for job '{job_name}'.")
        else:
            print(f"Error: Job '{job_name}' does not exist.")

    except JenkinsException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Jenkins server details
    jenkins_server_url = "http://localhost:9090/"
    jenkins_username = "Praveen"
    jenkins_password = "Pr@veen2"

    # Job details
    job_name = "TDSWeb_working"

    # Trigger Jenkins job build
    trigger_jenkins_job_build(jenkins_server_url, jenkins_username, jenkins_password, job_name)