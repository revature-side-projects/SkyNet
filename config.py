import sys

from datetime import date, datetime, timedelta

github_dateformat = "%Y-%m-%dT%H:%M:%SZ"
config_dateformat = "%m/%d/%Y"

def parseArgs(config):
    if "orgs" not in config and len(sys.argv) == 1:
        raise Exception('At least 1 GitHub org must be provided to analyze')

    orgs = config.get('orgs', [])
    for i in range(1, len(sys.argv)):
        orgs.append(sys.argv[i])
    config['orgs'] = orgs

def parseConfig(config):
    if "token" not in config:
        print('GitHub API Token not found in config, looking in SKYNET_TOKEN environment variable instead')
        config["token"] = os.environ.get('SKYNET_TOKEN', None)

    if config["token"] == None:
        print('Could not find GitHub API Token')
        raise Exception('GitHub API Token required; Please include in .config.json or as SKYNET_TOKEN environment variable')

    if "until" not in config:
        print('No ending date provided, defaulting to retrieve commits until the end of commit history')
        config["until"] = None
    else:
        config["until"] = datetime.strftime(datetime.strptime(config["until"], config_dateformat), github_dateformat)

    if "since" not in config:
        print('No starting date provided, defaulting to retrieve commits from the beginning of commit history')
        config["since"] = None
    else:
        config["since"] = datetime.strftime(datetime.strptime(config["since"], config_dateformat), github_dateformat)

    if "duration_days" in config and config["since"] != None:
        print('A duration was provided: Overriding the "until" property based on the duration')
        start_date = datetime.strptime(config['since'], github_dateformat)
        config["until"] = (start_date + timedelta(days=config["duration_days"])).strftime(github_dateformat)