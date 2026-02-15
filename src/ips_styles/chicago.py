"""Chicago author-date bibliography style for pybtex.

Formats bibliography entries in Chicago Manual of Style 17th edition
author-date format:

  Article:  Author. Year. "Title." *Journal* Volume(Number): Pages. doi:DOI. URL.
  Book:     Author. Year. *Title*. Edition. Place: Publisher. doi:DOI. URL.
  Chapter:  Author. Year. "Title." In *Book*, edited by Editor, Pages. Place: Publisher. doi:DOI. URL.

Labels are empty (hidden via CSS) — inline citations use sphinxcontrib-bibtex's
author_year reference style instead.
"""

import re

from pybtex.richtext import Symbol, Text
from pybtex.style.formatting import BaseStyle, toplevel
from pybtex.style.labels import BaseLabelStyle
from pybtex.style.template import (
    field, first_of, href, join, names, optional, optional_field, sentence,
    tag, together, words
)


def dashify(text):
    dash_re = re.compile(r'-+')
    return Text(Symbol('ndash')).join(text.split(dash_re))


pages = field('pages', apply_func=dashify)


class ChicagoLabelStyle(BaseLabelStyle):
    """Use citation keys as labels (hidden by CSS).

    Labels must be unique for sphinxcontrib-bibtex anchoring to work.
    The CSS hides them visually — inline citations use author-year instead.
    """

    def format_labels(self, sorted_entries):
        for entry in sorted_entries:
            yield entry.key


