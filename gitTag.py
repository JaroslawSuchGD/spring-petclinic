import semver
from git import Repo

def get_latest_tag_short_gitpython(repo_path='.'):
    try:
        repo = Repo(repo_path)
        tags = sorted([tag.name for tag in repo.tags], key=semver.VersionInfo.parse)
        return tags[-1] if tags else None
    except Exception as e:
        print(f"Error: {e}")
        return None
    
def add_tag(repo_path='.', tag_name="", ref='HEAD'):
    try:
        repo = Repo(repo_path)
        tag = repo.create_tag(tag_name, ref=ref)
        return True
    except Exception as e:
        return False

if __name__ == "__main__":
    latest = get_latest_tag_short_gitpython()
    version = None
    if not latest:
        add_tag(tag_name='1.0.0')
    else:
        version = semver.Version.parse(latest).bump_minor()
        new_tag = f"{version.major}.{version.minor}.{version.patch}"

        if version.prerelease != None:
            new_tag += f"-{version.prerelease}"
        
        if version.build != None:
            new_tag += f"+{version.build}"

        add_tag(tag_name = new_tag)
