# This program prompts for scores between 0.0 and 1.0, and prints grade in table format

def scrs():
    score = (input("Enter score : "))
    try:
        score = float(score)
        if score >= 1.0:
            print("Bad score") 
        elif score >= 0.9:
            print("A") 
        elif score >= 0.8:
            print("B") 
        elif score >= 0.7:
            print("C") 
        elif score >= 0.6:
            print("D") 
        elif score >= 0.5:
            print("E") 
        elif score < 0.5:
            print("F") 

    except:
        raise Exception("Enter numeric characters only")
if __name__ == "__main__":
    scrs()