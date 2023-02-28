from git import Repo
username = "outscale-vbr"
password = ""
remote = f"https://{username}:{password}@github.com/outscale-vbr/upjet-provider-outscale.git"
repo = Repo()
repo.git.add("*")
repo.index.commit("hello")