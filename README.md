# S3PG
Standardized SHACL Shapes-based PG transformation (S3PG)

**Paper Title:** Lossless Transformations of Knowledge Graphs to Property Graphs using Standardized Schemas

**Status:** Under Review

## Code -- Open Source

Codebase to transform RDF graph data models to Property Graph (PG) data models is available at [https://github.com/dkw-aau/KG2PG/](https://github.com/dkw-aau/KG2PG/).

### Clone the code:

Start by cloning the code using the following command:

```bash
git clone https://github.com/dkw-aau/KG2PG.git
```

## Pre-requisite

Before using the transformation algorithm, ensure you have the necessary prerequisites in place.

### Step 1: Download Datasets

To begin, download the required datasets for your transformation.

#### 1. DBpedia

We downloaded two versions of DBpedia. The first version is from 2020 and the second version is from 2022. This folder ??? contains the files and scripts used to download each of the dataset. 


#### 2. Bio2RDF Clinical Trials Dataset
We downloaded this dataset from the official link: https://download.bio2rdf.org/#/current/clinicaltrials/





### Step 2: Extract SHACL shapes using QSE

Utilize QSE (Quality Shapes Extractor) to extract SHACL shapes from your datasets. 
Here is the link https://github.com/dkw-aau/qse 

## Run S3PG

### Option 1: Using Docker


If you prefer using Docker, follow these steps:


### Option 2: Using Jar (without Docker)

If you choose not to use Docker, follow these steps:

    1. Navigate to the cloned repository:

    cd KG2PG

    2. Run the transformation algorithm:

