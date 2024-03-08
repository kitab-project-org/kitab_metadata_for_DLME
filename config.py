"""
Configuration data for loading the OpenITI/KITAB metadata into the DLME.
"""


# release number of the OpenITI release this data is related to:
release = "2023.1.8"

# license:
license = "Creative Commons Attribution Non Commercial Share Alike 4.0 International"

# URL for instructions on how to batch download all OpenITI and KITAB data:
download_descr_url = "https://kitab-project.org/data/download"

#######################
# PROJECT DESCRIPTION #
#######################

# description of the OpenITI and KITAB projects:
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

project_descr_ar = """
مبادرة النصوص الإسلامية المفتوحة (OpenITI) هي جهد متعدد المؤسسات يقوده باحثون في معهد جامعة الآغا خان لدراسة الحضارات الإسلامية في لندن، ومعهد روشان للدراسات الفارسية في جامعة ميريلاند، كوليدج بارك، وجامعة هامبورغ. يهدف إلى تطوير البنية التحتية الرقمية لدراسة الثقافات الإسلامية.

منذ تأسيسها في عام 2016، ركز عمل OpenITI على المهام الضرورية لبناء القدرات الرقمية في الدراسات الإسلامية، بما في ذلك تحسين التعرف البصري على الأحرف (OCR) العربية والتعرف على خط اليد  (HTR) العربي، وتطوير معايير متينة لل (OCR) وال (HTR) للخط العربي، ولإخراجاتهما ولتكويد النص، وإنشاء منصات للإنتاج التعاوني لمجموعات نصوص إسلامية وللتحقيق الرقمي.

يأتي تركيز OpenITI الثانوي من عملنا في ال(OCR) وال(HTR): نريد إنشاء مجموعة علمية من نصوص إسلامية قابلة للتنفيذ الآلي ومتوافقة مع المعايير العلمية، وتغطي عددًا متزايدًا باستمرار من النصوص الفارسية والعربية والتركية العثمانية والأردية. سنجعل هذه النصوص متاحة في مجموعة متنوعة من الصيغ (نص بسيط OpenITI mARkdown، TEI XML) ونثريها بأكبر قدر ممكن من البيانات الوصفية الموثوقة. يرجى الاطلاع على صفحة مشروع مجموعة OpenITI للمزيد من المعلومات.

https://openiti.org/about.html

يقوم مشروع KITAB بتطوير مناهج كشف كيفية اقتباس المؤلفين من النصوص السابقة. كثيرًا ما استخدم المؤلفون باللغة العربية الأعمال السابقة، وقاموا بتقطيعها إلى أجزاء وإعادة تشكيلها لمعالجة وجهات نظرهم واهتماماتهم. نحن نعمل على اكتشاف العلاقات بين هذه النصوص وكذلك الأنظمة التناصية التي تتواجد فيها.

https://kitab-project.org/about/

"""

######################
# OBJECT DESCRIPTION #
######################

# Template for the description of each object (row in the tsv file).
# NB: use : `obj_descr_en.format(**row_dict)`

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

{uncorrected_ocr_en}
""" % (release, download_descr_url)

obj_descr_ar = """
المؤلف: {author_ar}

نص يمكن قراءته آليًا وبيانات إعادة استخدام النص (من إصدار OpenITI %s).

نص يمكن قراءته آليًا: {text_url}

توثق مجموعات بيانات إعادة استخدام النص KITAB (https://kitab-project.org/data#passim-text-reuse-data-sets) التداخل بين النص الحالي والنصوص الأخرى في مجموعة مبادرة النصوص الإسلامية المفتوحة OpenITI.

مجموعة البيانات التي توثق التداخل بين النص الحالي ومجموعة OpenITI بأكملها: {one2all_data_url}

الإحصائيات حول التداخل بين النص الحالي وجميع النصوص الأخرى في مجموعة OpenITI: {one2all_stats_url}

التمثيل البصري للتداخل بين النص الحالي ومجموعة OpenITI بأكملها: {one2all_vis_url}

مجموعات البيانات التي توثق التداخل بين النص الحالي ونص واحد آخر ("مقارنة زوجية"): {pairwise_data_url}

للحصول على إرشادات حول تحميل كافة بيانات KITAB وOpenITI دفعة واحدة، راجع %s.

{uncorrected_ocr_ar}
""" % (release, download_descr_url)
print(obj_descr_ar)
