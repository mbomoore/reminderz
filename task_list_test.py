from datetime import datetime, date,time
from data_model import Recurrence, Owner,DaysofWeek, ExclusionReasons, Kind
from data_model import Task, Calendar, Whereabout, Holiday, Event
from application import task_maker

# Test 0: You can't create a task without a day of the week defined
def test_task_days_of_week():
    Task(
        name="POOPOO",
        days_of_week=[4], 
        exclusion_reasons=[], 
        recurrence=Recurrence.weekly, 
        time=time(10, 0, 0), 
        address="73 Woodcrest Lane, Milton, NY 12547", 
        owner=[1])

# Test 1: If we are in a location and a task is feasible, then propose task
def test_task_creation():
    # input is  today's date, cal info and task info, exclusion/s
    the_date = datetime(2023, 5, 4, 22, 41, 0)
    cal_info = Calendar(
        whereabouts = [
            Whereabout(
                location = "73 Woodcrest Lane, Milton, NY 12547",
                start_time = datetime(2023, 5, 3, 0, 0, 0),
                end_time = datetime(2023, 5, 8, 23, 59, 0),
            )
        ]
    )    
    events = []

    task_info = Task(
        name = "Woob stacking",
        days_of_week = [0, 6],
        exclusion_reasons = [0],
        recurrence = Recurrence.monthly,
        time = time(10, 0, 0),
        address = "73 Woodcrest Lane, Milton, NY 12547",
        owner = Owner
    )
    holiday_list = Holiday(
            name = "Memorial Day",
            kind = Kind.holiday,
            date = date(2023, 5, 29),
        )
    
    # output is cal invite with date, time, title, location
    output = task_maker(the_date, cal_info, events, task_info, holiday_list)
    assert output[0] == Event(
        datetime(2023, 5, 6, 10, 0, 0), 
        "73 Woodcrest Lane, Milton, NY 12547"
        "woob stacking"
        "Marshall"
        )
    assert len(output) == 1
    




