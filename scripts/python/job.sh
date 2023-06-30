#!/bin/bash

#$ -M msiddiq3@nd.edu   # Email address for job notification
#$ -m abe            # Send mail when job begins, ends and aborts
#$ -pe smp 1     # Specify parallel environment and legal core size
#$ -q long           # Specify queue
#$ -N  rules

conda activate Franc
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/afs/crc.nd.edu/user/m/msiddiq3/.conda/envs/Franc/lib/
python controller.py
