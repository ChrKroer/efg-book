#!/bin/bash

# Leduc
# OMD runs
uv run main.py --iter 10000 --game=leduc_poker --reg=Entropy --eta=20 --alg=DOMD --avg=avg-iterate
uv run main.py --iter 10000 --game=leduc_poker --reg=Euclidean --eta=3 --alg=DOMD --avg=linear-avg-iterate

# CFR runs
uv run main.py --iter 10000 --game=leduc_poker --alg=CFR --avg=avg-iterate
uv run main.py --iter 10000 --game=leduc_poker --alg=CFR+ --avg=avg-iterate
uv run main.py --iter 10000 --game=leduc_poker --alg=CFR+ --avg=linear-avg-iterate

# Kuhn
# OMD runs
uv run main.py --iter 10000 --game=kuhn_poker --reg=Entropy --eta=20 --alg=DOMD --avg=avg-iterate
uv run main.py --iter 10000 --game=kuhn_poker --reg=Euclidean --eta=2 --alg=DOMD --avg=linear-avg-iterate

# CFR runs
uv run main.py --iter 10000 --game=kuhn_poker --alg=CFR --avg=avg-iterate
uv run main.py --iter 10000 --game=kuhn_poker --alg=CFR+ --avg=avg-iterate
uv run main.py --iter 10000 --game=kuhn_poker --alg=CFR+ --avg=linear-avg-iterate

# Sheriff
# OMD runs
uv run main.py --iter 10000 --game=sheriff --reg=Entropy --eta=5 --alg=DOMD --avg=avg-iterate
uv run main.py --iter 10000 --game=sheriff --reg=Euclidean --eta=1 --alg=DOMD --avg=linear-avg-iterate

# CFR runs
uv run main.py --iter 10000 --game=sheriff --alg=CFR --avg=avg-iterate
uv run main.py --iter 10000 --game=sheriff --alg=CFR+ --avg=avg-iterate
uv run main.py --iter 10000 --game=sheriff --alg=CFR+ --avg=linear-avg-iterate