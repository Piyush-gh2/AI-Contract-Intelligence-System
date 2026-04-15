def detect_risk(line):
    line = line.lower()
    
    if "unlimited liability" in line:
        return "High Risk"
    elif "no liability" in line:
        return "High Risk"
    elif "termination clause is not included" in line:
        return "High Risk"
    elif "late payment" in line:
        return "Medium Risk"
    else:
        return "Low Risk"