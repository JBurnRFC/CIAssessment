import re
def main():
    data = {}
    WorldValues = []
    file = input("Please enter file name:")
    openfile = open(file, "r")
    openfile = (re.split(r'\n\n', openfile.read()))
    values = []
    ValueDict = []
    CrispValues(openfile, data, WorldValues)
    GetMembership(WorldValues, values, openfile, ValueDict)
    print(ValueDict)


def GetMembership(WorldValues, values, openfile, ValueDict):
    for entry in WorldValues:
        values.append(entry['name'])

    MembershipName = []
    MembershipTuples = []
    for i in range(2, len(openfile) - 1, 2):
        x = openfile[i].strip()
        MembershipName.append(x)
        y = openfile[i+1].split("\n")
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
    #print(ValueDict)
    return ValueDict

def CrispValues(openfile, data, WorldValues):

    RuleList = openfile[1]
    Rules = RuleList.split("\n")

    #Name of rulebase
    ruleBaseName = openfile[0]
    #Get crisp values
    RealWorldValues = openfile[len(openfile) -1]

    RealWorldValues = RealWorldValues.split("\n")

    for x in range(0,len(RealWorldValues)):
        y = RealWorldValues[x].split(" = ")
        if y is not None:
            WorldValues.append(dict({"name": y[0], "value": y[1]}))

    data["CrispValues"] = WorldValues
    return data, WorldValues

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