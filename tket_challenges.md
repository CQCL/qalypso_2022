## Suggestions for Issues to Tackle (development tasks)

- https://github.com/CQCL/tket/issues/490 --> `get_unitary` and `get_statevector` should throw an error if circuit contains measurements
- https://github.com/CQCL/tket/issues/275 --> Add more options to `Backend.get_compiled_circuit`
- https://github.com/CQCL/pytket-extensions/issues/477 --> Add Anhamonicity to pytket-qiskit backend info
- https://github.com/CQCL/pytket-qujax/issues/40 --> Expand gateset in pytket-qujax


## Research Tasks
- Implement a Toffoli Simulator in python (A simulator for classical logic circuits). I.e a simulator for the $\{X, CX, CCX, ..., CnX\}$ gateset. See [here](https://barghouthi.github.io/2021/08/05/quantum/) for some ideas for how to write a simulator in python.
- Implement a routing method for a decomposition of CnX gates.
- Implement circuit gradients in pytket using the parameter shift rule or finite difference methods.





