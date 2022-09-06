FROM jupyter/minimal-notebook:python-3.9.4

ADD packages.txt .

RUN pip install -r packages.txt

RUN mamba install graphviz

