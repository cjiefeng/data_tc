import sys
from datetime import datetime

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import requests
from dateutil import parser
from dateutil.relativedelta import relativedelta


def plot_covid(data):
    x_axis = list(map(lambda x: parser.isoparse(x['Date']), data))
    y_axis = list(map(lambda y: y['Cases'], data))
    plt.plot(x_axis, y_axis)
    plt.title('Covid cases in Singapore')
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.xticks(rotation=45)
    plt.ylabel('Cases')
    plt.show()


API = 'https://api.covid19api.com/country/singapore/status/confirmed'
if __name__ == "__main__":
    start = ""  # 15/09/22
    end = ""  # 01/10/22
    if len(sys.argv) == 3:  # user input
        start = sys.argv[1]
        end = sys.argv[2]

    try:
        start = datetime.strptime(start, '%d/%m/%y')
        end = datetime.strptime(end, '%d/%m/%y')
    except Exception as e:
        print(e)
        # default get 3 months worth of data
        print('use default today - 3 months')
        end = datetime.now().replace(hour=0, minute=0, second=0)
        start = end - relativedelta(months=3)

    params = {
        'from': start,
        'to': end
    }
    resp = requests.get(API, params=params)
    data = resp.json()
    plot_covid(data)
