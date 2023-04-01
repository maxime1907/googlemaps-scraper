import logging

import click

from gmaps_scraper.scraper import GMapsScraper

logger = logging.getLogger(__name__)

SCRAPE_OPTIONS = ["review", "chrome"]
DRIVER_OPTIONS = ["chrome", "edge"]


@click.command()
@click.option(
    "--log-level",
    help="Logging level",
    default="INFO",
    type=click.Choice(list(logging._nameToLevel.keys())),
)
@click.option(
    "--log-format",
    help="Logging format",
    default="%(asctime)s | %(levelname)s | %(message)s",
    type=str,
)
@click.option(
    "--log-dateformat",
    help="Logging date format",
    default="%Y-%m-%dT%H:%M:%S%z",
    type=str,
)
@click.option(
    "--scrape",
    type=click.Choice(SCRAPE_OPTIONS),
    default=SCRAPE_OPTIONS[0],
    help="Scrape type to use",
)
@click.option(
    "--driver",
    type=click.Choice(DRIVER_OPTIONS),
    default=DRIVER_OPTIONS[0],
    help="Driver to use",
)
@click.option(
    "--number", "--N", type=int, default=100, help="Number of reviews to scrape"
)
@click.option("--input", "--i", type=str, default="urls.txt", help="target URLs file")
@click.option(
    "--sort_by",
    type=str,
    default="newest",
    help="most_relevant, newest, highest_rating or lowest_rating",
)
@click.option("--place", is_flag=True, help="Scrape place metadata")
@click.option(
    "--debug", is_flag=True, help="Run scraper using browser graphical interface"
)
@click.option(
    "--source",
    is_flag=True,
    help="Add source url to CSV file (for multiple urls in a single file)",
)
def cli(
    log_level: str,
    log_format: str,
    log_dateformat: str,
    scrape: str,
    driver: str,
    number: int,
    input: str,
    sort_by: str,
    place: bool,
    debug: bool,
    source: bool,
) -> None:
    """
    Google Maps reviews scraper
    """

    logging.basicConfig(
        level=log_level,
        format=log_format,
        datefmt=log_dateformat,
    )

    scraper = GMapsScraper(
        scrape=scrape,
        driver=driver,
        number=number,
        input=input,
        sort_by=sort_by,
        place=place,
        source=source,
        debug=debug,
    )
    scraper.run()
