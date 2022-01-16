from typing import List, Dict
import os
import lexy as g
import json
import pprint

# Build Html Components
# Table Header


def _buildTableHeader(headers: List[str]) -> str:
    trTag = "<tr role=\"row\">%s</tr>"
    thTag = "<th class=\"th-sm sorting_asc\" tabindex=\"0\" aria-controls=\"dtBasicExample\" rowspan=\"1\" colspan=\"1\" aria-sort=\"ascending\" aria-label=\"%s : activate to sort column descending\" style=\"width: %spx;\">%s</th>"
    headerTagsArr = [thTag % (hte[0], hte[1], hte[2]) for hte in headers]
    headerTags = "".join(headerTagsArr)
    return trTag % (headerTags)


# Table Data
def _buildTableData(value: str) -> str:
    tdTag = "<td>%s</td>"
    return tdTag % (value)

# Table Row


def _buildTableRow(rowValuesArr: List[str]) -> str:
    trTag = "<tr role=\"row\" class=\"even\">%s</tr>"
    tdTags = [_buildTableData(value) for value in rowValuesArr]
    rowValues = "".join(tdTags)
    return trTag % (rowValues)

# Table Body


def _buildTable(tableHeaderTag: str, tableBodyTags: List[str]) -> str:
    tableTag = "<table id=\"dtBasicExample\" class=\"table table-striped table-bordered table-sm dataTable\" cellspacing=\"0\" role=\"grid\" aria-describedby=\"dtBasicExample_info\" width=\"100%%\" style=\"width: 100%%;\"> <thead>%s</thead> <tbody>%s</tbody> </table>"
    tableBodyElements = "".join(tableBodyTags)
    return tableTag % (tableHeaderTag, tableBodyElements)

# Anchor


def _buildAnchor(name: str, href: str) -> str:
    anchorTag = "<a href=\"%s\" target=\"_blank\" style>%s</a>"
    return anchorTag % (href, name)

# Build Table Row Tag for HTML Display


def _buildTableRowTag(name: str, definition: str, usage_count, traces, metadata: Dict) -> str:
    termDataAsList = [_buildAnchor(name, "#"), definition, usage_count, traces, metadata]
    tableRowTag = _buildTableRow(termDataAsList)
    return tableRowTag


def _getHeaderColumns() -> List[str]:
    headers = [
        ["name", 85, "Name"],
        ["definition", 85, "Definition"],
        ["usage_count", 85, "Usage Count"],
        ["traces", 255, "Traces"],
        ["metadata", 255, "Metadata"],
    ]
    return headers


def _pretty(d):
    htmlLines = []
    for textLine in pprint.pformat(d).splitlines():
        htmlLines.append('%s<br/>' % textLine)
    htmlText = '\n'.join(htmlLines)
    return htmlText


def _generate_docs(glossary: g.Glossary):
    L = []
    for t in glossary.terms:
        name = glossary.terms.get(t).name
        definition = glossary.terms.get(t).definition
        usage_count = len(glossary.terms.get(t).traces)
        traces = glossary.terms.get(t).traces
        metadata = _pretty(glossary.terms.get(t).metadata)
        L.append(_buildTableRowTag(name, definition, usage_count, traces, metadata))

    glossaryTable = _buildTable(_buildTableHeader(_getHeaderColumns()), L)
    htmlPlainTag = "<!DOCTYPE html> <html lang=\"en\"> <head> <title>lexy Documentation</title> <meta charset=\"utf-8\"> <link rel=\"stylesheet\" href=\"https://use.fontawesome.com/releases/v5.8.2/css/all.css\"> <link rel=\"stylesheet\" href=\"https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap\"> <link href=\"https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.4.1/css/bootstrap.min.css\" rel=\"stylesheet\"> <link href=\"https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.18.0/css/mdb.min.css\" rel=\"stylesheet\"> <link rel=\"stylesheet\" type=\"text/css\" href=\"https://cdn.datatables.net/1.10.21/css/jquery.dataTables.css\"> <script type=\"text/javascript\" src=\"https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js\"></script> <script type=\"text/javascript\" src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.4/umd/popper.min.js\"></script> <script type=\"text/javascript\" src=\"https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.4.1/js/bootstrap.min.js\"></script> <script type=\"text/javascript\" src=\"https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.18.0/js/mdb.min.js\"></script> <script type=\"text/javascript\" charset=\"utf8\" src=\"https://cdn.datatables.net/1.10.21/js/jquery.dataTables.js\"></script> <style>table.dataTable thead .sorting:after, table.dataTable thead .sorting:before, table.dataTable thead .sorting_asc:after, table.dataTable thead .sorting_asc:before, table.dataTable thead .sorting_asc_disabled:after, table.dataTable thead .sorting_asc_disabled:before, table.dataTable thead .sorting_desc:after, table.dataTable thead .sorting_desc:before, table.dataTable thead .sorting_desc_disabled:after, table.dataTable thead .sorting_desc_disabled:before{bottom: .5em;} table a{margin: 0; color: #007bff !important;}</style> <script>$(document).ready(function (){$('#dtBasicExample').DataTable(); $('.dataTables_length').addClass('bs-select');}); </script> </head> <body> <div class=\"container\" style=\"padding: 1em;\"> <h2>✨ %s</h2> <div class=\"row\"> <div class=\"col-sm-12\">%s</div></div></div></div></body> </html>"
    htmlFormattedTag = htmlPlainTag % ("Glossary", glossaryTable)
    return htmlFormattedTag


def display_docs(glossary: g.Glossary):
    from IPython.display import display, HTML
    display(HTML(_generate_docs(glossary)))


def docs(glossary: g.Glossary):
    return(_generate_docs(glossary))


def export_docs(glossary: g.Glossary, filepath: str):
    f = open(filepath, "w")
    f.write(_generate_docs(glossary))
    f.close()
