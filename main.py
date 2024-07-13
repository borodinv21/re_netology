from pprint import pprint

import re
import csv

def get_data_from_csv(csv_filename):
    with open(csv_filename, encoding="utf-8") as f:
      rows = csv.reader(f, delimiter=",")
      contacts_list = list(rows)

    return contacts_list

def fio_edit(contact):
    fio = f"{contact[0]} {contact[1]} {contact[2]}".strip().split()
    fio_dict = {
        'lastname': fio[0],
        'firstname': fio[1],
        'surname': fio[2] if len(fio) == 3 else ""
    }

    return fio_dict

if __name__ == "__main__":
    contacts_list = get_data_from_csv("phonebook_raw.csv")

    phone_pattern = r"\+?[7|8]\s*(\(*\d{3}\)*)\s*\-*(\d{3})\s*\-*(\d{2})\s*\-*(\d{2})"
    secondary_phone_pattern = r"\s+(\d{4})"

    phone_format_with_bracket = r"+7(\1)\2-\3-\4"
    phone_format_no_bracket = r"+7\1\2-\3-\4"
    secondary_phone_format = r"доб.\1"

    for contact in contacts_list[1:]:
        fio = fio_edit(contact)
        contact[0] = fio['lastname']
        contact[1] = fio['firstname']
        contact[2] = fio['surname']

        phone_result = re.search(phone_pattern, contact[5])
        if phone_result is not None:
            if "(" in phone_result.group():
                contact[5] = re.sub(phone_pattern, phone_format_no_bracket, contact[5])
            else:
                contact[5] = re.sub(phone_pattern, phone_format_with_bracket, contact[5])
            secondary_phone = re.sub(secondary_phone_pattern, secondary_phone_format, contact[5])
            print(secondary_phone)