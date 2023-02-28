from git import Repo
username = "outscale-vbr"
password = "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"
remote = f"https://{username}:{password}@github.com/outscale-vbr/upjet-provider-outscale.git"
repo = Repo()
repo.git.add("*")
repo.index.commit("hello")
Repo.clone_from(remote,)
repo.remote()
origin = repo.remote(name="origin")
origin.push()
