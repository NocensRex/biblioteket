import csv


def fixed_string(string: str, length: int, end: str = ' ') -> str:
    """Cuts off a long string to conform with `length`, replace the end of the string with `end` if provided.
    Args:
        string (str): the string to format
        length (int): the max length of the string
        end (str): replace the end of the cut string with `end`
    Returns:
        str: the formatted string
    """
    length -= len(end)
    if length <= 0 or len(string) <= length:
        return string
    else:
        return string[:length] + end


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
