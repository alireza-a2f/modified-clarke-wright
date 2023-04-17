MAX_DISTANCE = 5
TIMEWINDOW_PENALTY = 5
STOPOFF_CHARGE = 2
TIME_HORIZON = 5
LENGTH_CHARGE = 1
VEHICLE_SPEED = 70


def stop_count_constraint(route, **kwargs):
    if len(route) <= 5:
        return True
    else:
        return False


def weight_capacity(weight, **kwargs):
    pass


def max_distance_constraint(route, **kwargs):
    for node in route:
        pass


# def demand_constraint(route):
#     for node in route:
#         pass
