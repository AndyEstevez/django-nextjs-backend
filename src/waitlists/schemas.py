from datetime import datetime
from ninja import Schema
from pydantic import EmailStr  # require email to have @<email-provider>.com

class WaitlistEntryCreateSchema(Schema):
    # Create -> Data
    # WaitlistEntryIn
    email: EmailStr

class WaitlistEntryListSchema(Schema):
    # List -> Data
    # WaitlistEntryOut
    id: int
    email: EmailStr

class WaitlistEntryDetailSchema(Schema):
    # Get -> Data
    # WaitlistEntryOut
    id: int
    email: EmailStr
    updated: datetime
    timestamp: datetime