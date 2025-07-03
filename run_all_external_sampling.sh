#!/bin/bash
t=100000
# Leduc
# OMD runs
uv run main.py --iter $t --game=leduc_poker --reg=Entropy --eta=0.05 --alg=DOMD --avg=avg-iterate --traverse_type=External
uv run main.py --iter $t --game=leduc_poker --reg=Euclidean --eta=0.005 --alg=DOMD --avg=avg-iterate  --traverse_type=External

# CFR runs
uv run main.py --iter $t --game=leduc_poker --alg=CFR --avg=avg-iterate --traverse_type=External
uv run main.py --iter $t --game=leduc_poker --alg=CFR+ --avg=avg-iterate --traverse_type=External

# Kuhn
# OMD runs
uv run main.py --iter $t --game=kuhn_poker --reg=Entropy --eta=0.09 --alg=DOMD --avg=avg-iterate --traverse_type=External
uv run main.py --iter $t --game=kuhn_poker --reg=Euclidean --eta=0.01 --alg=DOMD --avg=avg-iterate --traverse_type=External

# CFR runs
uv run main.py --iter $t --game=kuhn_poker --alg=CFR --avg=avg-iterate --traverse_type=External
uv run main.py --iter $t --game=kuhn_poker --alg=CFR+ --avg=avg-iterate --traverse_type=External

# Sheriff
# OMD runs
uv run main.py --iter $t --game=sheriff --reg=Entropy --eta=0.02 --alg=DOMD --avg=avg-iterate --traverse_type=External
uv run main.py --iter $t --game=sheriff --reg=Euclidean --eta=0.005 --alg=DOMD --avg=avg-iterate --traverse_type=External

# CFR runs
uv run main.py --iter $t --game=sheriff --alg=CFR --avg=avg-iterate --traverse_type=External
uv run main.py --iter $t --game=sheriff --alg=CFR+ --avg=avg-iterate --traverse_type=External