from data_model import ExclusionReasons
from data_model import DaysofWeek
# get all info needed
def invite_info(the_date, cal_info, events, task_info, holiday_list):
    pass

#if task_info.:
def is_feasible(the_date, task_info, holiday_list, cal_info):
    # is it on an exclusion date defined in the task?
    
    for holiday in holiday_list:
        if holiday.exclusion_reason in task_info.exclusion_reasons:
            if holiday.date == the_date.date():
                return False
            
    # if the_date.weekday() in task_info.days_of_week:
    if not DaysofWeek(the_date.weekday()) in task_info.days_of_week:
        return False
    
    # for the_date what is our whereabouts.location?
    # does our whereabouts location = task_info.address?
    for a_whereabout in cal_info.whereabouts:
        if the_date > a_whereabout.start_time and the_date < a_whereabout.end_time:
            if a_whereabout.location == task_info.address:
                return True
    return False

    # for whereabout in cal_info.whereabouts:
    #    if whereabout.start_time <= the_date <= whereabout.end_time:
    #        return False
   

#         does not match exclusion reasons
#         Will it already have been scheduled in specified time period?
#         Are we in location at time recommended?
#         Is it within time period?
#     Schedule task/s
#         Invite date
#         Invite time
#         Invite location
#         Invite task
#         Recurrence rules

# Assignment: Write the code for the task_maker function.  It should take the following inputs:
#     today's date
#     calendar information
#     events