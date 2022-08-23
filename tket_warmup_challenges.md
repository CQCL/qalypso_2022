# Qualypso Hackathon - Warmup Problems

These are exercises based on standard quantum computing basics and are designed to get you familiar with constructing and compiling circuits with TKET.

### (I) TKET Basics

This is basic exercise that will get you used to building circuits and using Backends from the pytket-qiskit extension.

1. define a function build_ghz_circuit which builds a n-qubit GHZ state for a specified number of qubits
2. Run your circuit on the AerStateBackend to verify that your solution is correct
3. Run your circuit on the shots-based IBMQEmualtorBackend from the pytket-qiskit extension. What is different from exercise (2.)?


### (II)  The Quantum Fourier Transform and Phase Estimation

1. Define a function build_qft_circ which constructs the circuit to perform the Quantum Fourier transform for n qubits (Hint: You can use recursion)

2. Write a script that implements the quantum phase estimation algorithm. This will involve using the QFT (or its inverse) as a subroutine. Start off by creating a circuit that estimates the phase applied to one ancilla qubit using $m$ measurement qubits.

3. Can you further generalise your solution to (2.)?


### (III) Grover's algorithm

1. Define construct a circuit which implements a grover oracle for the basis state '1101'. When this oracle is applied to the uniform superposition the state '1101' should be marked with a minus sign and the rest of the states should be unchanged. Verify your solution with a statevector simulator.

2. Generalise a solution to (1.) which will work for any chosen basis state. The appendix of [This paper](https://www.diva-portal.org/smash/get/diva2:1214481/FULLTEXT01.pdf) may be helpful.

3. Finish off your Grover implementation by creating a circuit for the reflection step of the algorithm. Combine this with your solution to (2.) The oracle and reflection steps can then be repeated iteratively. How can we apply the optimial number of iterations?

4. Run your algorithm on a simulator (Maybe try the Noiseless AerBacked first).

### (IV) Circuit Optimisation

1. Take the circuits generated in sections (II) and (III). Execute the circuits on the H1-1E emulator from the quantinuum extension after applying the default_compilation_pass to reduce the size of the circuit.

2. The default_compilation_pass used above is a pre-defined sequence of optimisation passes tailored for the H1 emualtor. Now try experimenting with different optimisation passes and construct your own SequencePass to optimise your circuits.

3. Define your own optimsation pass using [CustomPass](https://cqcl.github.io/pytket/manual/manual_compiler.html#user-defined-passes). Perhaps start off with a relatively simple CXCancellationPass that cancels adjacent CX gates which act on the same qubits.Try and experiment with this to see if you can come up with any novel ways to optimise quantum circuits, we'd be interested to know anything you come up with! 

See also the "Research problems section of the Hackathon"