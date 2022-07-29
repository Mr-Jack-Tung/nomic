# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))


# -- Project information -----------------------------------------------------

project = 'nomic'
copyright = '2022, Nomic, Inc'
author = 'nomic'
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['myst_parser', 'sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'sphinx_copybutton']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'sphinx_rtd_theme'
html_theme = 'furo'
html_logo = "nomic.png"
html_title = "The Nomic Client"
html_favicon = 'favicon.ico'

html_theme_options = {
    "sidebar_hide_name": False,
}

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "black",
        "color-brand-content": "#000000",
        "color-admonition-background": "black",
    },
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/nomic-ai/nomic",
            "html": """
            <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
            </svg>
        """,
            "class": "",
        },
        {
            "name": "Wittgenstein",
            "url": "https://www.youtube.com/watch?v=628eVJgHD6I",
            "html": """
<svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 512 512" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M397.777 20.81c-28.326 32.545-45.686 49.052-79.73 75.385.98 3.462 1.904 6.923 2.767 10.373a838.71 838.71 0 0 1 71.06-15.156c2.614-5.158 4.803-10.06 6.483-14.78 6.053-17.005 6.845-32.884-.58-55.823zm-116.646 31c-1.6 24.42-1.437 48.997-.728 73.72 11.823 16.072 20.343 35.874 23.293 59.55l4.282-15.91c3.56-13.232-.114-44.212-8.596-72.72-4.965-16.69-11.733-32.465-18.25-44.64zm-66.286 45.913c15.833 30.734 31.377 68.437 40.18 102.69 10.035 2.098 18.686 5.78 25.404 11.75 6.176 5.49 10.61 12.84 13.822 21.54 34.542 1.322 74.627 6.23 108.107 15.88-22.727-29.94-53.25-48.74-106.12-45.626l-8.985.53-.53-8.985c-3.143-53.38-36.79-84.435-71.878-97.78zM473.7 100.15c-37.875 2.156-91.904 9.273-149.04 24.123 2.246 12.387 3.374 24.24 2.81 34.774 16.516-3.57 37.316-4.425 58.604-3.342L473.7 100.15zm-101.26 73.278c-22.01-.027-42.3 2.385-52.43 6.437l-14.727 5.895c20.458-.12 38.216 3.195 53.735 9.144l78.19-13.728c-.43-.118-.798-.257-1.235-.37-11.935-3.122-26.448-5.348-41.262-6.51-7.406-.58-14.934-.86-22.27-.868zm-143.16 42.63c-1.946-.01-3.948.027-5.98.09l21.667 7.813-2.512-7.122c-4.072-.48-8.482-.755-13.174-.78zm-45.462 4.99c-2.788.567-5.6 1.19-8.423 1.85a1857.95 1857.95 0 0 1 8.96 32.416 1531.66 1531.66 0 0 1 30.608 4.842 1158.087 1158.087 0 0 0-9.54-31.318l-21.605-7.79zm79.684 1.35l3.332 9.448 7.992 2.88c-1.982-4.052-4.154-7.152-6.355-9.11-1.28-1.138-2.964-2.216-4.968-3.218zM158 227.512a308.24 308.24 0 0 0-32.396 11.646c.903 3.08 1.786 6.137 2.673 9.2a1119.28 1119.28 0 0 1 36.713 4.238c-2.268-8.373-4.6-16.734-6.99-25.084zm68.695 8.994a1255.104 1255.104 0 0 1 7.967 27.064 2700.72 2700.72 0 0 1 25.96 4.784l-7.925-22.47-26.002-9.378zm47.87 17.262l6.53 18.51c.78.153 1.558.305 2.34.456a169.9 169.9 0 0 0-.873-9.322c-.306-2.477-.675-4.86-1.095-7.156l-6.903-2.488zM83.89 263.006l7.672 33.676c10.445.647 21.214 1.323 32.143 2.043a2472.975 2472.975 0 0 0-9.328-33.57 933.866 933.866 0 0 0-30.486-2.15zm49.73 4a2415.755 2415.755 0 0 1 9.058 33.014c11.506.832 23.24 1.76 35.2 2.853-2.54-10.49-5.16-20.966-7.876-31.424a1139.84 1139.84 0 0 0-36.383-4.444zm-65.83 6.36c-7.67 6.476-14.238 13.314-19.31 20.42 7.942.605 16.05 1.166 24.35 1.706l-5.04-22.125zm121.505.882c2.593 10.15 5.108 20.31 7.54 30.482a1205.51 1205.51 0 0 1 31.16 3.66c-2.46-9.708-5.004-19.393-7.645-29.052a1628.07 1628.07 0 0 0-31.055-5.09zm50.664 8.58c2.515 9.41 4.94 18.833 7.29 28.264a961.73 961.73 0 0 1 30.21 5.012L267.55 288c-9.176-1.76-18.37-3.488-27.59-5.172zM53.243 312.193c3.25 9.827 6.13 19.728 8.744 29.674 7.282.42 14.533.89 21.737 1.45l-6.72-29.497a2728.25 2728.25 0 0 1-23.76-1.627zm42.492 2.815l6.823 29.95a1129.016 1129.016 0 0 1 33.993 3.73 2046.15 2046.15 0 0 0-7.975-31.56 6373.735 6373.735 0 0 0-32.842-2.12zm-59.806 2.197c-2.93 7.325-5.316 15.14-7.102 23.244 4.76.126 9.5.287 14.22.476-2.172-7.978-4.524-15.89-7.118-23.72zm111.584 1.256a2034.99 2034.99 0 0 1 8.173 32.794 1233.727 1233.727 0 0 1 34.48 5.43 2222.516 2222.516 0 0 0-7.89-35.295c-11.79-1.123-23.375-2.076-34.763-2.93zm53.672 4.864a2291.712 2291.712 0 0 1 8.117 36.778c10.88 2.027 21.74 4.172 32.593 6.453-2.996-13.145-6.04-26.27-9.22-39.354a1144.54 1144.54 0 0 0-31.49-3.876zm50.687 6.703c3.254 13.577 6.376 27.165 9.445 40.752 3.113.694 6.226 1.382 9.34 2.095a307.567 307.567 0 0 0 9.028-38.037 920.074 920.074 0 0 0-27.813-4.81zM25.898 358.375a166.825 166.825 0 0 0-.855 24.473c.05 1.287.122 2.57.203 3.85 9.547.376 19.1.758 28.643 1.17-1.907-9.643-3.956-19.23-6.212-28.737-7.216-.324-14.473-.577-21.78-.755zm40.596 1.787c2.19 9.497 4.168 19.022 6.018 28.555 7.288.354 14.56.747 21.822 1.17l-6.416-28.164a1071.11 1071.11 0 0 0-21.424-1.56zm40.28 3.293l6.29 27.62c11.363.785 22.678 1.68 33.91 2.76a1853.432 1853.432 0 0 0-5.954-26.425 1122.774 1122.774 0 0 0-34.247-3.955zm53.33 6.63a1859.694 1859.694 0 0 1 5.705 25.735 804.905 804.905 0 0 1 33.344 4.534c-1.62-8.244-3.28-16.48-4.982-24.708a1240.398 1240.398 0 0 0-34.067-5.562zm53.162 9.07a2610.58 2610.58 0 0 1 4.857 24.468c11.395 2.14 22.647 4.582 33.73 7.375-1.852-8.374-3.716-16.74-5.585-25.102a1473.226 1473.226 0 0 0-33.002-6.742zm-185.79 25.663c1.864 10.084 4.742 19.708 8.626 28.49 8.62.448 17.394.87 26.203 1.3-1.617-9.538-3.257-19.055-4.98-28.536-9.926-.444-19.88-.855-29.85-1.254zm48.434 2.14c1.708 9.546 3.32 19.07 4.918 28.58 8.123.43 16.218.903 24.233 1.44l-6.546-28.748c-7.51-.46-15.04-.887-22.604-1.27zm41.35 2.526l6.584 28.903c11.37.965 22.41 2.09 32.94 3.543-1.88-9.922-3.846-19.755-5.872-29.547-11.112-1.128-22.344-2.07-33.652-2.9zm52.45 4.993a1806.56 1806.56 0 0 1 5.966 30.564c12.337 2.424 23.668 5.542 33.62 9.696a2964.462 2964.462 0 0 0-6.5-35.498 755.42 755.42 0 0 0-33.087-4.76zm52.046 8.226c1.803 9.652 3.57 19.308 5.277 28.973 6.903-6.364 13.305-14.36 19.13-23.547-8.02-1.995-16.168-3.786-24.407-5.427zM46.816 451.89c3.138 4.21 6.606 8.045 10.405 11.42 3.476 3.09 7.304 5.85 11.415 8.307a2876.172 2876.172 0 0 1-3.248-18.828c-6.2-.304-12.4-.598-18.57-.9zm37.086 1.846a2058.225 2058.225 0 0 0 4.682 26.735c8.652 2.747 17.958 4.51 27.598 5.317l-6.946-30.482a1503.798 1503.798 0 0 0-25.334-1.57zm44.15 3.118l6.68 29.326c2.053-.08 4.11-.2 6.172-.362a166.66 166.66 0 0 0 23.047-3.464 1840.907 1840.907 0 0 0-3.677-21.442c-10.095-1.65-20.94-2.984-32.222-4.058zm51.143 7.74c.746 4.277 1.48 8.572 2.2 12.886 6.1-2.068 11.996-4.47 17.59-7.18-5.887-2.132-12.53-4.03-19.79-5.706z"></path></svg>
""",
            "class": "",
        },

    ],
    "source_repository": "https://github.com/nomic-ai/nomic/",
    "source_branch": "main",
    "source_directory": "docs/source",

}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']