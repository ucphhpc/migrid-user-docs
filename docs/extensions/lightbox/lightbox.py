# This file is part of the MiGrid Sphinx Extension for Sphinx documentation.
#
# Lightbox extension is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Lightbox extension is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with MiGrid Sphinx Extension.  If not, see <https://www.gnu.org/licenses/>.

import os
from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.util import logging
from sphinx.util.fileutil import copy_asset_file
from sphinx.util import relative_uri

logger = logging.getLogger(__name__)

class Lightbox(Directive):
    """
    Lightbox directive for Sphinx.

    This directive creates a lightbox element that displays an image in a larger view when clicked.

    Arguments:
        image path (str): The path to the image file.

    Options:
        alt (str): The alt text for the image.
        caption (str): The caption for the image.
        percentage (list): A list of two integers representing the thumbnail width and lightbox width as percentages.

    Example usage:
        .. lightbox:: path/to/image.jpg
           :alt: Alternative text for the image
           :caption: A caption for the image
           :percentage: 50 80 95
           :class: border-box
    """

    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        'alt': directives.unchanged,
        'caption': directives.unchanged,
        'percentage': directives.positive_int_list,
        'class': directives.unchanged,
    }


    def run(self):
        """
        Create a lightbox element.

        Returns:
            list: A list of nodes representing the lightbox element.
        """
        env = self.state.document.settings.env
        image_path = self.arguments[0]
        alt_text = self.options.get('alt', '')
        caption = self.options.get('caption', '')
        percentages = self.options.get('percentage', [])
        custom_class = self.options.get('class', '')

        # Set default values for thumbnail_width, lightbox_width, and height_style. Can be overridden by percentage option.
        # Initial value uses full width, or with of the image.
        thumbnail_width = '100%'
        # Initial value uses 95 % of width, specifically to allow for Close image icon.
        # Initial value uses 95 % of height, specifically to allow for caption text.

        # Inside the run() method
        if percentages:
            thumbnail_width = f'{percentages[0]}%'
            if len(percentages) > 1:
                scale_percentage = percentages[1]
                # Use min() function in CSS to automatically choose the constraining dimension
                size_style = f"""
                    width: min({scale_percentage}vw, calc({scale_percentage}vh * var(--aspect-ratio)));
                    height: min({scale_percentage}vh, calc({scale_percentage}vw / var(--aspect-ratio)));
                """

        # Generate a unique ID for the checkbox
        checkbox_id = f"lightbox-{env.new_serialno('lightbox')}"

        # Construct the full source path
        src_image_path = os.path.join(env.srcdir, image_path)

        # Copy the image to _static directory while preserving subdirectories
        static_dir = '_static'
        rel_path = os.path.relpath(image_path)
        new_image_path = os.path.join(static_dir, rel_path)

        # Create subdirectories if they don't exist
        os.makedirs(os.path.dirname(os.path.join(env.app.outdir, new_image_path)), exist_ok=True)

        try:
            copy_asset_file(src_image_path, os.path.join(env.app.outdir, new_image_path))
        except Exception as e:
            logger.warning(f"Failed to copy image file: {src_image_path}. Error: {str(e)}")
            new_image_path = image_path

        # Generate the correct relative path
        current_page_path = env.docname
        image_url = relative_uri(current_page_path, new_image_path)
        # Use image_url in your HTML generation
        html = f"""
        <label for="{checkbox_id}">
            <img src="{image_url}" alt="{alt_text}" class="lightbox-trigger {custom_class}" 
                style="width: {thumbnail_width};">
        </label>
        <input type="checkbox" id="{checkbox_id}" class="lightbox-toggle">
        <div class="lightbox">
            <label for="{checkbox_id}">
                <div class="lightbox-content" style="display: flex; flex-direction: column; align-items: center; justify-content: center;">
                    <div class="image-container" style="text-align: center;">
                        <img src="{image_url}" alt="{alt_text}" class="{custom_class}" style="{size_style}"
                            onload="this.style.setProperty('--aspect-ratio', this.naturalWidth / this.naturalHeight);">
                        <div class="caption-overlay" style="text-align: center;">{caption}</div>
                        <label for="{checkbox_id}" class="close-btn-overlay">×</label>
                    </div>
                    <p class="caption-below" style="text-align: center;">{caption}</p>
                    <label for="{checkbox_id}" class="close-btn-side">×</label>
                </div>
            </label>
        </div>
        """
        return [nodes.raw('', html, format='html')]

def setup(app):
    """
    Set up the Sphinx extension.

    Args:
        app (Sphinx): The Sphinx application object.

    Returns:
        dict: A dictionary containing extension metadata.
    """
    app.add_directive('lightbox', Lightbox)
    app.add_css_file('lightbox.css')

    return {
        'version': '0.1',
        'license': 'GPL-3.0-or-later',
        'author': 'Aputsiak Niels Janussen',
        'description': 'MiGrid extension Lightbox for Sphinx documentation',
        'long_description': 'Accessibility focused lightbox extension for Sphinx used in MiGrid User Docs',
        'url': 'https://github.com/aputtu/migrid-sphinx-ext',
        'classifiers': [
            'Development Status :: 3 - Alpha',
            'Framework :: Sphinx',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Operating System :: OS Independent',
            'Topic :: Documentation',
            'Topic :: Software Development :: Documentation',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Text Processing :: Markup :: HTML',
            'Topic :: Text Processing :: Markup :: LaTeX',
        ],
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
