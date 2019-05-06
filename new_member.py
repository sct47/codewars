def openOrSenior(data):
    """Senior members must be 55 years or older, handicap greater than 7."""
    category = []
    for member in data:
        age = member[0]
        handicap = member[1]
        if age >= 55 and handicap > 7:
            category.append("Senior")
        else:
            category.append("Open")
    return category

def openOrSenior(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]            



newMember([[18, 20],[45, 2], [61, 12], [37, 6], [21, 21],[78, 9]])