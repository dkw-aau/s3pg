# S3PG - Reproducibility Instructions
Standardized SHACL Shapes-based PG transformation (S3PG)

**Paper Title:** Lossless Transformations of Knowledge Graphs to Property Graphs using Standardized Schemas

**Status:** Under Review

## 1.  Getting the code

Codebase to transform RDF graph data models to Property Graph (PG) data models is available at [https://github.com/dkw-aau/KG2PG/](https://github.com/dkw-aau/KG2PG/).

Start by cloning the code using the following command:

```bash
git clone https://github.com/dkw-aau/KG2PG.git
```

## 2. Getting the data

Before using the S3PG transformation algorithm, ensure you have the necessary prerequisites in place.

### 2.1. RDF Datasets

To begin, download the required datasets, i.e., DBpedia and Bio2RDF Clinical Trials Dataset

#### 1. DBpedia

We downloaded two versions of DBpedia. 
The first version is from 2020 and the second version is from 2022. 
The folder [dbpedia](https://github.com/dkw-aau/s3pg/tree/main/dbpedia) contains the files and scripts used to download each of the dataset. 

You can download the datasets we used in experiments from [this](https://bitbucket.org/kashifrabbani/s3pg/src/master/Datasets/) link.

#### 2. Bio2RDF Clinical Trials Dataset
We downloaded this dataset from the official link: https://download.bio2rdf.org/#/current/clinicaltrials/

You can download the datasets we used in experiments from [this](https://bitbucket.org/kashifrabbani/s3pg/src/master/Datasets/) link.


### 2.2. SHACL shapes

Utilize QSE (Quality Shapes Extractor) to extract SHACL shapes from your datasets. 
[QSE](https://github.com/dkw-aau/qse) GitHub repository contains the codebase and instructions to extract SHACL shapes from a given dataset.

You can download the SHACL shapes used for the datasets used in our experiments from this link: [S3PG-SHACL-SHAPES](https://bitbucket.org/kashifrabbani/s3pg/src/master/)


## 3. Transforming KGs to PGs using S3PG

Once you have downloaded the datasets (RDF knowledge graphs) and SHACL shapes for them, next step is to use S3PG transformation algorithm to transform them into property graphs.

We used Docker and shell scripts to build and run the code on different datasets. We allow users to specify the configuration parameters in the config files depending on the dataset and user's requirement.


#### 3.1. Requirements
The experiments run on a _single machine_. To reproduce the experiments the software used are *a GNU/Linux distribution (with git, bash, make, and wget)*, Docker,  and Java  *version 15.0.2.fx-zulu*
having a machine with 256 GB (minimum required 16GB) and CPU with 16 cores (minimum required 1 core).

We have prepared shell scripts and configuration files for each dataset to make the process of running experiments as much easy as possible.


#### 3.2. Configuration Parameters
Please update the configuration file for each dataset available in the [config](https://github.com/dkw-aau/KG2PG/tree/master/config) directory, i.e., `dbpedia2020`, `dbpedia2022`, and `bio2rdf` to set the correct paths for your machine.

#### 3.3. Shell Scripts
Assuming that you are in the project's directory, you have updated the configuration file(s), and docker is installed on your machine, move into [scripts](https://github.com/dkw-aau/KG2PG/tree/master/scripts) directory using the command ``` cd scripts ``` and then execute one of the following shell scripts files:
``` ./run_bio2rdf.sh ``` ,
``` ./run_dbp2020.sh ``` ,
``` ./run_dbp2022.sh ``` 


You will see logs and the output will be stored in the path of the output directory specified in the config file.

*Note: You may have to execute ```chmod +rwx ``` for each script to solve the permissions issue. In case you want to run the experiments without script, please follow the instructions on [TODO](https://github.com/dkw-aau/KG2PG/blob/master/README_without_script.md) page.*


### 5. S3PG Output

S3PG will output PG in CSV and JSON format.

TODO: Add more details

## Step 4. Loading transformed Graphs into Neo4j
Use neo4j admin import to load the files into Neo4j. 

TODO: Add more details

## Step 5. Running Queries 

Queries are available in the [resources](https://github.com/dkw-aau/KG2PG/tree/master/src/main/resources) directory.


