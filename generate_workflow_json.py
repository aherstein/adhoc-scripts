import json
import random

statuses = [
    "Status 1",
    "Status 2",
    "Status 3",
    "Status 4"
]

priorities = [
    "Priority Low",
    "Priority Medium",
    "Priority High",
    "Priority Critical"
]
types = [
    "Fraud"
    "Collections / Servicing"
    "Credit Reporting"
    "Dealers"
    "Third Party / Other"
    "Billing"
    "Insurance"
    "Other"
]

thresholds = {}

for type in types:
    thresholds[type] = {}
    for priority in priorities:
        thresholds[type][priority] = {}
        for status in statuses:
            thresholds[type][priority][status] = random.randint(0, 9)

print(json.dumps(thresholds))
