OPENQASM 2.0;
include "qelib1.inc";

qreg q[3];
creg c[2];
h q[0];
h q[1];
x q[2];
cu1(0.25*pi) q[1],q[2];
cu1(0.25*pi) q[0],q[2];
cu1(0.25*pi) q[0],q[2];
swap q[0],q[1];
h q[1];
cu1(1.5*pi) q[1],q[0];
measure q[1] -> c[1];
h q[0];
measure q[0] -> c[0];