class Style(BaseStyle):
    """Chicago author-date bibliography style.

    Key differences from the default ``unsrt``/``alpha`` styles:

    1. Year appears immediately after the author block (not at the end).
    2. Article and chapter titles are enclosed in quotation marks.
    3. Labels are empty (no ``[CK17]``-style codes).
    4. Entries are sorted alphabetically by author, then year, then title.
    """

    default_name_style = 'lastfirst'
    default_label_style = 'number'   # overridden in __init__
    default_sorting_style = 'author_year_title'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_style = ChicagoLabelStyle()
        self.format_labels = self.label_style.format_labels

    # ------------------------------------------------------------------
    # Name formatting
    # ------------------------------------------------------------------

    def format_names(self, role, as_sentence=True):
        formatted_names = names(role, sep=', ', sep2=' and ', last_sep=', and ')
        if as_sentence:
            return sentence [formatted_names]
        else:
            return formatted_names

    def format_author_or_editor(self, e):
        return first_of [
            optional [self.format_names('author')],
            self.format_editor(e),
        ]

    def format_editor(self, e, as_sentence=True):
        editors = self.format_names('editor', as_sentence=False)
        if 'editor' not in e.persons:
            return editors
        word = 'editors' if len(e.persons['editor']) > 1 else 'editor'
        result = join(sep=', ') [editors, word]
        if as_sentence:
            return sentence [result]
        else:
            return result

    # ------------------------------------------------------------------
    # Title formatting
    # ------------------------------------------------------------------

    def format_article_title(self, e, which_field):
        """Article/chapter title in quotation marks, period inside closing quote."""
        formatted_title = field(
            which_field, apply_func=lambda text: text.capitalize()
        )
        return join ['\u201c', formatted_title, '.\u201d']

    def format_btitle(self, e, which_field, as_sentence=True):
        """Book title in italics."""
        formatted_title = tag('em') [field(which_field)]
        if as_sentence:
            return sentence [formatted_title]
        else:
            return formatted_title

    def format_title(self, e, which_field, as_sentence=True):
        """Plain title (fallback)."""
        formatted_title = field(
            which_field, apply_func=lambda text: text.capitalize()
        )
        if as_sentence:
            return sentence [formatted_title]
        else:
            return formatted_title

    # ------------------------------------------------------------------
    # Year
    # ------------------------------------------------------------------

    def format_year(self, e):
        return sentence [field('year')]

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def format_volume_and_series(self, e, as_sentence=True):
        volume_and_series = optional [
            words [
                together [
                    'Volume' if as_sentence else 'volume',
                    field('volume'),
                ],
                optional [words ['of', field('series')]],
            ]
        ]
        number_and_series = optional [
            words [
                join(sep=Symbol('nbsp')) [
                    'Number' if as_sentence else 'number',
                    field('number'),
                ],
                optional [words ['in', field('series')]],
            ]
        ]
        series = optional_field('series')
        result = first_of [volume_and_series, number_and_series, series]
        if as_sentence:
            return sentence(capfirst=True) [result]
        else:
            return result

    def format_chapter_and_pages(self, e):
        return join(sep=', ') [
            optional [together ['chapter', field('chapter')]],
            optional [together ['pages', pages]],
        ]

    def format_edition(self, e):
        return optional [
            words [
                field('edition', apply_func=lambda x: x.lower()),
                'edition',
            ]
        ]

    # ------------------------------------------------------------------
    # Web references (DOI, URL, arXiv)
    # ------------------------------------------------------------------

    def format_web_refs(self, e):
        return sentence [
            optional [self.format_doi(e)],
            optional [self.format_eprint(e)],
            optional [self.format_url(e)],
        ]

    def format_doi(self, e):
        url = join ['https://doi.org/', field('doi', raw=True)]
        return href(url) [join ['doi:', field('doi', raw=True)]]

    def format_eprint(self, e):
        url = join ['https://arxiv.org/abs/', field('eprint', raw=True)]
        return href(url) [join ['arXiv:', field('eprint', raw=True)]]

    def format_url(self, e):
        url = field('url', raw=True)
        return href(url) [url]

    def format_isbn(self, e):
        return join(sep=' ') ['ISBN', field('isbn')]

    # ------------------------------------------------------------------
    # Entry type templates
    # ------------------------------------------------------------------

    def get_article_template(self, e):
        volume_and_pages = first_of [
            optional [
                join [
                    field('volume'),
                    optional ['(', field('number'), ')'],
                    ':', pages,
                ],
            ],
            words ['pages', pages],
        ]
        template = toplevel [
            self.format_names('author'),
            self.format_year(e),
            self.format_article_title(e, 'title'),
            sentence [
                tag('em') [field('journal')],
                optional [volume_and_pages],
            ],
            sentence [optional_field('note')],
            self.format_web_refs(e),
        ]
        return template

    def get_book_template(self, e):
        template = toplevel [
            self.format_author_or_editor(e),
            self.format_year(e),
            self.format_btitle(e, 'title'),
            self.format_volume_and_series(e),
            sentence [
                field('publisher'),
                optional_field('address'),
                self.format_edition(e),
            ],
            sentence [optional_field('note')],
            self.format_web_refs(e),
        ]
        return template

    def get_incollection_template(self, e):
        template = toplevel [
            sentence [self.format_names('author')],
            self.format_year(e),
            self.format_article_title(e, 'title'),
            words [
                'In',
                sentence [
                    optional [self.format_editor(e, as_sentence=False)],
                    self.format_btitle(e, 'booktitle', as_sentence=False),
                    self.format_volume_and_series(e, as_sentence=False),
                    self.format_chapter_and_pages(e),
                ],
            ],
            sentence [
                optional_field('publisher'),
                optional_field('address'),
                self.format_edition(e),
            ],
            self.format_web_refs(e),
        ]
        return template

    def get_inproceedings_template(self, e):
        template = toplevel [
            sentence [self.format_names('author')],
            self.format_year(e),
            self.format_article_title(e, 'title'),
            words [
                'In',
                sentence [
                    optional [self.format_editor(e, as_sentence=False)],
                    self.format_btitle(e, 'booktitle', as_sentence=False),
                    self.format_volume_and_series(e, as_sentence=False),
                    optional [pages],
                ],
            ],
            sentence [optional_field('note')],
            self.format_web_refs(e),
        ]
        return template

    def get_misc_template(self, e):
        template = toplevel [
            optional [sentence [self.format_names('author')]],
            optional [self.format_year(e)],
            optional [self.format_title(e, 'title')],
            sentence [
                optional [field('howpublished')],
            ],
            sentence [optional_field('note')],
            self.format_web_refs(e),
        ]
        return template

    def get_online_template(self, e):
        return self.get_misc_template(e)

    def get_dataset_template(self, e):
        return self.get_misc_template(e)

    def get_software_template(self, e):
        return self.get_misc_template(e)

    def get_patent_template(self, e):
        return self.get_misc_template(e)

    def get_booklet_template(self, e):
        return self.get_misc_template(e)

    def get_phdthesis_template(self, e):
        template = toplevel [
            sentence [self.format_names('author')],
            self.format_year(e),
            self.format_btitle(e, 'title'),
            sentence [
                first_of [
                    optional_field('type'),
                    'PhD thesis',
                ],
                field('school'),
                optional_field('address'),
            ],
            sentence [optional_field('note')],
            self.format_web_refs(e),
        ]
        return template

    def get_mastersthesis_template(self, e):
        template = toplevel [
            sentence [self.format_names('author')],
            self.format_year(e),
            self.format_title(e, 'title'),
            sentence [
                "Master's thesis",
                field('school'),
                optional_field('address'),
            ],
            sentence [optional_field('note')],
            self.format_web_refs(e),
        ]
        return template

    def get_techreport_template(self, e):
        template = toplevel [
            sentence [self.format_names('author')],
            self.format_year(e),
            self.format_title(e, 'title'),
            sentence [
                words [
                    first_of [
                        optional_field('type'),
                        'Technical Report',
                    ],
                    optional_field('number'),
                ],
                field('institution'),
                optional_field('address'),
            ],
            sentence [optional_field('note')],
            self.format_web_refs(e),
        ]
        return template

    def get_unpublished_template(self, e):
        template = toplevel [
            sentence [self.format_names('author')],
            self.format_year(e),
            self.format_title(e, 'title'),
            sentence [field('note')],
            self.format_web_refs(e),
        ]
        return template

    def get_proceedings_template(self, e):
        if 'editor' in e.persons:
            main_part = [
                self.format_editor(e),
                self.format_year(e),
                sentence [
                    self.format_btitle(e, 'title', as_sentence=False),
                    self.format_volume_and_series(e, as_sentence=False),
                ],
            ]
        else:
            main_part = [
                optional [sentence [field('organization')]],
                self.format_year(e),
                sentence [
                    self.format_btitle(e, 'title', as_sentence=False),
                    self.format_volume_and_series(e, as_sentence=False),
                ],
            ]
        template = toplevel [
            main_part + [
                sentence [
                    optional_field('publisher'),
                    optional_field('address'),
                ],
                sentence [optional_field('note')],
                self.format_web_refs(e),
            ]
        ]
        return template

    def get_inbook_template(self, e):
        template = toplevel [
            self.format_author_or_editor(e),
            self.format_year(e),
            sentence [
                self.format_btitle(e, 'title', as_sentence=False),
                self.format_chapter_and_pages(e),
            ],
            self.format_volume_and_series(e),
            sentence [
                field('publisher'),
                optional_field('address'),
                optional [
                    words [field('edition'), 'edition']
                ],
            ],
            sentence [optional_field('note')],
            self.format_web_refs(e),
        ]
        return template

    def get_manual_template(self, e):
        template = toplevel [
            optional [sentence [self.format_names('author')]],
            optional [self.format_year(e)],
            self.format_btitle(e, 'title'),
            sentence [
                optional_field('organization'),
                optional_field('address'),
                self.format_edition(e),
            ],
            sentence [optional_field('note')],
            self.format_web_refs(e),
        ]
        return template
