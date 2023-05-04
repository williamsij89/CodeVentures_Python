mad_libs_template = "Once upon a time, there was a {adjective1} {noun1} who lived in a {noun2}. One day, the {noun1} decided to {verb1} to the {noun3} to find a {adjective2} {noun4}."

def mad_libs():
    words = {
        "adjective1": input("Enter an adjective: "),
        "noun1": input("Enter a noun: "),
        "noun2": input("Enter another noun: "),
        "verb1": input("Enter a verb: "),
        "noun3": input("Enter another noun: "),
        "adjective2": input("Enter another adjective: "),
        "noun4": input("Enter one more noun: "),
    }

    story = mad_libs_template.format(**words)
    print("\nHere's your Mad Libs story:")
    print(story)
