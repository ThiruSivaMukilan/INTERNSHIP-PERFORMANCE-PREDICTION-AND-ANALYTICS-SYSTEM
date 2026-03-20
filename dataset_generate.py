import pandas as pd
import numpy as np
import os
np.random.seed(42)
rows = 5000
data = []
os.makedirs("data", exist_ok=True)
for i in range(rows):
    intern_id = f"RX{str(i+1).zfill(4)}"
    perf_type = np.random.choice(['high', 'medium', 'low'])
    if perf_type == 'high':
        sprints_total = np.random.randint(4, 8)
        sprints_done = np.random.randint(sprints_total-1, sprints_total+1)

        tasks_assigned = np.random.randint(8, 15)
        tasks_completed = np.random.randint(tasks_assigned-2, tasks_assigned+1)

        meetings_total = np.random.randint(15, 25)
        meetings_attended = np.random.randint(meetings_total-3, meetings_total+1)

        code_review_score = np.random.uniform(80, 100)
        deadline_met = np.random.uniform(75, 100)
        attendance = np.random.uniform(85, 100)
        punctuality = 1
    elif perf_type == 'medium':
        sprints_total = np.random.randint(4, 8)
        sprints_done = np.random.randint(int(sprints_total*0.6), sprints_total)

        tasks_assigned = np.random.randint(8, 15)
        tasks_completed = np.random.randint(int(tasks_assigned*0.6), tasks_assigned)

        meetings_total = np.random.randint(15, 25)
        meetings_attended = np.random.randint(int(meetings_total*0.6), meetings_total)

        code_review_score = np.random.uniform(50, 80)
        deadline_met = np.random.uniform(50, 75)
        attendance = np.random.uniform(60, 85)
        punctuality = np.random.choice([0,1])
    else:
        sprints_total = np.random.randint(4, 8)
        sprints_done = np.random.randint(1, int(sprints_total*0.5))

        tasks_assigned = np.random.randint(8, 15)
        tasks_completed = np.random.randint(1, int(tasks_assigned*0.5))

        meetings_total = np.random.randint(15, 25)
        meetings_attended = np.random.randint(1, int(meetings_total*0.5))

        code_review_score = np.random.uniform(20, 50)
        deadline_met = np.random.uniform(20, 50)
        attendance = np.random.uniform(40, 60)
        punctuality = 0
    data.append([
        intern_id,
        sprints_done,
        sprints_total,
        tasks_completed,
        tasks_assigned,
        meetings_attended,
        meetings_total,
        round(code_review_score, 2),
        round(deadline_met, 2),
        round(attendance, 2),
        punctuality
    ])
columns = [
    "intern_id",
    "sprints_done",
    "sprints_total",
    "tasks_completed",
    "tasks_assigned",
    "meetings_attended",
    "meetings_total",
    "code_review_score",
    "deadline_met_percentage",
    "attendance_percentage",
    "punctuality"
]
df = pd.DataFrame(data, columns=columns)
df.to_csv("data/real_world_intern_data.csv", index=False)
print("Real-world dataset created successfully!")
print(df.head())