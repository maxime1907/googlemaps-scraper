import csv

HEADER = [
    "id_review",
    "caption",
    "relative_date",
    "retrieval_date",
    "rating",
    "username",
    "n_review_user",
    "n_photo_user",
    "url_user",
]
HEADER_W_SOURCE = [
    "id_review",
    "caption",
    "relative_date",
    "retrieval_date",
    "rating",
    "username",
    "n_review_user",
    "n_photo_user",
    "url_user",
    "url_source",
]


def csv_writer(source_field, ind_sort_by, path="data/"):
    outfile = ind_sort_by + "_gm_reviews.csv"
    targetfile = open(path + outfile, mode="w", encoding="utf-8", newline="\n")
    writer = csv.writer(targetfile, quoting=csv.QUOTE_MINIMAL)

    if source_field:
        h = HEADER_W_SOURCE
    else:
        h = HEADER
    writer.writerow(h)

    return writer
