"""
{{cookiecutter.description}}
"""


import urwid


from lookatme.exceptions import IgnoredByContrib


def render_code(token, body, stack, loop):
    lang = token["lang"] or ""
    if lang != "{{cookiecutter.extension_name}}":
        raise IgnoredByContrib()
    
    return urwid.Text("Yay! The {{cookiecutter.extension_name}} extension works!")
