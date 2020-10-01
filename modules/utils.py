import csv


def fixed_string(string: str, length: int, end: str = ' '):
    """Cuts long strings shorter and adds 'end' to shorter strings
    
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
    """Saves data to csv file

    Args:
        data (list): list of data to write to file
    """
    with open('data/data.csv', 'w', newline='') as f:
        csv_out = csv.writer(f)
        for row in data:
            csv_out.writerow(row.save())


def load_from_csv():
    """Loads data from csv file (data/data.csv)

    Returns:
        list: list of tuples
    """
    with open('data/data.csv', 'r', newline='') as f:
        csv_in = csv.reader(f)
        data = []
        for row in csv_in:
            data.append((row[0], row[1:]))

    return data
