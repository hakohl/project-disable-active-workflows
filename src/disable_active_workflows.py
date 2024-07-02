# disable active GitHub workflows
import argparse
import requests

def list_repos(owner, token):
    check_existence_owner(owner, token)
    all_repos = get_all_repos(owner, token)

    print(f"Repositories of owner \"{owner}\":\n")

    for repository in all_repos:
        print(f"{repository['name']}")
    
    return 0    

def check_existence_owner(owner, token):
    api_url = f"https://api.github.com/users/{owner}"
    #token = ""

    response = requests.get(
        api_url,
        auth=("", token)
    )
    
    if not response:
        raise Exception(f"Owner \"{owner}\" not found.")
    
    return 0

def check_existence_repo(owner, repository):
    api_url = f"https://api.github.com/repos/{owner}/{repository}"
    token = ""

    response = requests.get(
        api_url,
        auth=("", token)
    )
    
    if not response:
        if response.status_code == 404:
            raise Exception(f"Repository \"{owner}/{repository}\" not found.")
        else:
            raise Exception(f"Non-success status code: {response.status_code} - {response.text}")
    
    return 0
        
def get_all_repos(owner, token):
    api_url = f"https://api.github.com/users/{owner}/repos"
    #token = ""

    response = requests.get(
        api_url,
        auth=("", token)
    )

    all_repos = response.json()

    return all_repos

def get_all_workflows(owner, repository, token):
    api_url = f"https://api.github.com/repos/{owner}/{repository}/actions/workflows"

    response = requests.get(
        api_url,
        auth=("", token)
    )

    all_workflows = response.json()

    return all_workflows

def determine_active_workflows(all_workflows):
    active_workflows=[]

    for workflow in all_workflows['workflows']:
        #print(f"{workflow['name']}: {workflow['state']}")

        if workflow['state'] == "active":
            active_workflows.append(workflow)

    return active_workflows

def disable_workflows(active_workflows, owner, repository, token):
    num_active_workflows = len(active_workflows)

    for workflow in active_workflows:
        api_url = f"https://api.github.com/repos/{owner}/{repository}/actions/workflows/{workflow['id']}/disable"

        response = requests.put(
            api_url,
            auth=("", token)
        )

        if not response:
            raise Exception(f"Non-success status code: {response.status_code} - {response.text}")

        print(f"Workflow \"{workflow['name']}\" was disabled.")
        num_active_workflows -= 1

    return num_active_workflows

def main():
    token=""
    
    # create main parser
    parser = argparse.ArgumentParser(
        prog="disable_active_workflows",
        description="Disable active workflows"
    )

    subparsers = parser.add_subparsers(dest='subcommand', title='subcommands', help='sub-command help', required=True, )

    # create subparser for command "list-repos"
    parser_list_repos = subparsers.add_parser('list-repos', help='list repos of one GitHub owner')
    parser_list_repos.add_argument('owner', nargs=1, help='GitHub owner name')

    # create subparser for command "list-workflows"
    parser_list_workflows = subparsers.add_parser('list-workflows', help='list workflows of one GitHub repository')
    parser_list_workflows.add_argument('owner', nargs=1, help='GitHub owner name')
    parser_list_workflows.add_argument('repository', nargs=1, help='GitHub repository name')

    # create subparser for command "disable-workflows"
    parser_disable_workflows = subparsers.add_parser('disable-workflows', help='disable workflows of one GitHub repository')
    parser_disable_workflows.add_argument('owner', nargs=1, help='GitHub owner name')
    parser_disable_workflows.add_argument('repository', nargs=1, help='GitHub repository name')

    #group = parser.add_mutually_exclusive_group(required=True)
    #group.add_argument('--list-repos', help='list repositories of one GitHub owner')
    #group.add_argument('owner', default='hakohl', help="GitHub owner name")
    #group.add_argument('--list-workflows', help='list workflows of one GitHub repository')

    #parser.add_argument("owner", nargs=1, help="GitHub owner name")
    #parser.add_argument("repository", nargs=1, help="GitHub repository name")

    args=parser.parse_args()

    if args.subcommand == "list-repos":
        owner = args.owner[0]
        list_repos(owner, token)






    print(f"Handle workflows in GitHub repository \"{owner}/{repository}\".")
    print("Get all workflows ...")
    all_workflows = get_all_workflows(owner, repository, token)
    if all_workflows['total_count'] == 0:
        raise Exception(f"There are no workflows in repository \"{repository}\"!")

    print("Determine active workflows ...")
    active_workflows = determine_active_workflows(all_workflows)
    if active_workflows == []:
        raise Exception(f"There are no active workflows in repository \"{repository}\"!")

    print("Disable active workflows ...")
    disable_workflows(active_workflows, owner, repository, token)

if __name__ == "__main__":
    main()
