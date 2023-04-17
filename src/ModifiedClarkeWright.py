from utils import *
from constraints import *
from models import *


class ModifiedClarkWright:
    def __init__(self, node_demands, node_distances, constraints, origin):
        # self.vehicles = vehicles
        self.node_demands = node_demands
        self.node_distances = node_distances
        self.constraints = constraints
        self.origin = origin
        self.savings_list = []
        self.plans = []

    def calc_distance_saving(self, i, j):
        origin_to_i_distance = self.get_distance(self.origin, i)
        origin_to_j_distance = self.get_distance(self.origin, j)
        i_to_j_distance = self.get_distance(i, j)

        if origin_to_i_distance and origin_to_j_distance and i_to_j_distance:
            return (origin_to_i_distance + origin_to_j_distance - i_to_j_distance) * LENGTH_CHARGE

        return 0

    def get_distance(self, i, j):
        return next(x for x in self.node_distances if (x[0] == i and x[1] == j) or (x[0] == j and x[1] == i))

    def calc_savings(self):
        # for time in range(0, self.time_horizon):
        #     for vehicle in self.vehicles:
        #         if vehicle.available == False: continue
        #         for i in self.G.nodes:
        #             for j in self.G.nodes:
        #                 if i != j and i != 'A' and j != 'A' and j < i:
        #                     self.savings_list.append({"saving": self.calc_saving(G, i, j), "i": i, "j": j})

        # for time_i in self.node_demands:
        #     for time_j in self.node_demands:
        #         for node_i in self.node_demands[time_i]:
        #             for node_j in self.node_demands[time_j]:
        #                 quantity = self.calc_distance_saving(node_i, node_j)
        #                 self.savings_list.append(
        #                     Saving(i=node_i, j=node_j, time=time, quantity=quantity))

        # for node_demands in range(0, self.node_demands):
        #     for i in self.G.nodes:
        #         for j in self.G.nodes:
        #             if i != 'A' and j != 'A' and j < i:
        #                 quantity = self.calc_distance_saving(G, i, j)
        #                 self.savings_list.append(
        #                     Saving(i=i, j=j, time=time, quantity=quantity))

        self.savings_list.sort(
            key=lambda saving: saving.quantity, reverse=True)

    def get_plan(self, node):
        for plan in self.plans:
            if node in plan.route:
                return plan
        return None

    def node_is_interior(self, node):
        plan = self.get_plan(node)
        if plan is not None:
            index = plan.route.index(node)
            if index == 1 or index == len(plan.route) - 2:
                return False
        return True

    def check_constraints(self, route):
        for constraint in self.constraints:
            if not constraint(route):
                return False
        return True

    def get_time_to_reach_node(self, G, route, target_node):
        time = 0
        prev_node = None
        for node in route:
            if prev_node is not None:
                time += G.get_edge_data(prev_node,
                                        node)['distance'] / VEHICLE_SPEED
            if node == target_node:
                break
            prev_node = node
        return time

    def check_saving(self, route, saving):
        for node in route:
            pass

    def process_saving(self, saving):
        i = saving["i"]
        j = saving["j"]
        plan_i = self.get_plan(i)
        plan_j = self.get_plan(j)
        remove_plan_i = False
        remove_plan_j = False
        new_route = None
        if plan_i is None and plan_j is None:
            new_route = ['A', i, j, 'A']
        elif plan_i is not None and plan_j is None and not self.node_is_interior(i):
            if plan_i.route.index(i) == 1:
                new_route = ['A', j] + plan_i.route[1:]
            else:
                new_route = plan_i.route[:-1] + [j, 'A']
            remove_plan_i = True
        elif plan_i is None and plan_j is not None and not self.node_is_interior(j):
            if plan_j.route.index(j) == 1:
                new_route = ['A', i] + plan_j.route[1:]
            else:
                new_route = plan_j.route[:-1] + [i, 'A']
            remove_plan_j = True
        elif plan_i is not None and plan_j is not None and not self.node_is_interior(i) and not self.node_is_interior(j):
            if plan_i.route.index(i) == 1 and plan_j.route.index(j) == 1:
                new_route = plan_j.route[len(
                    plan_j.route) - 2::-1] + plan_i.route[1:]
                remove_plan_i = True
                remove_plan_j = True
            elif plan_i.route.index(i) == 1 and plan_j.route.index(j) == len(plan_j.route) - 2:
                new_route = plan_j.route[:-1] + plan_i.route[1:]
                remove_plan_i = True
                remove_plan_j = True
            elif plan_i.route.index(i) == len(plan_i.route) - 2 and plan_j.route.index(j) == 1:
                new_route = plan_i.route[:-1] + plan_j.route[1:]
                remove_plan_i = True
                remove_plan_j = True
            else:
                new_route = plan_i.route[len(
                    plan_i.route) - 2::-1] + plan_j.route[1:]
                remove_plan_i = True
                remove_plan_j = True
        else:
            pass

        if new_route is not None and self.check_constraints(new_route):
            if remove_plan_i:
                self.plans.pop(self.plans.index(plan_i))
            if remove_plan_j:
                self.plans.pop(self.plans.index(plan_j))
            plan = Plan(new_route)
            self.plans.append(plan)

    def solve(self):
        self.calc_savings()
        for saving in self.savings_list:
            self.process_saving(saving)
