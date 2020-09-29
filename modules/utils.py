import csv


def str_sized(string: str, lenth: int, end: str = ' ') -> str:
    """Cuts off a long string to conform with `lenth`, replace the end of the string with `end` if provided.
    Args:
        string (str): the string to format
        lenth (int): the max lenth of the string
        end (str): replace the end of the cut string with `end`
    Returns:
        str: the formatted string
    """
    lenth -= len(end)
    if lenth <= 0 or len(string) <= lenth:
        return string
    else:
        return string[:lenth] + end


def save_to_csv(data):
    with open('data/data.csv', 'w', newline='') as f:
        csv_out = csv.writer(f)
        for row in data:
            csv_out.writerow(row.save())


def load_from_csv():
    with open('data/data.csv', 'r', newline='') as f:
        csv_in = csv.reader(f)
        data = []
        for row in csv_in:
            data.append((row[0], row[1:]))

    return data
