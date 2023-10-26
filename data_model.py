from pydantic import BaseModel
from enum import Enum, IntEnum
from typing import List, Optional
from datetime import time, datetime, date

class DaysofWeek (IntEnum):
    monday = 0
    tuesday = 1
    wednesday = 2
    thursday = 3
    friday = 4
    saturday = 5
    sunday = 6

class ExclusionReasons (Enum):
    national_holiday = 0
    holiday_weekend = 1
    birthday = 2

class Recurrence (Enum):
    daily = 0
    weekly = 1
    monthly = 2
    annually = 3

class Owner (Enum):
    Marshall = 0
    Isabelle = 1

class Task (BaseModel):
    name: str
    days_of_week: List[DaysofWeek]
    exclusion_reasons: List[ExclusionReasons]
    recurrence: Recurrence
    time: time
    address: str
    owner: List[Owner]

class Whereabout (BaseModel):
    location: str
    start_time: datetime
    end_time: datetime

class Calendar (BaseModel):
    whereabouts: List[Whereabout]

class Holiday (BaseModel):
    name: str
    exclusion_reason: ExclusionReasons
    date: date

class Event (BaseModel):
    date: datetime
    location: str
    title: str
    owner: List[Owner]


