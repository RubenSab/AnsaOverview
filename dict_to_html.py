from airium import Airium

class DictToHtml:

    def __init__(self, categories: dict,
        lang, title, mention_link, mention_link_text, description,
        output_filename, css_filename
    ):
        self.categories = categories
        self.lang = lang
        self.title = title
        self.mention_link = mention_link
        self.mention_link_text = mention_link_text
        self.description = description
        self.output_filename = output_filename
        self.css_filename = css_filename

    def generate_html(self):
        a = Airium()

        a('<!DOCTYPE html>')
        with a.html(lang=self.lang):
            with a.head():
                a.meta(charset="utf-8")
                a.link(href=self.css_filename, rel='stylesheet')
                a.title(_t=self.title)

            with a.body():
                with a.div(klass="container"):
                    with a.div(klass="title-row"):
                        with a.h1():
                            a(self.title)
                        with a.em():
                            a(self.description)
                        a.br()
                        with a.a(href=self.mention_link, klass = "mention-link"):
                            a(self.mention_link_text)
                    a.hr()

                    for category, content in self.categories.items():
                        with a.h3():
                            a(category)
                        with a.p():
                            a(content)

        with open(self.output_filename, 'wb') as f:
            f.write(bytes(a))
