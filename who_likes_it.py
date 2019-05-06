import string

def likes(names):
    """Determine the correct grammar for likes."""
    if len(names) == 0:
        return("no one likes this")
    elif len(names) == 1:
        print(string.capwords(names[0]) + " likes this")
    elif len(names) == 2:
        return(names[0].title() + " and " + names[1].title() + " like this.")
    elif len(names) == 3:
        return(names[0].title() + ", " + names[1].title() + " and " + 
            names[2].title() + " like this.")
    elif len(names) >= 4:
        return(names[0].title() + ", " + names[1].title() + " and " + 
            str((len(names) - 2)) + " others like this.") 

likes(['Jess McMan'])