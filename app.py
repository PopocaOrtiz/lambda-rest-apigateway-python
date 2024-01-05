import io
import base64

from chalice.app import Chalice, Response
import matplotlib.pyplot as plt

from chalicelib.pokeapi import api
from chalicelib.calculate.growth_time import GrowthTimeStats


def fetch_growth_time_stats_from_api():
    """
    Retrieves berries' data, fetches their details, and calculates statistics based on the data.
    """

    berries_names = api.get_berries_list()
    berries_details = api.get_berries_detail(berries_names)

    growth_time = GrowthTimeStats([berry['growth_time'] for berry in berries_details])

    return {
        "berries_names": berries_names,
        "min_growth_time": growth_time.get_min(),
        "median_growth_time": growth_time.get_median(),
        "max_growth_time": growth_time.get_max(),
        "variance_growth_time": growth_time.get_variance(),
        "mean_growth_time": growth_time.get_mean(),
        "frequency_growth_time": growth_time.get_frequency()
    }


app = Chalice(app_name='poke-berries-statistics-api')


@app.route('/allBerryStats')
def all_berry_stats():
    return fetch_growth_time_stats_from_api()


@app.route('/allBerryStats/histogram')
def all_berry_stats_histogram():
    res = fetch_growth_time_stats_from_api()
    frequency_growth_time = res['frequency_growth_time']

    values = list(frequency_growth_time.keys())
    repetitions = list(frequency_growth_time.values())

    plt.bar(values, repetitions)
    plt.xlabel('Growth Time')
    plt.ylabel('Number of Repetitions')
    plt.title('Growth Time Histogram')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Convert the plot to a base64 string
    plot_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return Response(
        body="""<html><body><img src="data:image/png;base64,{}" /></body></html>""".format(plot_base64),
        headers={'Content-Type': 'text/html'},
        status_code=200
    )