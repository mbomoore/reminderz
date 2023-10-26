from datetime import datetime, date,time
from data_model import Recurrence, Owner,DaysofWeek, ExclusionReasons
from data_model import Task, Calendar, Whereabout, Holiday, Event
from application import invite_info
from application import is_feasible

# Test if a feasible task is feasible
def test_feasibility():
    task_info = Task(
        name = "Woob stacking",
        days_of_week = [DaysofWeek.monday, DaysofWeek.saturday],
        exclusion_reasons = [0],
        recurrence = Recurrence.monthly,
        time = time(10, 0, 0),
        address = "73 Woodcrest Lane, Milton, NY 12547",
        owner = Owner
    )
    holiday_list = [Holiday(
            name = "Memorial Day",
            exclusion_reason = ExclusionReasons.national_holiday,
            date = date(2023, 5, 29),
        )]
    cal_info = Calendar(
        whereabouts = [
            Whereabout(
                location = "73 Woodcrest Lane, Milton, NY 12547",
                start_time = datetime(2023, 10, 1, 0, 0, 0),
                end_time = datetime(2023, 10, 8, 23, 59, 0),
            )
        ]
    )    
    the_date = datetime(2023, 10, 2, 22, 41, 0)
    assert is_feasible(the_date, task_info, holiday_list, cal_info) == True   

# Test if a task is feasible on a holiday
def test_holiday_infeasibility():
    task_info = Task(
        name = "Woob stacking",
        days_of_week = [0, 6],
        exclusion_reasons = [0],
        recurrence = Recurrence.monthly,
        time = time(10, 0, 0),
        address = "73 Woodcrest Lane, Milton, NY 12547",
        owner = Owner
    )
    holiday_list = [Holiday(
            name = "Memorial Day",
            exclusion_reason = ExclusionReasons.national_holiday,
            date = date(2023, 5, 29),
        )]
    cal_info = Calendar(
        whereabouts = [
            Whereabout(
                location = "73 Woodcrest Lane, Milton, NY 12547",
                start_time = datetime(2023, 5, 29, 0, 0, 0),
                end_time = datetime(2023, 5, 29, 23, 59, 0),
            )
        ]
    )    
    the_date = datetime(2023, 5, 29, 22, 41, 0)
    assert is_feasible(the_date, task_info, holiday_list, cal_info) == False 

# Test if a task is feasible on the wrong day of week
def test_day_of_week_infeasibility():
    task_info = Task(
        name = "Woob stacking",
        days_of_week = [DaysofWeek.monday, DaysofWeek.saturday],
        exclusion_reasons = [0],
        recurrence = Recurrence.monthly,
        time = time(10, 0, 0),
        address = "73 Woodcrest Lane, Milton, NY 12547",
        owner = Owner
    ) 
    holiday_list = [Holiday(
            name = "Memorial Day",
            exclusion_reason = ExclusionReasons.national_holiday,
            date = date(2023, 5, 29),
        )]
    cal_info = Calendar(
        whereabouts = [
            Whereabout(
                location = "73 Woodcrest Lane, Milton, NY 12547",
                start_time = datetime(2023, 5, 29, 0, 0, 0),
                end_time = datetime(2023, 5, 29, 23, 59, 0),
            )
        ]
    )
    the_date = datetime(2023, 10, 3, 22, 41, 0)
    assert is_feasible(the_date, task_info, holiday_list, cal_info) == False   

# Test if a task is not feasible if you are in a different location from the task location
def test_task_location_infeasibility():
    task_info = Task(
        name = "Woob stacking",
        days_of_week = [DaysofWeek.monday, DaysofWeek.saturday],
        exclusion_reasons = [0],
        recurrence = Recurrence.monthly,
        time = time(10, 0, 0),
        address = "73 Woodcrest Lane, Milton, NY 12547",
        owner = Owner
    ) 
    holiday_list = [Holiday(
            name = "Memorial Day",
            exclusion_reason = ExclusionReasons.national_holiday,
            date = date(2023, 5, 29),
        )]
    cal_info = Calendar(
        whereabouts = [
            Whereabout(
                location = "255 West 21 St, New York, NY 10011",
                start_time = datetime(2023, 5, 29, 0, 0, 0),
                end_time = datetime(2023, 5, 29, 23, 59, 0),
            )
        ]
    )
    the_date = datetime(2023, 10, 3, 22, 41, 0)
    assert is_feasible(the_date, task_info, holiday_list, cal_info) == False  

# Recurrence test
def test_against_recurrence_rules():
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
    events = [
        Event(
            date: datetime(2023, 5, 8, 23, 59, 0)
            location: "73 Woodcrest Lane, Milton, NY 12547"
            title: "Woob stacking"
            owner: List[1]
        )
    ]

    task_info = Task(
        name = "Woob stacking",
        days_of_week = [0, 6],
        exclusion_reasons = [0],
        recurrence = Recurrence.monthly,
        time = time(10, 0, 0),
        address = "73 Woodcrest Lane, Milton, NY 12547",
        owner = [0]
    )
    holiday_list = Holiday(
            name = "Memorial Day",
            exclusion_reason = ExclusionReasons.national_holiday,
            date = date(2023, 5, 29),
        )
# Time
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
        owner = [0]
    )
    holiday_list = Holiday(
            name = "Memorial Day",
            exclusion_reason = ExclusionReasons.national_holiday,
            date = date(2023, 5, 29),
        )

# If we are in a location and a task is feasible, then propose task
def te_st_task_creation():
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
        owner = [0]
    )
    holiday_list = Holiday(
            name = "Memorial Day",
            exclusion_reason = ExclusionReasons.national_holiday,
            date = date(2023, 5, 29),
        )


    # output is cal invite with date, time, title, location
    output = invite_info(the_date, cal_info, events, task_info, holiday_list)
    assert output[0] == Event(
        datetime(2023, 5, 6, 10, 0, 0), 
        "73 Woodcrest Lane, Milton, NY 12547"
        "Woob stacking"
        "Marshall"
        )
    assert len(output) == 1

    # We can add a test here later for Owner
    




