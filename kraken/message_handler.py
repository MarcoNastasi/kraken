import yaml
import smtplib
from email.message import EmailMessage


class message_handler(object):
    def __init__(self):
        self.config = yaml.safe_load(open("config.yml"))

    def handler(self, recipients: list, title: str, message: str):
        """
        Checks which handler is supposed to be used for the message
        """
        for recipient in recipients:
            if recipient not in list(self.config["recipients"].keys()):
                # If the recipient is not in the configured list, do not do anything further and send feedback
                pass
            if 'Email' in recipient[recipient]:
                self.send_email(recipient, title, message)


    def send_email(self, recipient, title, message):
        """
        Send email to recipient
        """
        msg = EmailMessage()
        msg.set_content(message)
        msg['subject'] = title
        msg['From'] = self.config['senders']['Email']['From']
        msg['To'] = ", ".join(self.config['recipients'][recipient]['Email'])
        s = smtplib.SMTP(self.config['senders']['Email']['smtpurl'])
        s.send_message(msg)
        s.quit()
