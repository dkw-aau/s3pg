import os
import csv
from rdflib import Graph, Namespace, RDF

# Create an RDF graph
g = Graph()

# Load your RDF data from a file
rdf_file = "Bio2rdf_QSE_FULL_SHACL.ttl"  # Replace with your file path
g.parse(rdf_file, format="turtle")

# Define relevant namespaces
SHACL = Namespace("http://www.w3.org/ns/shacl#")


def compute_shape_statistics(graph):
    property_shapes_without_or = 0
    property_shapes_with_or = 0
    property_shapes_with_or_datatype = 0
    property_shapes_with_or_class = 0
    property_shapes_with_or_both = 0
    property_shapes_with_datatype_only = 0
    property_shapes_with_class_only = 0
    node_shape_count = 0
    property_shape_count = 0

    for shape in g.subjects(RDF.type, SHACL.NodeShape):
        node_shape_count += 1

    for shape in g.subjects(RDF.type, SHACL.PropertyShape):
        property_shape_count += 1
        or_items = list(g.objects(shape, SHACL["or"]))

        if not or_items:
            property_shapes_without_or += 1
            has_datatype = g.value(shape, SHACL["datatype"])
            has_class = g.value(shape, SHACL["class"])

            if has_datatype and not has_class:
                property_shapes_with_datatype_only += 1
            elif has_class and not has_datatype:
                property_shapes_with_class_only += 1
        else:
            property_shapes_with_or += 1
            has_datatype = False
            has_class = False

            for or_item in or_items:
                for list_item in g.items(or_item):
                    if g.value(list_item, SHACL["datatype"]):
                        has_datatype = True
                    if g.value(list_item, SHACL["class"]):
                        has_class = True

            if has_datatype and not has_class:
                property_shapes_with_or_datatype += 1
            elif has_class and not has_datatype:
                property_shapes_with_or_class += 1
            elif has_datatype and has_class:
                property_shapes_with_or_both += 1

    return {
        "Count_NS": node_shape_count,
        "Count_PS": property_shape_count,
        "COUNT_PS_wd_or": property_shapes_without_or,
        "COUNT_PS_wo_or": property_shapes_with_or,
        "COUNT_PS_wd_or_literal": property_shapes_with_or_datatype,
        "COUNT_PS_wd_or_nonLiteral": property_shapes_with_or_class,
        "COUNT_PS_wd_or_literalAndNonLiteral": property_shapes_with_or_both,
        "COUNT_PS_wo_or_literal": property_shapes_with_datatype_only,
        "COUNT_PS_wo_or_nonLiteral": property_shapes_with_class_only,
    }


# Function to print property shapes with or both
def print_property_shapes_with_or_both(graph):
    for shape in g.subjects(RDF.type, SHACL.PropertyShape):
        or_items = list(g.objects(shape, SHACL["or"]))

        if or_items:
            has_datatype = False
            has_class = False

            for or_item in or_items:
                for list_item in g.items(or_item):
                    if g.value(list_item, SHACL["datatype"]):
                        has_datatype = True
                    if g.value(list_item, SHACL["class"]):
                        has_class = True

            if has_datatype and has_class:
                print(f"Property Shape with or both: {shape}")


statistics = compute_shape_statistics(g)
# Extract the filename (without path) from rdf_file
filename = os.path.basename(rdf_file)

# Extract the filename (without path) from rdf_file
filename_wo_extension, file_extension = os.path.splitext(os.path.basename(rdf_file))

# Specify the output CSV file
output_csv_file = f"shape_statistics_{filename_wo_extension}.csv"

# Write the statistics to a CSV file
with open(output_csv_file, mode="w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["ShapeFile"] + list(statistics.keys()))
    writer.writeheader()
    writer.writerow({"ShapeFile": filename, **statistics})

print(f"Statistics have been written to {output_csv_file}")

# Call the function to print property shapes with or both
if statistics["COUNT_PS_wd_or_literalAndNonLiteral"] > 0:
    print_property_shapes_with_or_both(g)
