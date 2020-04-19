from docutils import nodes
from pelican import readers
from pelican import signals
from pelican.readers import PelicanHTMLTranslator
from pelican.utils import slugify
import re

LINK_CHAR = "*"
LINK_TITLE = "Permalink to this headline"
SLUG_REGEX_SUBSTITUTIONS = []
NEED_TO_ADD_ID = True


def my_slugify(text):
    return slugify(text, SLUG_REGEX_SUBSTITUTIONS)


def init_headerid(sender):
    global LINK_CHAR, LINK_TITLE, SLUG_REGEX_SUBSTITUTIONS, NEED_TO_ADD_ID

    LINK_CHAR = sender.settings.get("HEADERID_LINK_CHAR", LINK_CHAR)
    LINK_TITLE = sender.settings.get("HEADERID_LINK_TITLE", LINK_TITLE)
    SLUG_REGEX_SUBSTITUTIONS = sender.settings.get(
        "SLUG_REGEX_SUBSTITUTIONS", SLUG_REGEX_SUBSTITUTIONS
    )
    NEED_TO_ADD_ID = not bool(
        # if "pelican-toc" is used, we do not have to add "id" attr
        set(["pelican-toc"]).intersection(set(sender.settings.get("PLUGINS", [])))
    )


def register():
    signals.initialized.connect(init_headerid)

    class HeaderIDPatchedPelicanHTMLTranslator(PelicanHTMLTranslator):
        # fix Chinese section id slugify
        def visit_section(self, node):
            if NEED_TO_ADD_ID and "names" in node:
                section_id = my_slugify(node["names"][0])
                if "ids" in node and section_id != "":
                    node["ids"][0] = section_id

            PelicanHTMLTranslator.visit_section(self, node)

        def depart_title(self, node):
            close_tag = self.context[-1]
            parent = node.parent
            anchor_name = ""

            if NEED_TO_ADD_ID and isinstance(parent, nodes.section) and parent["ids"]:
                anchor_name = parent["ids"][0]
            elif isinstance(node, nodes.title):
                anchor_name = my_slugify(node.astext())

            # add permalink anchor
            if re.match(r"</[hH]\d+>", close_tag):
                self.body.append(
                    '<a class="headerlink" href="#%s" title="%s">%s</a>'
                    % (anchor_name, LINK_TITLE, LINK_CHAR)
                )

            PelicanHTMLTranslator.depart_title(self, node)

    readers.PelicanHTMLTranslator = HeaderIDPatchedPelicanHTMLTranslator
