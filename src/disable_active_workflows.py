# disable active GitHub workflows
import argparse
import requests

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
    parser = argparse.ArgumentParser(
        prog="disable_active_workflows",
        description="Disable active workflows"
    )

    parser.add_argument("owner", nargs=1, help="GitHub account name")
    parser.add_argument("repository", nargs=1, help="GitHub repository name")

    args=parser.parse_args()

    owner = args.owner[0]
    repository = args.repository[0]

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
