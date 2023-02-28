from git import Repo
username = "outscale-vbr"
full_local_path = "/home/outscale/upjet-provider-outscale"
password = "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"
remote = f"https://{username}:{password}@github.com/outscale-vbr/upjet-provider-outscale.git"
repo = Repo(full_local_path)
repo.git.add("*")
repo.index.commit("hello")
Repo.clone_from(remote,full_local_path)
repo.remote()
origin = repo.remote(name="origin")
origin.push()
