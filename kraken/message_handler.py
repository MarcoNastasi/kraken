import yaml
from smtplib import SMTP_SSL as SMTP
from email.message import EmailMessage
import logging


class Message_handler(object):
    def __init__(self):
        self.config = yaml.safe_load(open("config.yml"))

    def handler(self, receivers: list, title: str, message: str):
        """
        Checks which handler is supposed to be used for the message
        """
        for receiver in receivers:
            try:
                if receiver not in list(self.config["recipients"].keys()):
                    # If the recipient is not in the configured list, do not do anything further and send feedback
                    pass
                if "email" in list(self.config["recipients"]["subscribers"].keys()):
                    self.send_email(receiver, title, message)
            except Exception as e:
                print(e)

    def send_email(self, recipient, title, message):
        """
        Send email to recipient
        """
        msg = EmailMessage()
        msg.set_content(message)
        msg["subject"] = title
        msg["From"] = self.config["senders"]["Email"]["From"]
        msg["To"] = ", ".join(self.config["recipients"][recipient]["email"])
        destination = self.config["recipients"][recipient]["email"]
        SMTPserver = self.config["senders"]["Email"]["smtpurl"]

        conn = SMTP(SMTPserver, self.config["senders"]["Email"]["smtpport"])
        conn.login(
            self.config["senders"]["Email"]["From"],
            self.config["senders"]["Email"]["smtppass"],
        )
        try:
            conn.sendmail(
                self.config["senders"]["Email"]["From"], destination, msg.as_string()
            )
        except Exception as e:
            print(e)
        finally:
            conn.quit()
