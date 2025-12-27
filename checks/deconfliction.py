from checks.spatial import distance

def classify_severity(d, safety_radius):
    if d < safety_radius * 0.5:
        return "CRITICAL"
    elif d < safety_radius:
        return "HIGH"
    elif d < safety_radius * 1.5:
        return "MEDIUM"
    else:
        return "LOW"


def detect_conflict(primary, other, safety_radius, time_step):
    start_time = max(primary.waypoints[0].t, other.waypoints[0].t)
    end_time = min(primary.waypoints[-1].t, other.waypoints[-1].t)

    t = start_time
    while t <= end_time:
        p_pos = primary.position_at(t)
        o_pos = other.position_at(t)

        if p_pos and o_pos:
            d = distance(p_pos[0], p_pos[1], o_pos[0], o_pos[1])
            severity = classify_severity(d, safety_radius)

            # HARD CONFLICT
            if d < safety_radius:
                return {
                    "type": "CONFLICT",
                    "time": round(t, 2),
                    "location": (round(p_pos[0], 2), round(p_pos[1], 2)),
                    "distance": round(d, 2),
                    "severity": severity,
                    "suggestion": f"Delay primary mission by {round(time_step * 4, 2)} seconds"
                }

            # NEAR MISS
            elif d < safety_radius * 1.2:
                return {
                    "type": "NEAR_MISS",
                    "time": round(t, 2),
                    "location": (round(p_pos[0], 2), round(p_pos[1], 2)),
                    "distance": round(d, 2),
                    "severity": severity,
                    "suggestion": "Increase separation or monitor closely"
                }

        t += time_step

    return None
