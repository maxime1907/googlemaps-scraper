# -*- coding: utf-8 -*-
from termcolor import colored

from gmaps_scraper.csv import csv_writer
from gmaps_scraper.googlemaps import GoogleMapsScraper

ind = {"most_relevant": 0, "newest": 1, "highest_rating": 2, "lowest_rating": 3}


class GMapsScraper:
    def __init__(
        self,
        *,
        scrape: str,
        driver: str,
        number: int,
        input: str,
        sort_by: str,
        place: bool,
        debug: bool,
        source: bool
    ):
        self.scrape = scrape
        self.driver = driver
        self.number = number
        self.input = input
        self.sort_by = sort_by
        self.place = place
        self.debug = debug
        self.source = source

    def run(self) -> None:
        if self.scrape == "review":
            # store reviews in CSV file
            writer = csv_writer(self.source, self.sort_by)

            with GoogleMapsScraper(driver=self.driver, debug=self.debug) as scraper:
                with open(self.input, "r") as urls_file:
                    for url in urls_file:
                        if self.place:
                            print(scraper.get_account(url))
                        else:
                            error = scraper.sort_by(url, ind[self.sort_by])

                            if error == 0:

                                n = 0

                                # if ind[self.sort_by] == 0:
                                #    scraper.more_reviews()

                                while n < self.number:

                                    # logging to std out
                                    print(colored("[Review " + str(n) + "]", "cyan"))

                                    reviews = scraper.get_reviews(n)
                                    if len(reviews) == 0:
                                        break

                                    for r in reviews:
                                        row_data = list(r.values())
                                        if self.source:
                                            row_data.append(url[:-1])

                                        writer.writerow(row_data)

                                    n += len(reviews)
        elif self.scrape == "place":
            with GoogleMapsScraper(driver=self.driver, debug=True) as scraper:
                scraper.get_places(keyword_list=["romantic restaurant"])
