from typing import List, Dict
import lexy as xy

htmlTemplate = """
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Lexy Documentation</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.2/css/all.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap">
    <link rel="stylesheet" type="text/css"
        href="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.3.1/semantic.min.css">
    <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.3.1/components/table.min.css">
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.11.3/css/dataTables.semanticui.min.css">
    <style>
        table.glossary thead .sorting:after,
        table.glossary thead .sorting:before,
        table.glossary thead .sorting_asc:after,
        table.glossary thead .sorting_asc:before,
        table.glossary thead .sorting_asc_disabled:after,
        table.glossary thead .sorting_asc_disabled:before,
        table.glossary thead .sorting_desc:after,
        table.glossary thead .sorting_desc:before,
        table.glossary thead .sorting_desc_disabled:after,
        table.glossary thead .sorting_desc_disabled:before {
            bottom: .5em;
        }

        table a {
            margin: 0;
            color: #007bff !important;
        }

        table, th, td {
            border: 0.5px solid #ccc !important;
            text-align: center !important;
        }

        a.label {
            margin:1px !important;
        }
    </style>
</head>

<body>
    <div class="ui" style="padding: 1em;">
        <div
            style="padding-top: 1em; padding-bottom:0.5em; margin-bottom: 1em; border-bottom: 2px solid #F1F1F1;">
            <h2>📙 %s</h2>
        </div>
        <div>
            %s
        </div>
    </div>
    </div>

    <script type="text/javascript" src="https://code.jquery.com/jquery-3.5.1.js"></script>
    <script type="text/javascript"
        src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.4/umd/popper.min.js"></script>
    <script type="text/javascript" charset="utf8"
        src="https://cdn.datatables.net/1.11.3/js/jquery.dataTables.min.js"></script>
    <script type="text/javascript" charset="utf8"
        src="https://cdn.datatables.net/1.11.3/js/dataTables.semanticui.min.js"></script>
    <script type="text/javascript" charset="utf8"
        src="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.3.1/semantic.min.js"></script>
    <script>$(document).ready(function () { $('#glossary').DataTable(); }); </script>
</body>

</html>
"""

# Build Html Components
# Table Header


def _buildTableHeader(headers: List[str]) -> str:
    trTag = "<tr role=\"row\">%s</tr>"
    thTag = "<th class=\"th-sm \" tabindex=\"0\" aria-controls=\"glossy\" rowspan=\"1\" colspan=\"1\" aria-sort=\"ascending\" aria-label=\"%s : activate to sort column descending\" style=\"width: %spx;\">%s</th>"
    headerTagsArr = [thTag % (hte[0], hte[1], hte[2]) for hte in headers]
    headerTags = "".join(headerTagsArr)
    return trTag % (headerTags)


# Table Data
def _buildTableData(value: str) -> str:
    tdTag = "<td>%s</td>"
    return tdTag % (value)

# Table Row


def _buildTableRow(rowValuesArr: List[str]) -> str:
    trTag = "<tr role=\"row\" id='%s' class=\"even\">%s</tr>"
    tdTags = [_buildTableData(value) for value in rowValuesArr]
    rowValues = "".join(tdTags)
    return trTag % (rowValuesArr[0], rowValues)

# Table Body


def _buildTable(tableHeaderTag: str, tableBodyTags: List[str]) -> str:
    tableTag = "<table id=\"glossary\" class=\"ui compact striped table\" cellspacing=\"0\" role=\"grid\" width=\"100%%\" style=\"width: 100%%;\"> <thead>%s</thead> <tbody>%s</tbody> </table>"
    tableBodyElements = "".join(tableBodyTags)
    return tableTag % (tableHeaderTag, tableBodyElements)

# Anchor


def _buildAnchor(name: str, href: str) -> str:
    anchorTag = "<a href=\"%s\" target=\"_blank\" style>%s</a>"
    return anchorTag % (href, name)

# Build Table Row Tag for HTML Display


