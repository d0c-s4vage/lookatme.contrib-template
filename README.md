# `lookatme` contrib template

[lookatme](https://github.com/d0c-s4vage/lookatme) is a terminal-based, markdown
presentation tool that supports community contributed extensions.

Contributed extensions are namespaced python packages that override functionality
in a default `lookatme`.

## Template

This template is a [cookiecutter](https://github.com/cookiecutter/cookiecutter)
project template. After installing cookiecutter (`pip install cookiecutter`),
create a new lookatme contrib project from this template like so:

```bash
$> cookiecutter https://github.com/d0c-s4vage/lookatme.contrib-template.git
extension_name: new_ext
project_name: lookatme.contrib.new_ext
```

Following which you will have a new directory named `lookatme.contrib.new_ext`
in your current working directory.
