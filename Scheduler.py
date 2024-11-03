import requests
from bs4 import BeautifulSoup
from fpdf import FPDF
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import subprocess

class Scheduler:
    def __init__(self, python_path, script_path, task_name="DailyTechNewsScript"):
        self.python_path = python_path
        self.script_path = script_path
        self.task_name = task_name

    def create_task(self):
        command = (
            f'schtasks /create /tn "{self.task_name}" /tr "{self.python_path} {self.script_path}" '
            f'/sc daily /st 22:00 /rl highest /f'
        )
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
            print(result.stdout)  # Print output if needed
            print("Scheduled task created successfully.")
        except subprocess.CalledProcessError as e:
            with open('task_creation_error.log', 'w') as log_file:
                log_file.write(f"Failed to create scheduled task: {e.stderr}\n")
            print("Error logged to task_creation_error.log")


