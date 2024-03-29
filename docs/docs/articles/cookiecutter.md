!!! warning
    Page in progress. There may be typos and the content is subject to change.

# How to Generate a Python Package in 5m

<a href="../../probability/Integral/#1.1"><b>Link to lemma</b></a>

## Intorduction
Creating a new Python package involves setting up a project structure,
creating boilerplate code, and configuring various files. This process can 
be repetitive and time-consuming, especially when you want to follow best 
practices and maintain consistency across multiple projects. This is where 
templating tools like 
[Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/index.html)
or [Jinja](https://jinja.palletsprojects.com/en/3.1.x/)
come in as valuable tools.

In this tutorial, we will explore the practical application of Cookiecutter to
facilitate the creation of a customized template for a Python package.
This hands-on tutorial will guide you through the step-by-step process of
setting up a Cookiecutter template.

## Install Cookiecutter
Cookiecutter is a python package so you need to have python installed in 
your machine then you can install it with ``pip``:
```shell
pip install cookiecutter
```
## Usage
Basically a Cookiecutter template project is a diretory containing
a sub-directory that will be copied when generating a project from it.
The way it works is that iside this subdirectory (in file of directory names 
and within files) you can use "variables" that will be replaced by Cookiecutter.

```shell
mkdir PythonProjectGenerator
cd PythonProjectGenerator
mkdir {{cookiecutter.project_name}}
```


