"""Main module."""
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
from message_handler import Message_handler
# Set up fast api
app = FastAPI()
security = HTTPBasic()

# Initialize message model
class Message(BaseModel):
    subject: str
    recipients: list
    contents: str

# Set up message handler, which will handle the message delivery
message_handler = Message_handler()

@app.put("/message/")
def update_message(message: Message):
    response = message_handler.handler(message.recipients, message.subject, message.contents)
    return {"message_subect": message.subject, "message_recipiens": message.recipients}
