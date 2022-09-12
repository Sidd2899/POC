from re import S
from UCorpus import UCorpus

s = UCorpus

s.init(s,'/home/siddhant/Audiofiles/POC')

s.add(s,'/home/siddhant/Audiofiles/POC/2BqVo8kVB2Skwgyb',0)
s.add(s,'https://github.com/Sidd2899/POC.git',1)
s.commit(s,'/home/siddhant/Audiofiles/POC/2BqVo8kVB2Skwgyb.dvc','abc')
s.remote(s,'s3://uniphoredataops/data/','https://github.com/Sidd2899/POC.git')
s.fetch(s)
    
s.push(s)




