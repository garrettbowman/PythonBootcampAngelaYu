def format_name(fname, lname):
    formated_f_name = fname.title()
    formated_l_name = lname.title()
    return f"{formated_f_name} {formated_l_name}"

formated_name = format_name("AnGeLa", "YU")

length = len(formated_name)

print(length)