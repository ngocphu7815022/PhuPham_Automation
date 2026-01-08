import json
import yaml
import openpyxl
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")


def load_json(file_name):
    with open(os.path.join(DATA_DIR, file_name), encoding="utf-8") as f:
        return json.load(f)


def load_yaml(file_name):
    with open(os.path.join(DATA_DIR, file_name), encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_excel(file_name, sheet_name):
    workbook = openpyxl.load_workbook(os.path.join(DATA_DIR, file_name))
    sheet = workbook[sheet_name]

    headers = [cell.value for cell in sheet[1]]
    data = []

    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append(dict(zip(headers, row)))

    return data
