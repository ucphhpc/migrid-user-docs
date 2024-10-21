# This file is part of the MiGrid extension for Sphinx documentation.
#
# Accordion extension is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Accordion extension is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Aria Accordion.  If not, see <https://www.gnu.org/licenses/>.

import os
from docutils.nodes import Element, General, Text, container
from sphinx.util.docutils import SphinxDirective
from docutils.parsers.rst import directives


class Details(General, Element):
    """
    Details node representing the parent of Summary and Content.
    Using the details HTML element allows for HTML5 built-in accessibility.
    """
    pass


class Summary(General, Element):
    """
    Summary node representing the child of Details.
    """
    pass


class AccordionDirective(SphinxDirective):
    """
    Directive to create a new accordion.

    Arguments:
        heading or summary of text (str): The text to display in the accordion summary.

    Options:
        expand (flag): If set, the accordion will be expanded by default.

    Example usage:
        .. accordion:: Summary text
           :expand:

           Accordion content goes here.
    """

    has_content = True
    required_arguments = 1
    optional_arguments = 100  # Needed for optional arguments and nested elements
    option_spec = {'expand': directives.flag}
    counter = 0  # Used to generate unique IDs for accordions, needed for better accessibility

    def run(self):
        """
        Create a new accordion with the given summary text and content.

        Returns:
            list: A list containing the Details node representing the accordion.
        """
        self._validate_arguments()
        details_node = self._create_details_node()
        summary_node = self._create_summary_node()
        content_node = self._create_content_node()

        details_node.append(summary_node)
        details_node.append(content_node)

        self._set_accessibility_attributes(summary_node, content_node)

        return [details_node]

    def _validate_arguments(self):
        """
        Validate the arguments passed to the directive.
        Raises an error if no summary text is provided.
        """
        if not self.arguments:
            raise self.error('Accordion directive requires one argument: the summary text')

    def _create_details_node(self):
        """
        Create a new Details node and set the role and classes.

        Returns:
            Details: The created Details node.
        """
        details_node = Details()
        details_node['classes'].append('accordion')
        details_node['role'] = 'group'
        if 'expand' in self.options:
            details_node['open'] = 'open'
        return details_node

    def _create_summary_node(self):
        """
        Create a new Summary node and set the role, classes, and summary text.

        Returns:
            Summary: The created Summary node.
        """
        summary_node = Summary()
        summary_node['role'] = 'button'
        summary_node['classes'].append('accordion-summary')
        summary_text = ' '.join(self.arguments)
        summary_node.append(Text(summary_text))
        return summary_node

    def _create_content_node(self):
        """
        Create a new container node for the accordion content and parse the content.

        Returns:
            container: The created container node containing the parsed content.
        """
        content_node = container(classes=['accordion-content'])
        self.state.nested_parse(self.content, self.content_offset, content_node)
        return content_node

    @staticmethod
    def _set_accessibility_attributes(summary_node, content_node):
        """
        Set the aria-controls and aria-labelledby attributes for the summary and content nodes.

        Args:
            summary_node (Summary): The Summary node.
            content_node (container): The container node for the accordion content.
        """
        AccordionDirective.counter += 1
        content_id = f'accordion-{AccordionDirective.counter}'
        summary_node['aria-controls'] = content_id
        content_node['ids'].append(content_id)


def visit_details(self, node):
    """
    Visit the Details node and add the corresponding HTML element.

    Args:
        node (Details): The Details node.
    """
    attrs = {'class': 'accordion', 'role': 'region'}
    if 'open' in node:
        attrs['open'] = 'open'
    self.body.append(self.starttag(node, 'details', **attrs))


def depart_details(self, _node):
    """
    Depart the Details node and close the corresponding HTML element.
    """
    self.body.append('</details>\n')


def visit_summary(self, node):
    """
    Visit the Summary node and add the corresponding HTML element.

    Args:
        node (Summary): The Summary node.
    """
    attrs = {
        'class': 'accordion-summary',
        'aria-expanded': 'true' if 'open' in node.parent else 'false'
    }
    self.body.append(self.starttag(node, 'summary', **attrs))


def depart_summary(self, _node):
    """
    Depart the Summary node and close the corresponding HTML element.
    """
    self.body.append('</summary>\n')


def latex_visit_details(self, _node):
    """
    Visit the Details node in LaTeX and add the corresponding LaTeX command.

    Args:
        _node (Details): The Details node (unused).
    """
    self.body.append('\n\\begin{details}\n')


def latex_depart_details(self, _node):
    """
    Depart the Details node in LaTeX and close the corresponding LaTeX command.

    Args:
        _node (Details): The Details node (unused).
    """
    self.body.append('\n\\end{details}\n')


def latex_visit_summary(self, _node):
    """
    Visit the Summary node in LaTeX and add the corresponding LaTeX command.

    Args:
        _node (Summary): The Summary node (unused).
    """
    self.body.append('\\detailssummary{')


def latex_depart_summary(self, _node):
    """
    Depart the Summary node in LaTeX and close the corresponding LaTeX command.

    Args:
        _node (Summary): The Summary node (unused).
    """
    self.body.append('}\n')


def setup(app):

    """
    Set up the Sphinx extension.

    Args:
        app (Sphinx): The Sphinx application object.

    Returns:
        dict: A dictionary containing extension metadata.
    """
    app.add_directive('accordion', AccordionDirective)

    # Copy CSS file

    app.add_css_file('accordion.css')

    app.add_node(Details,
                 html=(visit_details, depart_details),
                 latex=(latex_visit_details, latex_depart_details))
    app.add_node(Summary,
                 html=(visit_summary, depart_summary),
                 latex=(latex_visit_summary, latex_depart_summary))

    return {
        'version': '0.1',
        'license': 'GPL-3.0-or-later',
        'author': 'Aputsiak Niels Janussen',
        'description': 'MiGrid extension Accordion for Sphinx documentation',
        'long_description': 'Accessibility focused accordion extension for Sphinx used in MiGrid User Docs',
        'url': 'https://github.com/aputtu/migrid-sphinx-ext',
        'classifiers': [
            'Development Status :: 3 - Alpha',
            'Framework :: Sphinx',
            'Intended Audience :: Developers and System Administrators',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Operating System :: OS Independent',
            'Topic :: Documentation',
            'Topic :: Software Development :: Documentation',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Text Processing :: Markup :: HTML',
            'Topic :: Text Processing :: Markup :: LaTeX',
        ],
        'parallel_read_safe': True,
    }
