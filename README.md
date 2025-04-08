# 🧹 lora-image-filter

A Python script to automatically detect and group near-duplicate images using perceptual hashing (pHash).  
Ideal for cleaning datasets before training LoRA or Stable Diffusion models.

---

## 📌 프로젝트 소개 

Perceptual Hashing (pHash) 기법을 사용하여  
**거의 동일한 이미지들을 자동으로 감지하고 그룹화**하는 파이썬 스크립트입니다.  
LoRA 또는 Stable Diffusion 모델 학습 전 **데이터셋을 정제**하는 데 매우 유용합니다.

---

## 🛠️ 설치 및 실행 방법

1. 이 저장소를 클론합니다:

```bash
git clone https://github.com/squirrel765/lora-image-filter.git
cd lora-image-filter
```

2. `install.bat` 실행 (최초 1회 실행)
   - 가상환경(`.venv`)이 생성되고
   - 필요한 Python 패키지(`pillow`, `imagehash`)가 자동으로 설치됩니다.

3. 유사 이미지 필터링을 실행하려면 `run.bat`를 실행하세요.
   - `input_images/` 폴더 안에 필터링할 이미지들을 넣어두면 됩니다.
   - 실행 결과는 `grouped_duplicates/` 폴더로 자동 분류되어 저장됩니다.
