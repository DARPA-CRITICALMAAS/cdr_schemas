from dataclasses import dataclass
from pathlib import Path
from types import ModuleType

from jinja2 import Template
from jinja2.filters import FILTERS
from pydantic_mermaid import MermaidGenerator

import cdr_schemas.area_extraction
import cdr_schemas.document
import cdr_schemas.events
import cdr_schemas.feature_results
import cdr_schemas.features.line_features
import cdr_schemas.features.point_features
import cdr_schemas.features.polygon_features
import cdr_schemas.georeference
import cdr_schemas.map
import cdr_schemas.map_results
import cdr_schemas.metadata
import cdr_schemas.mineral
import cdr_schemas.prospectivity_input
import cdr_schemas.prospectivity_models


@dataclass
class Diagram:
    title: str
    body: str


@dataclass
class Module:
    title: str
    ref: ModuleType


def replaces_block(text: str, block: str):
    comment = "<!-- this sections is autogenerated -->"
    begin_mark = "<!--#+BEGIN_SCHEMA-->"
    end_mark = "<!--#+END_SCHEMA-->"

    begin_idx = text.index(begin_mark)
    end_idx = text.index(end_mark)

    assert end_idx > begin_idx

    prefix = text[:begin_idx]
    suffix = text[end_idx + len(end_mark) :]

    return f"{prefix}{begin_mark}\n{comment}\n{block}\n{end_mark}{suffix}"


def mk_quote(s: str) -> str:
    return s.replace(" ", "-")


def run():
    diagrams = []
    FILTERS["mk_quote"] = mk_quote
    template = Template(Path("docs/schemas.md.j2").read_text())
    modules = [
        Module(title="area extraction", ref=cdr_schemas.area_extraction),
        Module(title="georeference", ref=cdr_schemas.georeference),
        Module(title="metadata", ref=cdr_schemas.metadata),
        Module(title="feature results", ref=cdr_schemas.feature_results),
        Module(title="point feature", ref=cdr_schemas.features.point_features),
        Module(title="line feature", ref=cdr_schemas.features.line_features),
        Module(title="polygon feature", ref=cdr_schemas.features.polygon_features),
        Module(title="cog metadata", ref=cdr_schemas.metadata),
        Module(title="document", ref=cdr_schemas.document),
        Module(title="mineral", ref=cdr_schemas.mineral),
        Module(title="map results", ref=cdr_schemas.map_results),
        Module(title="map", ref=cdr_schemas.map),
        Module(title="prospectivity input", ref=cdr_schemas.prospectivity_input),
        Module(title="prospectivity models", ref=cdr_schemas.prospectivity_models),
    ]

    for m in modules:
        generator = MermaidGenerator(m.ref)
        diagrams.append(Diagram(title=m.title, body=generator.generate_chart()))

    md = template.render(diagrams=diagrams)
    readme = Path("README.md").read_text()
    Path("README.md").write_text(replaces_block(readme, md))

    print("Schema diagrams updated!")


if __name__ == "__main__":
    run()
