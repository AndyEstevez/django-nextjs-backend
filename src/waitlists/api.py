from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router

from ninja_jwt.authentication import JWTAuth

from .models import WaitlistEntry
from .schemas import WaitlistEntryListSchema, WaitlistEntryDetailSchema, WaitlistEntryCreateSchema

router = Router()

# /api/waitlists/
@router.get("", response=List[WaitlistEntryListSchema], auth=JWTAuth())
def list_waitlist_entries(request):
    qs = WaitlistEntry.objects.all()
    return qs

# /api/waitlists/'
@router.post("", response=WaitlistEntryDetailSchema)
def create_waitlist_entry(request,
data:WaitlistEntryCreateSchema):
    print(data)
    obj = WaitlistEntry.objects.create(**data.dict())
    return obj

@router.get("{entry_id}/", response=WaitlistEntryDetailSchema, auth=JWTAuth())
def get_waitlist_entry(request, entry_id:int):
    obj = get_object_or_404(WaitlistEntry, id=entry_id)
    return obj

