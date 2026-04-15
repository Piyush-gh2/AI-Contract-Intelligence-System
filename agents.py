from src.parser import load_contract
from src.risk import detect_risk

def analyze_contract():
    lines = load_contract()
    
    results = []
    
    for line in lines:
        risk = detect_risk(line)
        results.append((line.strip(), risk))
    
    return results