course_id = input("хичээлийн код: ")
course_name = input("хичээлийн нэр: ")
credit = input("хичээлийн кредит: ")

madlib = "энэ хичээлийн код нь {}".format(course_id).upper() + \
    ", хичээлийн нэр нь {}".format(course_name).title() + \
    "бөгөөд уг хичээл нь {}".format(credit) + "  кредитийн хичээл юм."

madlib1 = " энэ хичээлийн код нь {}".format(course_id).upper() + \
    ", хичээлийн нэр нь {}".format(course_name).title() + \
    "бөгөөд уг хичээл нь {}".format(credit) + "  кредитийн хичээл юм."
print(madlib)
print(madlib1)