import tkinter as tk


class StudentBidInfo:
    """
    This class displays all the details of a student's bid
    """
    def display_bid_details(self, bid_item, root):
        additional_info = bid_item['additionalInfo']['bidInfo']

        tk.Label(root, text="Required lesson: " + additional_info['requiredLesson'], height="4", width="50").grid(row=1, column=7)
        tk.Label(root, text="Preferred time and day: " + additional_info['timeDay'], height="4", width="50").grid(row=3, column=7)
        tk.Label(root, text="Number of sessions per week: " + additional_info['sessionsPerWeek'], height="4", width="50").grid(row=5, column=7)
        tk.Label(root, text="Rate(per hour or per session): " + additional_info['lessonRate'], height="4", width="50").grid(row=7, column=7)
