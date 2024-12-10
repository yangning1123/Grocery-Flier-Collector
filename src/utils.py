import datetime
import requests
from pathlib import Path

RESOURCES_PATH = Path(__file__).parent.parent / "resources"
current_calendar = datetime.datetime.now().isocalendar()
year_no, week_no = current_calendar.year, current_calendar.week
YEAR_WEEK = str(year_no) + '-' + str(week_no)


def download_pdf_from(**kwargs):
    brand_name = kwargs.get('brand_name')
    url = kwargs.get('url')
    default_name = brand_name + '-' + YEAR_WEEK + '.pdf'
    file_name = RESOURCES_PATH / kwargs.get('filename', default_name)

    response = requests.get(url)
    with open(file_name, "wb") as f:
        f.write(response.content)

