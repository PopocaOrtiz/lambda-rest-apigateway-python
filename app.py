import base64

from chalice.app import Chalice, Response
import pygal

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

    frequency_growth_time = {}
    for i in range(res['min_growth_time'], res['max_growth_time'] + 1):
        if i in res['frequency_growth_time']:
            frequency_growth_time[i] = res['frequency_growth_time'][i]
        else:
            frequency_growth_time[i] = 0

    values = list(frequency_growth_time.keys())
    repetitions = list(frequency_growth_time.values())

    # Create a Pygal Bar chart
    chart = pygal.Bar()
    chart.x_labels = values
    chart.add('Repetitions', repetitions)

    # Render the chart to a file
    chart.render_to_file('/tmp/histogram.svg')

    # Read the rendered chart file
    with open('/tmp/histogram.svg', 'rb') as f:
        plot_base64 = base64.b64encode(f.read()).decode('utf-8')

    return Response(
        body="""<html><body><img style="width:800px" src="data:image/svg+xml;base64,{}" /></body></html>""".format(plot_base64),
        headers={'Content-Type': 'text/html'},
        status_code=200
    )