from csv import DictReader, DictWriter


def process_file(path):
    with open(path, 'r') as data:
        csv_reader = DictReader(data)
        for row in csv_reader:
            name = row['name']
            price = row['price']
            above_100 = False
            clean_name = name.strip()
            if clean_name == "":  # skip empty name
                continue
            name_split = clean_name.split()  # split first/last name
            first_name = name_split[0]
            last_name = name_split[1]
            if price.startswith('0'):
                price = price.lstrip('0')  # remove prepended '0'
                f_price = float(price)
                if f_price > 100:
                    above_100 = True
            yield {
                'first_name': first_name,
                'last_name': last_name,
                'price': price,
                'above_100': above_100
            }
    data.close()


if __name__ == "__main__":
    # assume data is already in data directory every day before processing
    # example: download csv file from source, i.e. from s3 to data/ directory
    with open('output.csv', 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name', 'price', 'above_100']
        csv_writer = DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()
        files = ['data/dataset1.csv', 'data/dataset2.csv']
        for file in files:
            for item in process_file(file):
                csv_writer.writerow(item)
        csvfile.close()
    # extra: send file i.e. s3, so we can terminate pod
