# FastSC
Frequency-Aware Synthesis Toolbox for Superconducting Quantum Computers


## Install

It is encouraged to install the software using virtualenv

`python3 -m venv path/to/env`

`source path/to/env/bin/activate`

`pip install -r requirements.txt`

`pip install -e .`

## Run test

`cd tests/`

## Run frequency assignment algorithm

`cd experiments/`

`python3 frequency_simulate.py -h`

## Trouble Shooting

If the required packages fail to install, try running the following command manually after setting up a new virtualenv with python3:

`python3 -m venv path/to/env`

`source path/to/env/bin/activate`

`pip install --upgrade pip`

`pip install Cython`

`pip install sympy`

`pip install numpy`

`pip install scipy`

`pip install qutip`

`pip install jupyter`

`pip install matplotlib`

`pip install networkx`

`pip install qiskit`

`python3 -m pip install z3-solver`

`pip install -e .`

