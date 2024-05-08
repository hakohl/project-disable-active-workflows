# disable active GitHub workflows
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

        print(f"Workflow \"{workflow['name']}\" was disabled.")
        num_active_workflows -= 1

    return num_active_workflows

def main():
    owner = "hakohl"
    repository = "study-github"
    #repository = "project-disable-active-workflows"
    token = ""

    print(f"Handle workflows in GitHub repository \"{repository}\".")
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