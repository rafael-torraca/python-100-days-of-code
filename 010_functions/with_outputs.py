def format_name(f_name, l_name):
    """Take a first and last name and format it
    to return the title case version of the name.

    Args:
        f_name ([string])
        l_name ([string])

    Returns:
        f_name + l_name in title
    """
    if f_name == "" or l_name == "":
        return "You not enter a valid name!"
    full_name = f"{f_name} {l_name}"
    return full_name.title()


print(format_name("rafaeL", "LeanDrO"))
