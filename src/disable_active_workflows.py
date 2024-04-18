# disable active GitHub workflows
import requests

owner = "hakohl"
repository = "study-github"
token = ""

print(f"Handle workflows in GitHub repository \"{repository}\".")

def get_all_workflows():
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
        print(f"{workflow['name']}: {workflow['state']}")
        
        if workflow['state'] == "active":
            active_workflows.append(workflow) 

    return active_workflows

def disable_workflows(active_workflows):
    for workflow in active_workflows:
        api_url = f"https://api.github.com/repos/{owner}/{repository}/actions/workflows/{workflow['id']}/disable"

        response = requests.put(
            api_url,
            auth=("", token)
        )

        print(f"Workflow \"{workflow['name']}\" was disabled.")

def main():
    # get workflow data from GitHub
    print("Get workflow data from GitHub ...")
    all_workflows = get_all_workflows()
    print("Determine active workflows ...")
    active_workflows = determine_active_workflows(all_workflows)
    print("Disable active workflows ...")
    disable_workflows(active_workflows)

if __name__ == "__main__":
    main()