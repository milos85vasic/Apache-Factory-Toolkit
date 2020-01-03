import subprocess
import json

key_branch = "branch"
destination = "git_info.json"
key_repository = "repository"


def set_git_info():
    star = "* "
    branch = ""
    repository = ""
    fetch_url = "Fetch URL:"
    url_result, _ = subprocess.Popen(["git", "remote", "show", "origin"], stdout=subprocess.PIPE).communicate()
    branch_result, _ = subprocess.Popen(["git", "branch"], stdout=subprocess.PIPE).communicate() 
    url_split_result = url_result.splitlines(keepends=False)
    branch_split_result = branch_result.splitlines(keepends=False)

    for line in url_split_result:
        print("> > > ", line)
        if fetch_url in line:
            repository = line.replace(fetch_url, "").strip()
            break

    for line in branch_split_result:
        print("> > > ", line)
        if "* " in line:
            branch = line[line.index(star) + star.__len__():].strip()
            break

    git_configuration = {
        key_branch: branch,
        key_repository: repository
    }

    print("Repository is: ", git_configuration[key_repository])
    print("Branch is: ", git_configuration[key_branch])

    try:
        with open(destination, 'w') as outfile:
            json.dump(git_configuration, outfile)
    except IOError:
        print("Can't access " + destination)


def get_git_info():
    return json.load(open(destination))
