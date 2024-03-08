"""
Prepare metadata for ingestion into the DLME
(Digital Library of the Middle East)
"""

import re
import csv


release = "2023.1.8"
infp = "../../kitab-metadata-automation/releases/OpenITI_metadata_2023-1-8.csv"
outfp = "kitab_metadata_for_DLME_latest_release.tsv"

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



def generate_metadata():
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

    with open(outfp, mode="w", encoding="utf-8") as file:
        file.write("\n".join(new_csv))

if __name__ == "__main__":
    generate_metadata()
