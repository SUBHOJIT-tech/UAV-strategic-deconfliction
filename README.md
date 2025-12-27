🚁 UAV Strategic Deconfliction System
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![UAV](https://img.shields.io/badge/Domain-UAV%20Safety-orange)

🛩️ Multi-Drone Airspace Safety • Conflict Detection • Visualization
🚀 Quick Start (Run in 60 seconds)
git clone https://github.com/SUBHOJIT-tech/UAV-strategic-deconfliction.git
cd UAV-strategic-deconfliction

python -m venv venv
venv\Scripts\activate    # Windows
pip install -r requirements.txt

python main.py

FOR macOS/Linux
source venv/bin/activate
Outputs:-
Visualization:
- 2D plot with drone paths
- Highlighted conflict / near-miss point
📌 Overview

This project implements a Strategic UAV Deconfliction System that determines whether a planned drone mission can safely operate in shared airspace with multiple other drones.

The system detects:

🚨 Hard conflicts (safety violation)

⚠️ Near-miss events (unsafe proximity)

📊 Severity levels

🧭 Mitigation suggestions

It is inspired by real-world UTM (Unmanned Traffic Management) and airspace safety systems used for autonomous drones.

✨ Key Features

🧠 Continuous-Time Conflict Detection
Drones are tracked continuously using linear interpolation between waypoints.

🛸 Multi-Drone Airspace (N Drones)
Evaluates one primary mission against any number of other drones.

🚨 Conflict & Near-Miss Classification

CONFLICT → Safety radius violated

NEAR_MISS → Unsafe proximity without violation

🔥 Severity Grading

CRITICAL

HIGH

MEDIUM

LOW

🛠️ Mitigation Suggestions
Example:

Delay mission

Increase separation

Monitor closely

🗺️ Real-World Scenario Presets

Urban delivery crossing

Emergency priority drone

Time-shifted corridor reuse

Hovering surveillance drone

📈 2D Visualization(Initial)

Drone trajectories

Conflict / near-miss location

Time annotation

## 🧭 4D Deconfliction Extension

To extend the system beyond planar motion, the simulation has been upgraded to support **4D deconfliction**, where:

- **X, Y** → horizontal position  
- **Z** → altitude  
- **T** → time (continuous)

This enables realistic modeling of **vertical separation**, which is critical in real-world UAV and UTM (Unmanned Traffic Management) systems.

---

### 🔹 What Changed

- **Waypoints extended to (x, y, z, t)**  
  Each waypoint now includes altitude, allowing drones to cross the same x–y location at different heights.

- **Continuous-Time 3D Separation**
  Drone positions are interpolated in 3D space, and **Euclidean distance in (x, y, z)** is evaluated at each time step.

- **4D Conflict Logic**
  The same deconfliction engine operates in 4D by combining:
  - 3D spatial separation  
  - continuous time evaluation  

- **3D Visualization**
  A dedicated 3D plot visualizes:
  - drone trajectories in space  
  - altitude differences  
  - conflict / near-miss points  

---

### 🔹 Why This Matters

In dense airspace, many conflicts are avoided not by horizontal separation but by **altitude stratification**.  
This extension demonstrates how the system aligns with **real aviation safety practices**, where vertical separation is a primary deconfliction mechanism.

---

### 🔹 2D vs 4D Modes

The system supports both modes using a simple toggle:

- **2D Mode** → traditional planar analysis  
- **4D Mode** → full (x, y, z, t) safety evaluation  

This design keeps the core logic reusable while enabling advanced analysis.
 The inclusion of altitude transforms the simulation into a true **4D deconfliction system**, qualifying it for extended visualization and safety analysis.


## 📁 Project Structure

UAV-strategic-deconfliction/
│
├── main.py # Entry point: orchestration
├── README.md # Project documentation
├── requirements.txt # Dependencies
├── .gitignore # Ignored files
│
├── models/
│ ├── waypoint.py # Waypoint abstraction (x, y, z, t)
│ └── trajectory.py # Continuous motion model
│
├── checks/
│ ├── spatial.py # Distance calculations
│ ├── temporal.py # Time utilities
│ └── deconfliction.py # Core safety engine
│
├── scenarios/
│ └── presets.py # Real-world UAV scenarios
│
├── visualization/
│ ├── plot2d.py # 2D visualization
│ └── plot3d.py # 3D (altitude-aware) visualization
│
└── assets/

⚙️ How the System Works
1️⃣ Trajectory Modeling

Each drone mission is defined using time-stamped waypoints (x, y, t).

2️⃣ Continuous Motion

Drone positions are interpolated between waypoints to compute location at any time.

3️⃣ Spatio-Temporal Evaluation

At each time step:

Distance between drones is computed

Safety thresholds are applied

4️⃣ Event Classification
Condition	Result
Distance < Safety Radius	🚨 Conflict
Safety < Distance < 1.2×Safety	⚠️ Near Miss
5️⃣ Severity Assessment

Severity is based on proximity to the safety radius.

6️⃣ Prioritization

If multiple events exist, the earliest safety-critical event is reported.
Urban Delivery Simulation:(4D also included  according to our requirement we can toggle).
<img width="1365" height="785" alt="image" src="https://github.com/user-attachments/assets/77549216-d444-4915-9e7b-743a897521ee" />

Emergency Drone simulation:
<img width="1265" height="828" alt="Screenshot 2025-12-27 134451" src="https://github.com/user-attachments/assets/d3cd185c-6486-43a4-8b77-fe476d0bec15" />
Hovering Survillience:
<img width="1198" height="766" alt="Screenshot 2025-12-27 134638" src="https://github.com/user-attachments/assets/ee4b58bc-e706-49b5-a5b9-320cba4cdec8" />

🔧 Configuration Parameters

Defined in main.py:

SAFETY_RADIUS = 2.0   # Minimum safe separation distance
TIME_STEP = 0.5       # Time resolution (seconds)

🌍 Real-World Scenarios Implemented
Scenario	Description
🏙️ Urban Delivery	Crossing delivery drones in city airspace
🚑 Emergency Drone	Priority UAV cutting across traffic
⏱️ Time-Shifted Corridor	Same path, different time slots
👁️ Surveillance Drone	Hovering drone near flight path
🧠 Design Philosophy

🧩 Separation of Concerns

main.py → orchestration

deconfliction.py → safety logic

scenarios/ → real-world modeling

📈 Scalability-Ready
Architecture naturally extends to large airspace systems.

🛡️ Safety-First Thinking
Near-miss handling reflects aviation best practices.

🚀 Scalability Discussion (High Level)

To support thousands of drones, this system can be extended using:

Spatial partitioning (grids / R-trees)

Time bucketing

Parallel conflict evaluation

Distributed processing (UTM-style architecture)

🧑‍💻 Author Notes

This project demonstrates:

System-level thinking

Real-world UAV safety modeling

Clean and modular Python architecture

Strong documentation and presentation

## 📌 Key Takeaway

This project demonstrates how **real-world UAV airspace safety** can be modeled using:
- Continuous-time motion
- Multi-drone conflict detection
- Severity grading
- Mitigation planning
- Visual validation


## ⭐ Support

If you find this project interesting or useful:
- ⭐ Star the repository
- 🍴 Fork it for experimentation