def _buildTableRowTag(name: str, definition: str, usage_count, traces, metadata: Dict) -> str:
    termDataAsList = [_buildAnchor(
        name, f"#{name}"), definition, usage_count, traces, metadata]
    tableRowTag = _buildTableRow(termDataAsList)
    return tableRowTag


def _getHeaderColumns() -> List[str]:
    headers = [
        ["name", 85, "Name"],
        ["definition", 255, "Definition"],
        ["usage_count", 85, "Usage Count"],
        ["traces", 255, "Traces"],
        ["metadata", 100, "Metadata"],
    ]
    return headers



def _generate_docs(glossary: xy.Glossary):
    L = []
    for t in glossary.terms:
        name = glossary.terms.get(t).name
        definition = glossary.terms.get(t).definition
        usage_count = f"<a class='ui small grey label'>{len(glossary.terms.get(t).traces)}</a>"
        traces = "&nbsp;&nbsp;".join([f"<span class='ui compact small message'><b>{trace.code_context[0]}</b> <span class='detail'>[{trace.filename}] (lineno={trace.lineno})</span></span>" for trace in glossary.terms.get(t).traces])
        metadata = "&nbsp;&nbsp;".join([f"<a class='ui small teal label'>{meta[0]} <span class='detail'>{meta[1]}</span></a>" for meta in glossary.terms.get(t).metadata.items()])
        L.append(_buildTableRowTag(name, definition,
                 usage_count, traces, metadata))

    glossaryTable = _buildTable(_buildTableHeader(_getHeaderColumns()), L)
    htmlPlainTag = "<!DOCTYPE html> <html lang=\"en\"> <head> <title>lexy Documentation</title> <meta charset=\"utf-8\"> <link rel=\"stylesheet\" href=\"https://use.fontawesome.com/releases/v5.8.2/css/all.css\"> <link rel=\"stylesheet\" href=\"https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap\"> <link href=\"https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.4.1/css/bootstrap.min.css\" rel=\"stylesheet\"> <link href=\"https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.18.0/css/mdb.min.css\" rel=\"stylesheet\"> <link rel=\"stylesheet\" type=\"text/css\" href=\"https://cdn.datatables.net/1.10.21/css/jquery.dataTables.css\"> <script type=\"text/javascript\" src=\"https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js\"></script> <script type=\"text/javascript\" src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.4/umd/popper.min.js\"></script> <script type=\"text/javascript\" src=\"https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.4.1/js/bootstrap.min.js\"></script> <script type=\"text/javascript\" src=\"https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.18.0/js/mdb.min.js\"></script> <script type=\"text/javascript\" charset=\"utf8\" src=\"https://cdn.datatables.net/1.10.21/js/jquery.dataTables.js\"></script> <style>table.dataTable thead .sorting:after, table.dataTable thead .sorting:before, table.dataTable thead .sorting_asc:after, table.dataTable thead .sorting_asc:before, table.dataTable thead .sorting_asc_disabled:after, table.dataTable thead .sorting_asc_disabled:before, table.dataTable thead .sorting_desc:after, table.dataTable thead .sorting_desc:before, table.dataTable thead .sorting_desc_disabled:after, table.dataTable thead .sorting_desc_disabled:before{bottom: .5em;} table a{margin: 0; color: #007bff !important;}</style> <script>$(document).ready(function (){$('#dtBasicExample').DataTable(); $('.dataTables_length').addClass('bs-select');}); </script> </head> <body> <div class=\"container\" style=\"padding: 1em;\"> <h2>✨ %s</h2> <div class=\"row\"> <div class=\"col-sm-12\">%s</div></div></div></div></body> </html>"
    htmlFormattedTag = htmlTemplate % ("Glossary", glossaryTable)
    return htmlFormattedTag


def display_docs(glossary: xy.Glossary):
    from IPython.display import display, HTML
    display(HTML(_generate_docs(glossary)))


def docs(glossary: xy.Glossary):
    return(_generate_docs(glossary))


def export_docs(glossary: xy.Glossary, filepath: str):
    f = open(filepath, "w")
    f.write(_generate_docs(glossary))
    f.close()
