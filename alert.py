import smtplib  # Used to establish a connection with an SMTP server and send emails.
from email.mime.multipart import MIMEMultipart  # Allows creating a multipart email (can include text and attachments).
from email.mime.text import MIMEText    # Used to create the text body of the email.
from email.mime.base import MIMEBase    # Used to create attachments for the email.
from email import encoders  # Encodes the attachments (e.g., converts them to base64).
import time


# Define the error to search for
error_to_search = "ERROR"

# Log file path
log_file_path = r'D:\All Documents\Resume and interview preparation\GitHub\python-scripting\sample.log'

# Email settings
sender_email = "Sender_Email@gmail.com"
receiver_email = "Receiver_Email@gmail.com"
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_user = "Sender_Email@gmail.com"
smtp_password = "Password"  # Update with your Gmail app-specific password

# Function to read log file and find the error
def check_error_in_log(log_file_path, error_to_search):
    with open(log_file_path, 'r') as file:
        logs = file.readlines()

    error_logs = [log for log in logs if error_to_search in log]
    return error_logs

# Function to send email with attached log file
def send_email_with_attachment(error_logs):
    # Set up the MIME
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    
    # Make subject line as the first error message
    subject_line = f"Error Logs: {error_logs[0].strip()}"
    msg['Subject'] = subject_line

    # Add the body to the email
    body = "Please find the attached error logs."
    msg.attach(MIMEText(body, 'plain'))

    # Attach the error log
    log_file_content = "\n".join(error_logs)
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(log_file_content)
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="error_logs.txt"')
    msg.attach(part)

    # Set up the server and send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Main script to check every minute
while True:
    error_logs = check_error_in_log(log_file_path, error_to_search)
    if error_logs:
        send_email_with_attachment(error_logs)
    else:
        print("No errors found in the log.")
    
    # Wait for 1 minute before checking again
    time.sleep(60)  # 60 seconds = 1 minute
