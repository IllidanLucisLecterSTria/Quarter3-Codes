names = ["Me", "Lia", "Jake"]
steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
daily_totals = []
for day_index in range(len(days)):
    total = 0
    for person in range(len(steps)):
        total += steps[person][day_index]
    daily_totals.append(total)
    print(f"{days[day_index]} total steps: {total}")
max_steps = max(daily_totals)
most_active_day = days[daily_totals.index(max_steps)]
print(f"\nMost active day overall: {most_active_day} ({max_steps} steps)")
