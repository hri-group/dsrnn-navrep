# dsrnn-navrep
Used for [DS-RNN](https://github.com/Shuijing725/CrowdNav_DSRNN) neural network within the [NavRep](https://github.com/ethz-asl/navrep) training environment with static obstacles.
Some modifications are made to the DS-RNN model so the two can't be replaced with each other.

## Setup

1. Clone github repo
2. Install Python3.6 (can use virtual environment for this)
3. Install all required libraries using 
```pip install -r requirements.txt"```
4. Install [OpenAI Baselines](https://github.com/openai/baselines#installation)
```
git clone https://github.com/openai/baselines.git
cd baselines
pip install -e .
```
5. Install [Python-RVO2 library](https://github.com/sybrenstuvel/Python-RVO2)

## Getting started
This repository is organized in three parts:

- `crowd_sim/` folder contains the simulation environment.

- `crowd_nav/` folder contains configurations and non-neural network policies

- `pytorchBaselines/` contains the code for the DSRNN network and ppo algorithm.

- `a/` folder contains all the functions/classes used for [navreptrainenv.py](crowd_sim/envs/navreptrainenv.py) <- the file containing the NavRep training environment

Please try not to modify the `a/` folder without first understanding how it affects the NavRep training environment. Because the code is a mashup of two different repositories, there are some odd quirks when running the code-
- There are two different files containing the configs for the code
- `a/crowd_nav/config/test_soadrl_static.config` <- used for modifying the NavRep training environment EXCLUSIVELY (e.g. no. pedestrians, robot FOV, etc.)
- `crowd_nav/configs/config.py` <- used for modifying the training/testing stage itself (e.g. no. training steps, whether to visualise training or not, etc.)


## Running code
1. Train a policy.
```python train.py ```
2. Test policies.
Please modify the test arguments in the begining of test.py.
```python test.py ```
3. Plot training curve.
```python plot.py ```
