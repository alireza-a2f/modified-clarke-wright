import pandas as pd
import math
from constraints import *
from models import *


def get_edge_distances_from_excel(excel_file):
    data = pd.read_excel(excel_file, sheet_name=["Distance"], index_col=0)
    distances = data.get("Distance")
    edge_list = []
    nodes = distances.columns

    for i in nodes:
        for j in nodes:
            val = distances.loc[i, j]
            if not math.isnan(val):
                edge_list.append((i, j, {"distance": val}))

    return edge_list


def get_node_demands_from_excel(excel_file):
    data = pd.read_excel(excel_file, sheet_name=["Demand"], index_col=0)

    demands = data.get("Demand")
    time_series = demands.columns
    rows = demands.index

    node_demands = {}

    for time in time_series:
        node_demands[time] = []
        for row in rows:
            details = demands.loc[row, time].split(',')
            demand = Demand(w=0, te=details[1], tl=details[2])
            node_demands[time].append(Node(name=row, demand=demand))

    return node_demands


def get_vehicles_from_excel(excel_file):
    data = pd.read_excel(excel_file, sheet_name=["Vehicle"], index_col=0)

    vehicle_details = data.get("Vehicle")
    vehicle_type_names = vehicle_details.index

    vehicles = []

    for vehicle_type_name in vehicle_type_names:
        vehicle_type = VehicleType(
            name=vehicle_type_name,
            weight_capacity=vehicle_details.loc[vehicle_type_name,
                                                'weight_capacity'],
            volume_capacity=vehicle_details.loc[vehicle_type_name,
                                                'volume_capacity'],
            max_distance=vehicle_details.loc[vehicle_type_name, 'max_distance']
        )
        for i in range(vehicle_details.loc[vehicle_type_name, 'available']):
            vehicles.append(Vehicle(type=vehicle_type))

    return vehicles


def calc_timewindow_penalty(t, demand):
    if t < demand.te or t > demand.tl:
        return TIMEWINDOW_PENALTY
    return 0
