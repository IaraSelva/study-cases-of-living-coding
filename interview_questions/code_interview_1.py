input = [
    {
        "start": 10,
        "end": 100,
        "name": "Amanda"
    },
    {
        "start": 120,
        "end": 300,
        "name": "Afonso"
    },
    {
        "start": 10,
        "end": 50,
        "name": "Alex"
    },
    {
        "start": 20,
        "end": 70,
        "name": "Andre"
    },
    {
        "start": 20,
        "end": 120,
        "name": "Rafael"
    },
    {
        "start": 60,
        "end": 100,
        "name": "Sergio"
    }
]

def getHours(input):
    hours = []
    for schedule in input:
        hours.append(schedule["start"])
        hours.append(schedule["end"])

        hours = sorted(list(set(hours)))
        return hours

def createOutput(hours):
    left = 0
    right = 1
    output = []
    
    while right < len(hours):
        output.append({
            "start": hours[left],
            "end": hours[right],
            "names": []
        })
        left += 1
        right += 1
    return output

def getNames(input, output):
    for interval in output:
        for schedule in input:
            if schedule["start"] <= interval["start"] and schedule["end"] >= interval["end"]:
                interval["names"].append(schedule["name"])
    return output

getNames(input, createOutput(getHours(input)))