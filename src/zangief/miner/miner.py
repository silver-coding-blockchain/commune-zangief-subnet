import argparse
from config import Config

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="transaction validator")
    parser.add_argument("--miner", type=str, default="openai", help="miner type")
    parser.add_argument("--config", type=str, default="env/config.ini", help="config file path")
    args = parser.parse_args()

    config = Config(config_file=args.config)

    if args.miner == "m2m":
        from m2m_miner import M2MMiner
        miner = M2MMiner(config=config)
        M2MMiner.start_miner_server(miner=miner)
    elif args.miner == "openai":
        from openai_miner import OpenAIMiner
        miner = OpenAIMiner(config=config)
        OpenAIMiner.start_miner_server(miner=miner)
    else:
        print("Unsupported miner")
