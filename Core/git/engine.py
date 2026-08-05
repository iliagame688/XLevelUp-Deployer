from git.repository import find_repo
from git.status import git_status
from git.remote import get_remote



def inspect_workspace(path):

    print("""
╭──────────────────────────╮
│ XDEPLOY GIT ENGINE       │
╰──────────────────────────╯
""")


    repo = find_repo(path)


    if not repo:

        print(
            "REPOSITORY\n✗ NOT FOUND"
        )

        return None


    print(
        "REPOSITORY\n✓ DETECTED"
    )

    print(
        repo
    )


    changes = git_status(repo)


    print()

    print(
        "CHANGES:",
        len(changes)
    )


    remote = get_remote(repo)


    print()

    if remote:

        print(
            "REMOTE\n✓ CONFIGURED"
        )

        print(remote)

    else:

        print(
            "REMOTE\n○ NOT CONFIGURED"
        )


    return {
        "repo": str(repo),
        "changes": changes,
        "remote": remote
    }
