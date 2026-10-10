class ObjectiveBuilder:
    def weighted_objective(self, cost: float, carbon: float, urgency: float, battery: float) -> float:
        return (cost * 0.35) + (carbon * 0.25) + (urgency * 0.25) + (battery * 0.15)
