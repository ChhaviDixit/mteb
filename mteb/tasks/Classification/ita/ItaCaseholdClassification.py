from __future__ import annotations

from mteb.abstasks.AbsTaskClassification import AbsTaskClassification
from mteb.abstasks.TaskMetadata import TaskMetadata


class ItaCaseholdClassification(AbsTaskClassification):
    metadata = TaskMetadata(
        name="ItaCaseholdClassification",
        dataset={
            "path": "itacasehold/itacasehold",
            "revision": "fafcfc4fee815f7017848e54b26c47ece8ff1626",
        },
        description="An Italian Dataset consisting of 1101 pairs of judgments and their official holdings between the years 2019 and 2022 from the archives of Italian Administrative Justice categorized with 64 subjects.",
        reference="https://doi.org/10.1145/3594536.3595177",
        type="Classification",
        category="s2s",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["ita-Latn"],
        main_score="accuracy",
        date=("2019-01-01", "2022-12-31"),
        domains=["Legal", "Government", "Written"],
        dialect=[],
        task_subtypes=[],
        license="apache-2.0",
        annotations_creators="expert-annotated",
        sample_creation="found",
        bibtex_citation=r"""
@inproceedings{10.1145/3594536.3595177,
  abstract = {Legal holdings are used in Italy as a critical component of the legal system, serving to establish legal precedents, provide guidance for future legal decisions, and ensure consistency and predictability in the interpretation and application of the law. They are written by domain experts who describe in a clear and concise manner the principle of law applied in the judgments.We introduce a legal holding extraction method based on Italian-LEGAL-BERT to automatically extract legal holdings from Italian cases. In addition, we present ITA-CaseHold, a benchmark dataset for Italian legal summarization. We conducted several experiments using this dataset, as a valuable baseline for future research on this topic.},
  address = {New York, NY, USA},
  author = {Licari, Daniele and Bushipaka, Praveen and Marino, Gabriele and Comand\'{e}, Giovanni and Cucinotta, Tommaso},
  booktitle = {Proceedings of the Nineteenth International Conference on Artificial Intelligence and Law},
  doi = {10.1145/3594536.3595177},
  isbn = {9798400701979},
  keywords = {Italian-LEGAL-BERT, Holding Extraction, Extractive Text Summarization, Benchmark Dataset},
  location = {<conf-loc>, <city>Braga</city>, <country>Portugal</country>, </conf-loc>},
  numpages = {9},
  pages = {148–156},
  publisher = {Association for Computing Machinery},
  series = {ICAIL '23},
  title = {Legal Holding Extraction from Italian Case Documents using Italian-LEGAL-BERT Text Summarization},
  url = {https://doi.org/10.1145/3594536.3595177},
  year = {2023},
}
""",
    )

    def dataset_transform(self):
        self.dataset = self.dataset.rename_columns(
            {"summary": "text", "materia": "label"}
        )
