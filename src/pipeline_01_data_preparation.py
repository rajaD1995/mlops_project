import os
import argparse
import yaml # where we define our configurations
import logging #


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    # args.add_argument("--config", "-c", default="configs/config.yaml") # want to run from command line the config file
    # default points to config file path. if we want to run this script from command line we can provide default.
    
    args.add_argument("--config",  default="default")
    args.add_argument("--datasource", default=None)

    # Parses command-line arguments and stores them in 'parsed_args' as object attributes
    parsed_args = args.parse_args()

    print(parsed_args.config, parsed_args.datasource)

    # # read the config file
    # with open(parsed_args.config) as config_file:
    #     config = yaml.safe_load(config_file)

    # # Create necessary directories
    # os.makedirs(config['artifacts']['artifacts_dir'], exist_ok=True)
    # os.makedirs(config['artifacts']['raw_local_dir'], exist_ok=True)
    # os.makedirs(config['artifacts']['ingested_dir'], exist_ok=True)

    # # Set up logging
    # logging.basicConfig(
    #     filename=os.path.join(config['artifacts']['artifacts_dir'], 'data_preparation.log'),
    #     level=logging.INFO,
    #     format='%(asctime)s - %(levelname)s - %(message)s'
    # )

    # logging.info("Directories created successfully.")
