import re


def main():
    data = {}
    WorldValues = []
    Rules = []
    tophalf = []
    Weights = []
    values = []
    ValueDict = []



    file = input("Please enter file name:")
    openfile = open(file, "r")
    openfile = (re.split(r'\n\n', openfile.read()))
    CrispValues(Rules, openfile, data, WorldValues)
    GetMembership(WorldValues, values, openfile, ValueDict)
    GetFormula(openfile, ValueDict, tophalf, Weights)
    ComputeFormula(Weights, tophalf)



def ComputeFormula(Weights, tophalf):
    Overallweight = sum(Weights)
    overalltop = sum(tophalf)
    answer = overalltop / Overallweight
    print(answer)
    return answer


def GetFormula(openfile, ValueDict, tophalf, Weights):
    RuleList = openfile[1]
    Rules = RuleList.split("\n")
    for i in range(0, len(Rules)):
        SplitRules = Rules[i].split(" ")
        conditions = {SplitRules[4]: SplitRules[6], SplitRules[9]: SplitRules[11]}
        output = {SplitRules[14]: SplitRules[17]}
        RulesDict = {"Rule": SplitRules[1], "Conditions": conditions, "Operator": SplitRules[7],
                     "output_name": SplitRules[14], "Output": SplitRules[17]}
        PotentialWs = []
        w1 = 0
        for Entry in ValueDict:
            if SplitRules[7] == 'and':
                if Entry['name'] == SplitRules[4]:
                    #Check if equals 0
                    if Entry['Fuzzy Values'][SplitRules[6]] > 0:
                        PotentialWs.append(Entry['Fuzzy Values'][SplitRules[6]])
                    else:
                        pass
                elif Entry['name'] == SplitRules[9]:
                    #Check if equals 0
                    if Entry['Fuzzy Values'][SplitRules[11]] > 0:
                        PotentialWs.append(Entry['Fuzzy Values'][SplitRules[11]])
                    else:
                        pass
                if len(PotentialWs) > 1:
                    w1 = min(PotentialWs)
                else:
                    pass
            elif SplitRules[7] == 'or':
                if Entry['name'] == SplitRules[4]:
                    #Check if equals 0
                    if Entry['Fuzzy Values'][SplitRules[6]] > 0:
                        PotentialWs.append(Entry['Fuzzy Values'][SplitRules[6]])
                    else:
                        pass
                elif Entry['name'] == SplitRules[9]:
                    #Check if equals 0
                    if Entry['Fuzzy Values'][SplitRules[11]] > 0:
                        PotentialWs.append(Entry['Fuzzy Values'][SplitRules[11]])
                    else:
                        pass
                if len(PotentialWs) > 0:
                    w1 = max(PotentialWs)
        variable = 0
        counter = 0
        MembershipName = []
        MembershipTuples = []
        for i in range(2, len(openfile) - 1, 2):
            x = openfile[i].strip()
            MembershipName.append(x)
            y = openfile[i + 1].split("\n")
            MembershipTuples.append(y)
        Membership = dict(zip(MembershipName, MembershipTuples))
        while counter < w1:
            counter = 0
            for val in (Membership[SplitRules[14]]):
                if SplitRules[17] in val:
                    goon = val.split(" ")
                    a = goon[1]
                    b = goon[2]
                    Alpha = goon[3]
                    Beta = goon[4]
                    e1 = curve(a, b, Alpha, Beta, 'name')
                    counter = e1.membershipOf(variable)
                    # print(counter)
                    variable += 0.01
        wz = variable * w1
        if wz != 0:
            tophalf.append(wz)
            #print(wz)
        if w1 != 0:
            Weights.append(w1)
    return tophalf, Weights


def GetMembership(WorldValues, values, openfile, ValueDict):
    for entry in WorldValues:
        values.append(entry['name'])

    MembershipName = []
    MembershipTuples = []
    for i in range(2, len(openfile) - 1, 2):
        x = openfile[i].strip()
        MembershipName.append(x)
        y = openfile[i + 1].split("\n")
        MembershipTuples.append(y)

    Membership = dict(zip(MembershipName, MembershipTuples))
    for j in range(0, len(WorldValues)):
        x = WorldValues[j]
        var = x['name']
        Value = x['value']
        Membervals = {}
        for i in range(0, len(Membership)):
            tuple = (Membership[var])
            z = tuple[i].split(" ")
            a = int(z[1])
            b = int(z[2])
            Alpha = int(z[3])
            Beta = int(z[4])
            e1 = curve(a, b, Alpha, Beta, 'name')
            Membervals[z[0]] = e1.membershipOf(Value)
        ValueDict.append(dict({"name": var, "Fuzzy Values": Membervals}))
    return ValueDict


def CrispValues(Rules, openfile, data, WorldValues):
    RuleList = openfile[1]
    Rules = RuleList.split("\n")

    # Name of rulebase
    ruleBaseName = openfile[0]
    # Get crisp values
    RealWorldValues = openfile[len(openfile) - 1]

    RealWorldValues = RealWorldValues.split("\n")

    for x in range(0, len(RealWorldValues)):
        y = RealWorldValues[x].split(" = ")
        if y is not None:
            WorldValues.append(dict({"name": y[0], "value": y[1]}))

    data["CrispValues"] = WorldValues
    return Rules, data, WorldValues


class curve:
    name = ""

    def __init__(self, a, b, alpha, beta, name):
        self.a = int(a)
        self.b = int(b)
        self.alpha = int(alpha)
        self.beta = int(beta)
        self.name = name

    def CurveName(self):
        return self.name

    def membershipOf( self, value ):

        value = int(value)

        if(value < (self.a - self.alpha)):
            return 0
        elif(value in range (self.a - self.alpha, self.a)):
            return (value - self.a + self.alpha) / self.alpha
        elif(value in range(self.a,self.b)):
            return 1
        elif(value in range(self.b, self.b+self.beta)):
            return (self.b + self.beta - value) / self.beta
        elif(value > (self.b + self.beta)):
            return 0

        return


if __name__ == '__main__':
    main()