from checks.deconfliction import detect_conflict
from visualization.plot2d import plot_trajectories

# Import scenario presets
from scenarios.presets import (
    urban_delivery_crossing,
    emergency_priority_drone,
    same_path_different_time,
    hovering_surveillance_drone
)

# =====================================================
# CONFIGURATION
# =====================================================
SAFETY_RADIUS = 2.0     # minimum safe separation distance
TIME_STEP = 0.5         # time resolution (seconds)

# =====================================================
# SELECT REAL-WORLD SCENARIO (CHOOSE ONE)
# =====================================================
primary, other_drones = urban_delivery_crossing()
# primary, other_drones = emergency_priority_drone()
# primary, other_drones = same_path_different_time()
# primary, other_drones = hovering_surveillance_drone()

# =====================================================
# MULTI-DRONE CONFLICT EVALUATION
# =====================================================
conflicts = []

for drone in other_drones:
    result = detect_conflict(
        primary=primary,
        other=drone["trajectory"],
        safety_radius=SAFETY_RADIUS,
        time_step=TIME_STEP
    )

    if result:
        result["with_drone"] = drone["id"]
        conflicts.append(result)

# =====================================================
# DECISION LOGIC (PRIORITIZE EARLIEST EVENT)
# =====================================================
if conflicts:
    conflicts.sort(key=lambda c: c["time"])
    conflict = conflicts[0]

    print(
        f"{conflict['type']} with {conflict['with_drone']} "
        f"at time {conflict['time']} "
        f"location {conflict['location']} "
        f"(distance={conflict['distance']}, "
        f"severity={conflict['severity']})"
    )
    print(f"Suggested action: {conflict['suggestion']}")

else:
    conflict = None
    print("No conflicts with any drone. Mission is SAFE.")

# =====================================================
# VISUALIZATION
# =====================================================
if conflict:
    conflict_drone = next(
        d["trajectory"] for d in other_drones
        if d["id"] == conflict["with_drone"]
    )
    plot_trajectories(primary, conflict_drone, conflict)
else:
    # Visualize primary vs first drone if no conflict
    plot_trajectories(primary, other_drones[0]["trajectory"], None)
