import re


def main():
    data = {}
    file = input("Please enter file name:")
    openfile = open(file, "r")
    openfile = (re.split(r'\n\n', openfile.read()))
    CrispValues(openfile, data)
    print(data)


def CrispValues(openfile, data):
    RuleList = openfile[1]
    Rules = RuleList.split("\n")

    # Name of rulebase
    ruleBaseName = openfile[0]
    # Get crisp values
    RealWorldValues = openfile[len(openfile) - 1]

    RealWorldValues = RealWorldValues.split("\n")
    WorldValues = []

    for x in range(0, len(RealWorldValues)):
        y = RealWorldValues[x].split(" = ")
        if y is not None:
            WorldValues.append(dict({"name": y[0], "value": y[1]}))

    data["RuleBaseName"] = ruleBaseName
    data["CrispValues"] = WorldValues
    return data


if __name__ == '__main__':
    main()