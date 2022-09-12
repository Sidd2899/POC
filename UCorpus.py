from typing import Any
from dvc.repo import Repo
import git

class UCorpus:
    # initialize local repository
    def init(self,localRepo):
        self.d = Repo.init(localRepo,no_scm=True,force=True)
        self.g = git.Repo.init(localRepo)
    #adding files .dvc and to put current working files into the current index ) for dvc command and rest for git
    def add(self,folder,filetype = 0):
        defaultfile = '--all'
        if filetype == 0:
            Repo.add(self.d,folder)
        else: self.g.git.add(defaultfile)
    
    #Clone an existing repository into a new directory,
    def clone(localRepo,RepoAddress):
        git.Git(localRepo).clone(RepoAddress)
    
    #fetching changes from remote repo
    def fetch(self):
        self.d.fetch(self,remote='remote_store')
        self.g.remote().fetch()
    
    #Creating remote 
    def remote(self,remoterepolocation,gitrepoloc):
        with self.d.config.edit() as conf:
            conf["remote"]["remote_store"] = {"url": str(remoterepolocation)}
        self.g.delete_remote('master')
        self.g.create_remote('master',str(gitrepoloc))
    
    #pushing the Changes to the Remote Repo
    def push(self):
        Repo.push(self.d,remote='remote_store')
        print(self.g.remotes.master.push())
        
    
    def commit(self,localRepo,message = ''):
        self.d.commit(target=localRepo,force=True)
        self.g.index.commit(message)



    