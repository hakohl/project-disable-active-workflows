#from disable_active_workflows import *

#import sys
#sys.path.append(r'/home/harald/git/project_python/project-disable-active-workflows/disable_active_workflows')
#from disable_active_workflows import *

disable_active_workflows = __import__("disable_active_workflows.py")
get_all_workflows = disable_active_workflows.get_all_workflows
determine_active_workflows = disable_active_workflows.determine_active_workflows
disable_workflows = disable_active_workflows.disable_workflows

def test_get_all_workflows_workflows_exist():
    owner = "hakohl"
    repository = "study-github"
    token = ""

    assert get_all_workflows(owner, repository, token)['total_count'] > 0

def test_get_all_workflows_workflows_no_exist():
    owner = "hakohl"
    repository = "test-repo-without-workflows"
    token = ""

    assert get_all_workflows(owner, repository, token)['total_count'] == 0

def test_determine_active_workflows_exist():
    all_workflows = {
        'total_count': 4, 'workflows': [
            {'id': 87866223,
             'node_id': 'W_kwDOJzK9uc4FPLtv',
             'name': 'exercise-cli-github',
             'path': '.github/workflows/exercise-cli-github.yml',
             'state': 'active',
             'created_at': '2024-02-29T08:30:29.000Z',
             'updated_at': '2024-05-02T07:27:01.000Z',
             'url': 'https://api.github.com/repos/hakohl/study-github/actions/workflows/87866223',
             'html_url': 'https://github.com/hakohl/study-github/blob/main/.github/workflows/exercise-cli-github.yml',
             'badge_url': 'https://github.com/hakohl/study-github/workflows/exercise-cli-github/badge.svg'
             },
            {'id': 88635874,
             'node_id': 'W_kwDOJzK9uc4FSHni',
             'name': 'exercise-rest-api-cli-github',
             'path': '.github/workflows/exercise-rest-api-cli-github.yml',
             'state': 'disabled_manually',
             'created_at': '2024-03-06T15:39:55.000Z',
             'updated_at': '2024-03-07T09:25:12.000Z',
             'url': 'https://api.github.com/repos/hakohl/study-github/actions/workflows/88635874',
             'html_url': 'https://github.com/hakohl/study-github/blob/main/.github/workflows/exercise-rest-api-cli-github.yml',
             'badge_url': 'https://github.com/hakohl/study-github/workflows/exercise-rest-api-cli-github/badge.svg'
             },
            {'id': 88736327,
             'node_id': 'W_kwDOJzK9uc4FSgJH',
             'name': 'exercise-rest-api-curl-github',
             'path': '.github/workflows/exercise-rest-api-curl-github.yml',
             'state': 'active',
             'created_at': '2024-03-07T09:32:46.000Z',
             'updated_at': '2024-05-02T07:26:27.000Z',
             'url': 'https://api.github.com/repos/hakohl/study-github/actions/workflows/88736327',
             'html_url': 'https://github.com/hakohl/study-github/blob/main/.github/workflows/exercise-rest-api-curl-github.yml',
             'badge_url': 'https://github.com/hakohl/study-github/workflows/exercise-rest-api-curl-github/badge.svg'
             },
            {'id': 63633678,
             'node_id': 'W_kwDOJzK9uc4DyvkO',
             'name': 'GitHub-Actions-Demo',
             'path': '.github/workflows/github-actions-demo.yml',
             'state': 'disabled_manually',
             'created_at': '2023-07-19T13:04:07.000Z',
             'updated_at': '2024-05-02T07:23:50.000Z',
             'url': 'https://api.github.com/repos/hakohl/study-github/actions/workflows/63633678',
             'html_url': 'https://github.com/hakohl/study-github/blob/main/.github/workflows/github-actions-demo.yml',
             'badge_url': 'https://github.com/hakohl/study-github/workflows/GitHub-Actions-Demo/badge.svg'
             }
        ]
    }

    assert determine_active_workflows(all_workflows) == [
        {'id': 87866223,
         'node_id': 'W_kwDOJzK9uc4FPLtv',
         'name': 'exercise-cli-github',
         'path': '.github/workflows/exercise-cli-github.yml',
         'state': 'active',
         'created_at': '2024-02-29T08:30:29.000Z',
         'updated_at': '2024-05-02T07:27:01.000Z',
         'url': 'https://api.github.com/repos/hakohl/study-github/actions/workflows/87866223',
         'html_url': 'https://github.com/hakohl/study-github/blob/main/.github/workflows/exercise-cli-github.yml',
         'badge_url': 'https://github.com/hakohl/study-github/workflows/exercise-cli-github/badge.svg'
         },
        {'id': 88736327,
         'node_id': 'W_kwDOJzK9uc4FSgJH',
         'name': 'exercise-rest-api-curl-github',
         'path': '.github/workflows/exercise-rest-api-curl-github.yml',
         'state': 'active',
         'created_at': '2024-03-07T09:32:46.000Z',
         'updated_at': '2024-05-02T07:26:27.000Z',
         'url': 'https://api.github.com/repos/hakohl/study-github/actions/workflows/88736327',
         'html_url': 'https://github.com/hakohl/study-github/blob/main/.github/workflows/exercise-rest-api-curl-github.yml',
         'badge_url': 'https://github.com/hakohl/study-github/workflows/exercise-rest-api-curl-github/badge.svg'
         }
    ]

