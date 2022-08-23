## Qalypso Hackathon - Getting Started with TKET

Welcome to the Qalypso summer school!

This page will provide a quick intro to TKET and help you set up a programming environment with all the necessary packages installed.

If you have any questions during the summer school please feel free to ask me (Callum) or one of the other team members (Seyon or Luciana).

We have also created a [public slack channel](https://tketusers.slack.com/ssb/redirect) for support and discussion.

### Setting up a python environment

In order to manage python installations with minimal pain we recommend we set up a virtual environment. Virtual environments give you a place to install python packages and keep them separate from the other packages installed on your system.

```shell
python3 -m venv tket-env
```

Now you can activate your virtual environment as follows

```shell
source tket-env/bin/activate
```

Now that we have activated our virtual environment we can install packages inside this tket-env environment using the pip package manager.

```shell
pip install matplotlib
```

I have shown how to set up virtual environments using venv because this comes pre-installed with python. There are several other virtual environment managers you could use instead. Alternatively you could manage dependencies using a docker container or using poetry.

### Installing pytket and its Extensions

TKET is accessible though its python module, pytket. This can be installed using pip.

```shell
pip install pytket
```

In addition to the core pytket package there are also several pytket extension modules. These extensions enable the user to interface with quantum devices and simulators from different providers and also provide the ability to work with other popular quantum software libraries (qiskit, cirq and more).

Extensions can be installed by adding a hyphen to the installation command followed by the extension name.

```shell
pip install pytket-qiskit
```

Note that you will need python 3.8, 3.9 or 3.10 to use the latest version of pytket. To check which python version you have currently use `` python --verison``

For further help with installation see the [installation troubleshooting](https://cqcl.github.io/tket/pytket/api/install.html). You can also ask on [slack](https://tketusers.slack.com/ssb/redirect) or grab one of us in person.

### Getting Started with TKET

Lets start by building a basic circuit. 

```python
from pytket import Circuit
from pytket import OpType

circ = Circuit(3) # Create a Circuit with two qubits
circ.H(0) # Add a Hadamard to the 0th qubit
circ.CX(0,1) # CNOT with control qubit 0, target qubit 1
circ.Ry(0.5, 1) # Parameters specifed as number of half turns
circ.add_gate(OpType.CCX, [0,1,2]) # Less added using OpType enum
circ.measure_all() # Measure all qubits in the standard basis
```

Now a minimal example using the AerBackend from pytket-qiskit...

```python

from pytket import Circuit
from pytket.extensions.qiskit import AerBackend

bell_circ = Circuit(2)
bell_circ.H(0)
bell_circ.CX(0,1)

backend = AerBackend()
handle = backend.process_circuit(bell_circ)
result = backend.get_result(handle)
counts_dict = result.get_counts()
print(counts_dict)
```










