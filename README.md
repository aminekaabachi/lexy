# Lexy
![test](https://github.com/aminekaabachi/lexy/workflows/test/badge.svg?branch=main) 
[![codecov](https://codecov.io/gh/aminekaabachi/lexy/branch/main/graph/badge.svg)](https://codecov.io/gh/aminekaabachi/lexy) 
[![PyPI](https://img.shields.io/pypi/v/lexy?style=flat-square)](https://pypi.org/project/lexy/)
[![Downloads](https://img.shields.io/pypi/dm/lexy?style=flat-square)](https://pypi.org/project/lexy/)
[![Docs](https://readthedocs.org/projects/lexy/badge/?version=latest&style=flat-square)](https://lexy.readthedocs.io/en/latest/)
[![GitHub](https://img.shields.io/github/license/aminekaabachi/lexy?style=flat-square)](https://github.com/aminekaabachi/lexy/blob/main/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

📙 ***Lexy** enables you to easily build and share data dictionaries to explain and document your data terminology using code.* The name "Lexy" is inspired from [lexicographer (/ˌlɛksɪˈkɒɡrəfə/)](https://www.lexico.com/definition/lexicographer), the person who compiles dictionaries.


-----------------

Easily document your data objects and generate beautiful data dictionaries:
```python
import lexy as xy
glossary = xy.Glossary()

#Defining glossary terms
glossary("name", "name of the student")
glossary("lastname", "lastname of the student")
glossary("age", "age of the student", sensitivity="private")

#Using the glossary to define pandas dataframe
import pandas as pd
data = [['tom', 'bird', 10], ['nick', 'star', 15], ['juli', 'aston', 14]] 
df = pd.DataFrame(data, columns = [glossary('name'), glossary('lastname'), glossary('age')]) 

xy.display_docs(glossary)
```

![Displayed docs](demo.png?raw=true "lexy Documentation")


## Beloved Features

**Lexy** will be soon ready for your use-case:

- ✔ Clear standard way to define data dictionaries using code.
- ✔ Tracking of glossary usage throughout the code.
- ✔ Display / Generate of documentation pages for your data glossaries.
- ✔ Detection of similarity between the terms and warning about possible data dictionary issues.
- Validation of data dictionaries using defined templates and rules.
- ✔ Import / export data dictionary from different formats (csv, excel, etc)
- AI Suggesting of metadata based on name and definition (personal data, data types, ...)
- Support for multiple backends (Memory, File, Redis, CloudFile...)
- Integration with Apache Atlas and Azure Purview.
- Publish data dictionary to lexyHub using the cli.
