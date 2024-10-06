import os
import pandas as pd
from tqdm import tqdm
from git import Repo

# 레포 CSV 파일 읽기
repo_data = pd.read_csv('repo.csv')

# 이름과 깃허브 레포 링크로 딕셔너리 생성
repo_dict = {repo_data['이름'].iloc[i]: repo_data['깃허브 레포 링크'].iloc[i] for i in range(len(repo_data))}

def clone_repo(key, url):
    try:
        # 해당 이름의 디렉토리가 이미 존재하는지 확인
        if os.path.exists(key) and os.path.isdir(key):
            print(f"Repository '{key}' already exists. Pulling latest changes...")
            repo = Repo(key)
            repo.remotes.origin.pull()
        else:
            print(f"Cloning repository '{key}' from {url}...")
            Repo.clone_from(url, key)
            print(f"Repository '{key}' cloned successfully.")
    except Exception as e:
        print(f"Failed to process repository '{key}'. Error: {str(e)}")

# 레포지토리 딕셔너리를 순회하며 처리
for key, value in tqdm(repo_dict.items(), desc="Processing repositories"):
    clone_repo(key, value)
