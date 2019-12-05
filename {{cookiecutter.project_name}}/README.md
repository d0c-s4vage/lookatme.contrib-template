# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Installation

If this project has been pushed up to pypi:

```bash
pip install {{cookiecutter.project_name}}
```

otherwise:

```bash
pip install ./path/to/{{cookiecutter.project_name}}
```

## Usage

Add the {{cookiecutter.extension_name}} into the extensions array in the
slide YAML header:

```markdown
---
title: A title
author: Me
date: 2019-12-04
extensions:
  - {{cookiecutter.extension_name}}
---
```

With the extension installed and declared in the YAML header, use it in your
markdown like so:

~~~markdown
```{{cookiecutter.extension_name}}

```
~~~
