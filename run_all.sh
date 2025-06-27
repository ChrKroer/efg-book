#!/bin/bash
# OMD runs
uv run main.py --iter 2000 --print_freq 100 --game=leduc_poker --reg=Entropy --eta=20 --alg=DOMD --avg=avg-iterate
uv run main.py --iter 2000 --print_freq 100 --game=leduc_poker --reg=Euclidean --eta=3 --alg=DOMD --avg=linear-avg-iterate

# CFR runs
uv run main.py --iter 2000 --print_freq 100 --game=leduc_poker --alg=CFR --avg=avg-iterate
uv run main.py --iter 2000 --print_freq 100 --game=leduc_poker --alg=CFR+ --avg=linear-avg-iterate
