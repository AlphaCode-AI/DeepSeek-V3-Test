# 허깅페이스에서 특정 모델을 특정 경로로 다운로드하는 코드 작성
import os
import argparse
from huggingface_hub import snapshot_download

def download_model(model_name, local_dir=None):
    if local_dir is None:
        local_dir = os.path.join("models", model_name.split("/")[-1])
    
    os.makedirs(local_dir, exist_ok=True)
    
    local_dir_with_files = snapshot_download(
        repo_id=model_name,
        local_dir=local_dir,
        local_dir_use_symlinks=False,
    )
    
    print(f"모델 '{model_name}'이(가) '{local_dir_with_files}'에 다운로드되었습니다.")
    return local_dir_with_files

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="허깅페이스에서 모델 다운로드")
    parser.add_argument("--model_name", type=str, required=True, help="다운로드할 모델 이름 (예: 'deepseek-ai/deepseek-v3')")
    parser.add_argument("--local_dir", type=str, default=None, help="모델을 저장할 로컬 경로")
    
    args = parser.parse_args()
    download_model(args.model_name, args.local_dir)