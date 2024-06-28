"""
Prepare metadata for ingestion into the DLME
(Digital Library of the Middle East)
and generate the config.yml file from the config_template.yml.

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Before running this script, make sure the config_template.yml is updated
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

"""

import re
import csv
import yaml  # pip install pyyaml
import requests
import os

outfp = "kitab_metadata_for_DLME_latest_release.tsv"

with open("config_template.yml", mode="r", encoding="utf-8") as file:
    config_d = yaml.safe_load(file)

# generate some global variables:

release = config_d["release"]

gh_url = "https://raw.githubusercontent.com/"
kitab_url = gh_url + "kitab-project-org/"
text_url = gh_url+"openiti/release/master/{}"
one2all_data_url = kitab_url+"one_to_all/v%s/msdata/%s_{}_all.csv" % (release, release)
one2all_stats_url = kitab_url+"one_to_all/v%s/stats/%s_{}_stats.csv" % (release, release)
one2all_vis_url = "https://kitab-project.org/explore/#/visualise/%s/?books={}" % release
pairwise_data_url = "https://dev.kitab-project.org/%s-pairwise/{}/" % release
thumbnail_url = kitab_url+"/reuse-thumbnails/main/thumbnails/{}.jpg"

uncorrected_ocr_message_en = "WARNING: this is a text generated using OCR; it has not been post-corrected."
uncorrected_ocr_message_ar = "تحذير: هذا نص تم إنشاؤه باستخدام التعرف البصري على الأحرف؛ لم يتم تصحيحه لاحقًا."


relevant_keys = [
    'version_uri',
    'date',
    'author_ar',
    'author_lat',
    'title_ar',
    'title_lat',
    'ed_info',
    'tags',
    ]
generated_keys = [
    "text_url",
    "one2all_data_url",
    "one2all_stats_url",
    "one2all_vis_url",
    "pairwise_data_url",
    "thumbnail_url",
    "uncorrected_ocr_en",
    "uncorrected_ocr_ar",
    ]
header = relevant_keys + generated_keys

def download_file(url, path):
    r = requests.get(url)
    with open(path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)    

def generate_metadata(config_d):
    # download the release metadata from GitHub:
    print("downloading", config_d["release_meta"])
    infp = "temp.tsv"
    download_file(config_d["release_meta"], infp)
    print("download finished. Start generating metadata file.")
    
    # generate the metadata tsv in the required format for the DLME:
    new_csv = ["\t".join(header), ]
    with open(infp, mode="r", encoding="utf-8") as file:
        data = csv.DictReader(file, delimiter="\t")
        for i, d in enumerate(data):
            # include only primary version of each text:
            if d["status"] == "sec":
                continue

            # copy the relevant fields:
            row = []
            for k in relevant_keys:
                row.append(d[k])

            # generate the URLs to data and visualisations:
            path = d["local_path"].strip(".").strip("/")
            uri_w_extension = path.split("/")[-1]
            id_w_extension = ".".join(uri_w_extension.split(".")[2:])
            id_ = id_w_extension.split("-")[0]
            row.append(text_url.format(path))
            row.append(one2all_data_url.format(id_))
            row.append(one2all_stats_url.format(id_))
            row.append(one2all_vis_url.format(id_w_extension))
            row.append(pairwise_data_url.format(id_w_extension))
            row.append(thumbnail_url.format(id_w_extension))
            if "UNCORRECTED_OCR" in d["tags"]:
                row.append(uncorrected_ocr_message_en)
                row.append(uncorrected_ocr_message_ar)
            else:
                row.append("")
                row.append("")

            # do not include files that are not public:
            if "noorlib" in path.lower():
                print("NOORLIB!")
                continue

            # add the new row to the csv file:
            new_csv.append("\t".join(row))

    # remove the temporary downloaded metadata file:
    os.remove(infp)

    with open(outfp, mode="w", encoding="utf-8") as file:
        file.write("\n".join(new_csv))

def generate_config_yaml(config_d, splitter="# PROJECT DESCRIPTION #"):
    """Generate the config.yml file from the config_template.yml file.

    Args:
        config_d (dict): configuration dictionary,
            loaded from config_template.yml
        splitter (str): to split the yml header from its body
    """
    with open("config_template.yml", mode="r", encoding="utf-8") as file:
        yml_s = file.read()

    # split off the header
    # in order not to replace the placeholder strings there:
    head, body = yml_s.split(splitter)

    # replace placeholders in the template config file
    # with the relevant variables:
    for k, v in config_d["placeholder_strings"].items():
        body = re.sub(k, config_d[v], body)

    # insert <br/> tags for new lines in descriptions:
    body = re.sub("\n( *)\n", r"<br/>\n\1\n", body)
    print(repr(body))

    # add a warning at the top of the config file:
    warning = """\
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# IMPORTANT: This config file was created by the
# `generate_metadata_for_DLME.py` script.
# DO NOT MANUALLY CHANGE THIS CONFIG FILE.
# Make any changes in the `config_template.yml` file
# and re-run the `generate_metadata_for_DLME` script.
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
"""
    yml_s = warning + head + splitter + body

    # write the new yaml file:
    with open("config.yml", mode="w", encoding="utf-8") as file:
        file.write(yml_s)

if __name__ == "__main__":
    
    generate_metadata(config_d)
    generate_config_yaml(config_d)
