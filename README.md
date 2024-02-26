OpenITI / KITAB metadata for the Digital Library of the Middle East.

This repository contains: 

* kitab_metadata_for_DLME_latest_release.tsv : all relevant fields for the latest release of OpenITI texts and KITAB text reuse data
* generate_metadata_for_DLME.py: the script that generates the metadata tsv file
* config.py: contains the release version number, license, and texts for the description of the project and each data point. 

## metadata fields:

| field | description |
|-------|-------------|
| version_uri | OpenITI digital text version URI |
| date | death date of the author |
| author_ar | author name(s) in Arabic script; " :: "-separated |
| author_lat | author name(s) in Latin script; " :: "-separated |
| title_ar | title of the work in Arabic script; " :: "-separated |
| title_lat | title of the work in Latin script; " :: "-separated |
| ed_info | information on the original (printed) edition of the text |
| tags | genre/author/version tags from OpenITI |
| text_url | URL of the full text |
| one2all_data_url | URL of the text reuse data file detailing the overlap of the current text with any other text in the corpus |
| one2all_stats_url | URL of the text reuse data file containing statistics on the overlap of the current text with any other text in the corpus |
| one2all_vis_url | URL of the one-to-all text reuse visualisation on the KITAB website |
| pairwise_data_url | URL of the folder containing all text reuse data files detailing the overlap of the current file with a single other text file |
| uncorrected_ocr | statement on uncorrected OCR (empty for all non-OCR'ed texts) |