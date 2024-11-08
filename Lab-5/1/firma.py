class Candidate:
    def __init__(self, properties):
        self.properties = properties


class Firm:
    def __init__(self, properties):
        self.properties = properties


def calculate_preference(candidate, firm):
    SCALE = {
        "Positive": 1,
        "Negative": 0
    }

    preference = 0
    for key in candidate.properties:
        c_prop = candidate.properties[key]
        f_prop = firm.properties[key]
        if (c_prop == "Negative") and (f_prop) == "Negative":
            preference += not(SCALE[c_prop] and SCALE[f_prop])
        else:
            preference += SCALE[c_prop] and SCALE[f_prop]
    return preference

def main():
    Candidate1 = Candidate({"Property1": "Positive", "Property2": "Positive"})

    firms = [
        Firm({"Property1": "Negative", "Property2": "Negative"}),
        Firm({"Property1": "Negative", "Property2": "Positive"}),
        Firm({"Property1": "Positive", "Property2": "Positive"})
    ]

    count = 0
    canditate_choice = {}
    for firm in firms:
        count += 1
        canditate_choice[f'Firm {count}'] = calculate_preference(Candidate1, firm)
    print(canditate_choice)

    sorted_tuples = sorted(canditate_choice.items(), key=lambda item: item[1])
    sorted_dict = {k: v for k, v in sorted_tuples}
    s = ''
    for key, value in sorted_dict.items():
        s += ("{0}: {1} рейтниг ".format(key, value))
    print(s)

if __name__ == "__main__":
    main()

