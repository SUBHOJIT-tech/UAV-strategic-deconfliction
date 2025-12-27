class Trajectory:
    def __init__(self, waypoints):
        self.waypoints = waypoints

    def position_at(self, t):
        for i in range(len(self.waypoints) - 1):
            w1 = self.waypoints[i]
            w2 = self.waypoints[i + 1]

            if w1.t <= t <= w2.t:
                ratio = (t - w1.t) / (w2.t - w1.t)
                x = w1.x + ratio * (w2.x - w1.x)
                y = w1.y + ratio * (w2.y - w1.y)
                return x, y

        return None
