import matplotlib.pyplot as plt

def plot_trajectories(primary, other, conflict=None):
    px = [wp.x for wp in primary.waypoints]
    py = [wp.y for wp in primary.waypoints]
    plt.plot(px, py, 'r-', label='Primary Drone')

    ox = [wp.x for wp in other.waypoints]
    oy = [wp.y for wp in other.waypoints]
    plt.plot(ox, oy, 'b--', label='Other Drone')

    if conflict:
        cx, cy = conflict["location"]
        plt.scatter(cx, cy, c='red', s=100)
        plt.text(cx, cy, f"{conflict['type']} @ t={conflict['time']}")

    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.title("UAV Strategic Deconfliction Simulation")
    plt.legend()
    plt.grid(True)
    plt.show()
