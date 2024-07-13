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

    pattern = r"\(+7|8)?\s((\d(3)))\s(\d(3))[\s](\d(2))[\s](\d(2))"
    phone_format = r"+7(\2)\3-\4-\5"

    for contact in contacts_list[1:]:
        fio = fio_edit(contact)
        contact[0] = fio['lastname']
        contact[1] = fio['firstname']
        contact[2] = fio['surname']