def test_determine_active_workflows_no_exist():
    all_workflows = {
        'total_count': 4, 'workflows': [
            {'id': 87866223,
             'node_id': 'W_kwDOJzK9uc4FPLtv',
             'name': 'exercise-cli-github',
             'path': '.github/workflows/exercise-cli-github.yml',
             'state': 'disabled_manually',
             'created_at': '2024-02-29T08:30:29.000Z',
             'updated_at': '2024-05-02T07:27:01.000Z',
             'url': 'https://api.github.com/repos/hakohl/study-github/actions/workflows/87866223',
             'html_url': 'https://github.com/hakohl/study-github/blob/main/.github/workflows/exercise-cli-github.yml',
             'badge_url': 'https://github.com/hakohl/study-github/workflows/exercise-cli-github/badge.svg'
             },
            {'id': 88635874,
             'node_id': 'W_kwDOJzK9uc4FSHni',
             'name': 'exercise-rest-api-cli-github',
             'path': '.github/workflows/exercise-rest-api-cli-github.yml',
             'state': 'disabled_manually',
             'created_at': '2024-03-06T15:39:55.000Z',
             'updated_at': '2024-03-07T09:25:12.000Z',
             'url': 'https://api.github.com/repos/hakohl/study-github/actions/workflows/88635874',
             'html_url': 'https://github.com/hakohl/study-github/blob/main/.github/workflows/exercise-rest-api-cli-github.yml',
             'badge_url': 'https://github.com/hakohl/study-github/workflows/exercise-rest-api-cli-github/badge.svg'
             },
            {'id': 88736327,
             'node_id': 'W_kwDOJzK9uc4FSgJH',
             'name': 'exercise-rest-api-curl-github',
             'path': '.github/workflows/exercise-rest-api-curl-github.yml',
             'state': 'disabled_manually',
             'created_at': '2024-03-07T09:32:46.000Z',
             'updated_at': '2024-05-02T07:26:27.000Z',
             'url': 'https://api.github.com/repos/hakohl/study-github/actions/workflows/88736327',
             'html_url': 'https://github.com/hakohl/study-github/blob/main/.github/workflows/exercise-rest-api-curl-github.yml',
             'badge_url': 'https://github.com/hakohl/study-github/workflows/exercise-rest-api-curl-github/badge.svg'
             },
            {'id': 63633678,
             'node_id': 'W_kwDOJzK9uc4DyvkO',
             'name': 'GitHub-Actions-Demo',
             'path': '.github/workflows/github-actions-demo.yml',
             'state': 'disabled_manually',
             'created_at': '2023-07-19T13:04:07.000Z',
             'updated_at': '2024-05-02T07:23:50.000Z',
             'url': 'https://api.github.com/repos/hakohl/study-github/actions/workflows/63633678',
             'html_url': 'https://github.com/hakohl/study-github/blob/main/.github/workflows/github-actions-demo.yml',
             'badge_url': 'https://github.com/hakohl/study-github/workflows/GitHub-Actions-Demo/badge.svg'
             }
        ]
    }

    assert determine_active_workflows(all_workflows) == []

def test_disable_workflows():
    owner = "hakohl"
    repository = "study-github"
    token = ""

    # enable two workflows for test
    for id in (87866223, 88736327):
        api_url = f"https://api.github.com/repos/{owner}/{repository}/actions/workflows/{id}/enable"

        response = requests.put(
            api_url,
            auth=("", token)
        )

        print(f"Workflow with id \"{id}\" was enabled.")

    active_workflows = [
        {'id': 87866223,
         'node_id': 'W_kwDOJzK9uc4FPLtv',
         'name': 'exercise-cli-github',
         'path': '.github/workflows/exercise-cli-github.yml',
         'state': 'active',
         'created_at': '2024-02-29T08:30:29.000Z',
         'updated_at': '2024-05-02T07:27:01.000Z',
         'url': 'https://api.github.com/repos/hakohl/study-github/actions/workflows/87866223',
         'html_url': 'https://github.com/hakohl/study-github/blob/main/.github/workflows/exercise-cli-github.yml',
         'badge_url': 'https://github.com/hakohl/study-github/workflows/exercise-cli-github/badge.svg'
         },
        {'id': 88736327,
         'node_id': 'W_kwDOJzK9uc4FSgJH',
         'name': 'exercise-rest-api-curl-github',
         'path': '.github/workflows/exercise-rest-api-curl-github.yml',
         'state': 'active',
         'created_at': '2024-03-07T09:32:46.000Z',
         'updated_at': '2024-05-02T07:26:27.000Z',
         'url': 'https://api.github.com/repos/hakohl/study-github/actions/workflows/88736327',
         'html_url': 'https://github.com/hakohl/study-github/blob/main/.github/workflows/exercise-rest-api-curl-github.yml',
         'badge_url': 'https://github.com/hakohl/study-github/workflows/exercise-rest-api-curl-github/badge.svg'
         }
    ]

    assert disable_workflows(active_workflows, owner, repository, token) == 0
