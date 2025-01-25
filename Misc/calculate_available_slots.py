from datetime import datetime, timedelta
from typing import List, Dict, Tuple


def parse_time(time_str: str) -> datetime:
    return datetime.strptime(time_str, "%H:%M")


def get_appointment_end(start_time: datetime, duration: int) -> datetime:
    return start_time + timedelta(minutes=duration)


def find_max_30_min_slots(days: List[List[Dict[str, str]]]) -> List[int]:
    start_of_day = parse_time("09:00")
    end_of_day = parse_time("17:00")

    max_slots_per_day: List[int] = []

    for appointments in days:
        # Parse appointments into intervals
        booked_intervals: List[Tuple[datetime, datetime]] = []
        for appt in appointments:
            start = parse_time(appt["start"])
            end = get_appointment_end(start, int(appt["duration"]))
            booked_intervals.append((start, end))

        # Sort intervals by start time
        booked_intervals.sort()

        # Find gaps between appointments
        available_slots: List[Tuple[datetime, datetime]] = []
        current_time = start_of_day

        for start, end in booked_intervals:
            if current_time < start:  # There is a gap
                available_slots.append((current_time, start))
            current_time = max(current_time, end)

        # Check for gap after the last appointment
        if current_time < end_of_day:
            available_slots.append((current_time, end_of_day))

        # Calculate the number of 30-minute slots
        slots = 0
        for start, end in available_slots:
            gap_duration = (end - start).total_seconds() / 60
            if gap_duration >= 30:
                slots += int(gap_duration // 30)

        max_slots_per_day.append(slots)

    return max_slots_per_day


def find_max_available_slots(json_data):
    working_hours_start = datetime.strptime("09:00", "%H:%M")
    working_hours_end = datetime.strptime("17:00", "%H:%M")

    # Parse JSON and convert time slots to datetime ranges
    occupied_slots = []
    for entry in json_data:
        start = datetime.strptime(entry["start"], "%H:%M")
        end = get_appointment_end(start, int(entry["duration"]))
        occupied_slots.append((start, end))

    # Generate all 30-minute intervals
    available_slots = []
    current_time = working_hours_start
    while current_time + timedelta(minutes=30) <= working_hours_end:
        available_slots.append((current_time, current_time + timedelta(minutes=30)))
        current_time += timedelta(minutes=30)

    # Filter out occupied intervals
    max_available_slots = []
    for interval in available_slots:
        if all(
            interval[1] <= slot[0] or interval[0] >= slot[1] for slot in occupied_slots
        ):
            max_available_slots.append(interval)

    return len(max_available_slots)


# Sample Data
days = [
    [
        {"start": "09:15", "duration": "30"},
        {"start": "10:00", "duration": "60"},
        {"start": "11:15", "duration": "30"},
        {"start": "12:45", "duration": "30"},
        {"start": "13:15", "duration": "90"},
        {"start": "15:00", "duration": "30"},
        {"start": "15:30", "duration": "30"},
    ],
    [
        {"start": "11:15", "duration": "30"},
        {"start": "12:45", "duration": "30"},
        {"start": "13:15", "duration": "90"},
        {"start": "15:00", "duration": "30"},
    ],
]

# Find maximum number of 30-minute slots per day
result = find_max_30_min_slots(days)
print(result)

# Find maximum number of 30-minute slots per day
result = [find_max_available_slots(day) for day in days]
print(result)
