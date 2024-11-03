import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

class EmailSender:
    def __init__(self, from_email, password, to_email, smtp_server="smtp.gmail.com", port=587):
        self.from_email = from_email
        self.password = password
        self.to_email = to_email
        self.smtp_server = smtp_server
        self.port = port

    def send_email(self, subject, body, pdf_filename):
        msg = MIMEMultipart()
        msg['From'] = self.from_email
        msg['To'] = self.to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        with open(pdf_filename, "rb") as pdf_file:
            pdf_attachment = MIMEApplication(pdf_file.read(), _subtype="pdf")
            pdf_attachment.add_header('Content-Disposition', 'attachment', filename=pdf_filename)
            msg.attach(pdf_attachment)

        # Send the email
        with smtplib.SMTP(self.smtp_server, self.port) as server:
            server.starttls()
            server.login(self.from_email, self.password)
            server.sendmail(self.from_email, self.to_email, msg.as_string())
