from models.waypoint import Waypoint
from models.trajectory import Trajectory

def urban_delivery_crossing():
    """
    Scenario: Two delivery drones crossing in an urban area
    """
    primary = Trajectory([
        Waypoint(0, 0, 0),
        Waypoint(10, 10, 10)
    ])

    others = [
        {
            "id": "Delivery_Drone_A",
            "trajectory": Trajectory([
                Waypoint(10, 0, 0),
                Waypoint(0, 10, 10)
            ])
        }
    ]

    return primary, others


def emergency_priority_drone():
    """
    Scenario: Emergency drone cuts across normal traffic
    """
    primary = Trajectory([
        Waypoint(0, 5, 0),
        Waypoint(10, 5, 10)
    ])

    others = [
        {
            "id": "Emergency_Drone",
            "trajectory": Trajectory([
                Waypoint(5, -5, 0),
                Waypoint(5, 15, 8)
            ])
        }
    ]

    return primary, others


def same_path_different_time():
    """
    Scenario: Same air corridor but time-shifted (should be SAFE)
    """
    primary = Trajectory([
        Waypoint(0, 0, 0),
        Waypoint(10, 10, 10)
    ])

    others = [
        {
            "id": "Delayed_Drone",
            "trajectory": Trajectory([
                Waypoint(0, 0, 5),
                Waypoint(10, 10, 15)
            ])
        }
    ]

    return primary, others


def hovering_surveillance_drone():
    """
    Scenario: Static surveillance drone near flight path
    """
    primary = Trajectory([
        Waypoint(0, 0, 0),
        Waypoint(10, 0, 10)
    ])

    others = [
        {
            "id": "Surveillance_Drone",
            "trajectory": Trajectory([
                Waypoint(5, 1, 0),
                Waypoint(5, 1, 10)
            ])
        }
    ]

    return primary, others
