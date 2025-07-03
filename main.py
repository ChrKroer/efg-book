import numpy as np
import pyspiel
import LiteEFG as leg
import algorithms.CFR as CFR
import LiteEFG.baselines.CFRplus as CFRp
import algorithms.DOMD as DOMD
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--traverse_type", type=str, choices=["Enumerate", "External"], default="Enumerate")
parser.add_argument("--iter", type=int, default=1000)
parser.add_argument("--game", type=str, default="leduc_poker")
parser.add_argument("--alg", type=str, default="CFR+")
parser.add_argument("--avg", type=str, default="avg-iterate")
parser.add_argument("--reg", type=str, default="Entropy")
parser.add_argument("--eta", type=float, default=0.1)
parser.add_argument("--log", type=bool, default=False)
parser.add_argument("--print_count", type=int, default=10)
args = parser.parse_args()

def run(algo, algname, outfile=None):
    game = pyspiel.load_game(args.game)
    env = leg.OpenSpielEnv(game, traverse_type=args.traverse_type) # load the environment from files
    env.set_graph(algo) # pass graph to the environment
    avgname = ""
    if args.avg == "linear-avg-iterate":
        avgname = " lin"
    if args.log:
        print_iters = np.logspace(0, int(np.log10(args.iter)), num=args.print_count, base=10, dtype=int)
    else:
        print_iters = np.linspace(0, args.iter, num=args.print_count+1, dtype=int)
    for i in range(args.iter+1):
        algo.update_graph(env) # update the graph
        env.update_strategy(algo.current_strategy()) 
        # automatically update the last-iterate, best-iterate, avg-iterate, linear-avg-iterate of the strategy
        if i in print_iters:
            expl = np.sum(env.exploitability(algo.current_strategy(), args.avg))
            print(f"{i}\t{expl}")
            if outfile is not None:
                print(f"{i},{expl},{algname}{avgname},{args.game}", file=outfile)





algmap = {"CFR": CFR, "CFR+": CFRp, "DOMD": DOMD}
if args.alg in ["CFR", "CFR+"]:
    f = open(f'output/{args.game}_{args.alg}_{args.avg}_{args.traverse_type}.csv', 'w')
    run(algmap[args.alg].graph(), args.alg, f)
else:
    f = open(f'output/{args.game}_{args.alg}_{args.avg}_{args.reg}_{args.eta}_{args.traverse_type}.csv', 'w')
    run(DOMD.graph(eta=args.eta, regularizer=args.reg), f"DOMD({args.reg})", f)
f.close()
            