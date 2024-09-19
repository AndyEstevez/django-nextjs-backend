from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router

from ninja_jwt.authentication import JWTAuth
import helpers
from .models import WaitlistEntry
from .schemas import WaitlistEntryListSchema, WaitlistEntryDetailSchema, WaitlistEntryCreateSchema

router = Router()



# /api/waitlists/
@router.get("", response=List[WaitlistEntryListSchema], auth=helpers.api_auth_user_required)
def list_waitlist_entries(request):
    qs = WaitlistEntry.objects.filter(user=request.user)
    return qs

# /api/waitlists/'
@router.post("", response=WaitlistEntryDetailSchema, auth=helpers.api_auth_user_or_anon)
def create_waitlist_entry(request, data:WaitlistEntryCreateSchema):
    obj = WaitlistEntry(**data.dict())
    print(request.user)
    if request.user.is_authenticated:
        # obj.user_id = request.user
        obj.user = request.user
    obj.save()
    return obj

@router.get("{entry_id}/", response=WaitlistEntryDetailSchema, auth=helpers.api_auth_user_required)
def get_waitlist_entry(request, entry_id:int):
    obj = get_object_or_404(WaitlistEntry, id=entry_id, user=request.user)
    return obj

