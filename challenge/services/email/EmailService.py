import smtplib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from jinja2 import Template
import base64
import os

class EmailService():

    SENDER = "storicardchallengerueda@gmail.com"
    RECIPIENTS = []
    PASSWORD = "frfdkerdhdzkueig"
    TEMPLATE_ACCOUNT_SUMMARY = '''
        <html>
        <body>
            <h1>Aquí le enviamos su resumen de cuenta !</h1>
            <p> {{ summary }}</p>
            <p><img src="data:image/png;base64,{{ imagen_base64 }}" alt="Firma de página" /></p>
        </body>
        </html>
        '''

    def __init__(self) -> None:
        pass

    def send_account_summary(self, subject:str, RECIPIENTS:list, summary, attached_file):
        template = Template(self.TEMPLATE_ACCOUNT_SUMMARY)
        imagen_base64 = None
        image_path= os.path.join(os.path.dirname(__file__), 'Captura.PNG')
        with open(image_path, 'rb') as f:
            imagen_data = f.read()
            imagen_base64 = base64.b64encode(imagen_data).decode('utf-8')

        
        variables = {
           'summary': summary,
           'imagen_base64': imagen_base64,
           'attached_filename': "AccountSummary.csv"
            }
        
        rendered_html = template.render(variables)
        msg = MIMEMultipart('alternative')
        html_part = MIMEText(rendered_html, 'html')
        msg['Subject'] = subject
        msg['From'] = self.SENDER
        msg['To'] = ', '.join(RECIPIENTS)
        msg.attach(html_part)
        attached_content = attached_file.read()
        attached_filename = attached_file.filename
        attached_part = MIMEApplication(attached_content)
        attached_part.add_header('Content-Disposition', 'attachment', filename=attached_filename)
        msg.attach(attached_part)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(self.SENDER, self.PASSWORD)
            smtp_server.sendmail(self.SENDER, RECIPIENTS, msg.as_string())
