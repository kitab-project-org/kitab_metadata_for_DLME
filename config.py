"""
Configuration data for loading the OpenITI/KITAB metadata into the DLME.
"""


# release number of the OpenITI release this data is related to:
release = "2023.1.8"

# license:
license = "Creative Commons Attribution Non Commercial Share Alike 4.0 International"

# URL for instructions on how to batch download all OpenITI and KITAB data:
download_descr_url = "https://kitab-project.org/data/download"

# if necessary, update the intro text from the OpenITI project website (https://openiti.org/about.html): 
project_descr_en = """
The Open Islamicate Texts Initiative (OpenITI) is a multi-institutional effort
led by researchers at the Aga Khan University’s Institute for the Study of Muslim Civilisations in London,
Roshan Institute for Persian Studies at the University of Maryland, College Park,
and Universität Hamburg that aims to develop the digital infrastructure for the study of Islamicate cultures.

Since its founding in 2016, OpenITI's work has focused on the tasks necessary to build digital capacity in Islamicate studies,
including improving Arabic-script optical character recognition (OCR) and handwritten text recognition (HTR),
developing robust Arabic-script standards for OCR and HTR output and text encoding,
and creating platforms for the collaborative creation of Islamicate text corpora and digital editions.

OpenITI's secondary focus comes out of our OCR and HTR work:
we want to create a machine-actionable and standards-compliant scholarly corpus of Islamicate texts,
covering an ever-increasing number of Persian, Arabic, Ottoman Turkish, and Urdu works.
We will make these works available in a variety of formats (plaintext, OpenITI mARkdown, TEI XML)
and enrich them with as much verified metadata as possible. Please see the OpenITI corpus project page for more information.

https://openiti.org/about.html

The KITAB project is developing methods that detect how authors copied from previous works.
Arabic authors frequently made use of past works, cutting them into pieces and reconstituting
them to address their own outlooks and concerns.
We are working to discover relationships between these texts
and also the profoundly intertextual circulatory systems in which they sit.

https://kitab-project.org/about/
"""

# TO DO:`translate into Arabic:
project_descr_ar = """
The Open Islamicate Texts Initiative (OpenITI) is a multi-institutional effort
led by researchers at the Aga Khan University’s Institute for the Study of Muslim Civilisations in London,
Roshan Institute for Persian Studies at the University of Maryland, College Park,
and Universität Hamburg that aims to develop the digital infrastructure for the study of Islamicate cultures.

Since its founding in 2016, OpenITI's work has focused on the tasks necessary to build digital capacity in Islamicate studies,
including improving Arabic-script optical character recognition (OCR) and handwritten text recognition (HTR),
developing robust Arabic-script standards for OCR and HTR output and text encoding,
and creating platforms for the collaborative creation of Islamicate text corpora and digital editions.

OpenITI's secondary focus comes out of our OCR and HTR work:
we want to create a machine-actionable and standards-compliant scholarly corpus of Islamicate texts,
covering an ever-increasing number of Persian, Arabic, Ottoman Turkish, and Urdu works.
We will make these works available in a variety of formats (plaintext, OpenITI mARkdown, TEI XML)
and enrich them with as much verified metadata as possible. Please see the OpenITI corpus project page for more information.

https://openiti.org/about.html

The KITAB project is developing methods that detect how authors copied from previous works.
Arabic authors frequently made use of past works, cutting them into pieces and reconstituting
them to address their own outlooks and concerns.
We are working to discover relationships between these texts
and also the profoundly intertextual circulatory systems in which they sit.

https://kitab-project.org/about/
"""

# description of the single objects: 
# NB: use : `project_descr_en.format(**row_dict)
obj_descr_en = """
Author: {author_lat}

Machine-readable text and text reuse datasets (from OpenITI release %s).

Machine-readable text: {text_url}

The KITAB text reuse datasets (https://kitab-project.org/data#passim-text-reuse-data-sets)
document the overlap between the present work and other texts in the Open Islamicate Texts Initiative corpus.

Dataset documenting the overlap between the present text and the entire OpenITI corpus: {one2all_data_url}

Statistics on the overlap between the present text and all other texts in the OpenITI corpus: {one2all_stats_url}

Visualization of the overlap between the present text and the entire OpenITI corpus: {one2all_vis_url}

Datasets documenting the overlap between the present text and a single other text (“pairwise”): {pairwise_data_url}

For instructions on batch downloading all of the KITAB and OpenITI data, see %s

{uncorrected_ocr}
""" % (release, download_descr_url)

# TO DO: translate into Arabic! 
obj_descr_ar = """
المؤلف: {author_ar}

Machine-readable text and text reuse datasets (from OpenITI release %s).

Machine-readable text: {text_url}

The KITAB text reuse datasets (https://kitab-project.org/data#passim-text-reuse-data-sets)
document the overlap between the present work and other texts in the Open Islamicate Texts Initiative corpus.

Dataset documenting the overlap between the present text and the entire OpenITI corpus: {one2all_data_url}

Statistics on the overlap between the present text and all other texts in the OpenITI corpus: {one2all_stats_url}

Visualization of the overlap between the present text and the entire OpenITI corpus: {one2all_vis_url}

Datasets documenting the overlap between the present text and a single other text (“pairwise”): {pairwise_data_url}

For instructions on batch downloading all of the KITAB and OpenITI data, see %s.

{uncorrected_ocr}
""" % release
