import pyspiel
import LiteEFG as leg
import algorithms.CFR as CFR
import LiteEFG.baselines.CFRplus as CFRp
import algorithms.DOMD as DOMD
import argparse
from tqdm import tqdm

def run(gamename, algo, iterations, outfile, algname, avg="linear-avg-iterate"):
    leduc_poker = pyspiel.load_game(gamename)
    env = leg.OpenSpielEnv(leduc_poker, traverse_type=args.traverse_type) # load the environment from files
    env.set_graph(algo) # pass graph to the environment

    for i in range(args.iter+1):
        algo.update_graph(env) # update the graph
        env.update_strategy(algo.current_strategy()) 
        # automatically update the last-iterate, best-iterate, avg-iterate, linear-avg-iterate of the strategy
        if i % args.print_freq == 0:
            expl = max(env.exploitability(algo.current_strategy(), avg))
            print(f"{i}\t{expl}")
            print(f"{i},{expl},{algname}", file=outfile)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--traverse_type", type=str, choices=["Enumerate", "External"], default="Enumerate")
    parser.add_argument("--iter", type=int, default=1000)
    parser.add_argument("--print_freq", type=int, default=100)
    parser.add_argument("--game", type=str, default="leduc_poker")
    parser.add_argument("--alg", type=str, default="CFR+")
    parser.add_argument("--avg", type=str, default="avg-iterate")
    parser.add_argument("--reg", type=str, default="Entropy")
    parser.add_argument("--eta", type=float, default=0.1)
    args = parser.parse_args()



    algmap = {"CFR": CFR, "CFR+": CFRp, "DOMD": DOMD}
    if args.alg in ["CFR", "CFR+"]:
        f = open(f'output/{args.game}_{args.alg}_{args.avg}_{args.traverse_type}.csv', 'w')
        run(args.game, algmap[args.alg].graph(), args.iter, f, "CFR+", args.avg)
    else:
        f = open(f'output/{args.game}_{args.alg}_{args.avg}_{args.reg}_{args.eta}_{args.traverse_type}.csv', 'w')
        run(args.game, DOMD.graph(eta=args.eta, regularizer=args.reg), args.iter, f, f"DOMD({args.reg})", args.avg)
    f.close()
    # run(args.game, DOMD.graph(eta=args.eta, regularizer="Euclidean"), args.iter, f, "DOMD(L2)")
    # run(args.game, CFRp.graph(), args.iter, f, "CFR+")
    # run(args.game, CFR.graph(), args.iter, f, "CFR")
            