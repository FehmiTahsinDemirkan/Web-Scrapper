# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email import encoders
# from email.mime.text import MIMEText
#
#
# class EmailSender:
#     def __init__(self, sender_email, sender_password, smtp_server, smtp_port):
#         self.sender_email = sender_email
#         self.sender_password = sender_password
#         self.smtp_server = smtp_server
#         self.smtp_port = smtp_port
#
#     async def send_email(self, recipient_email, subject, message, attachment_path=None):
#         msg = MIMEMultipart()
#         msg['From'] = self.sender_email
#         msg['To'] = recipient_email
#         msg['Subject'] = subject
#
#         msg.attach(MIMEText(message, 'plain'))
#
#         if attachment_path:
#             attachment = open(attachment_path, "rb")
#             part = MIMEBase('application', 'octet-stream')
#             part.set_payload((attachment).read())
#             encoders.encode_base64(part)
#             part.add_header('Content-Disposition', "attachment; filename= %s" % attachment_path)
#             msg.attach(part)
#
#         with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
#             server.starttls()
#             server.login(self.sender_email, self.sender_password)
#             text = msg.as_string()
#             server.sendmail(self.sender_email, recipient_email, text)
