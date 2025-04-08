@echo off
chcp 65001
cd /d %~dp0

echo [🔍] 가상환경(v-env) 확인 중...

if not exist venv (
    echo [🛠️] venv 폴더 없음 → 새로 생성합니다...
    python -m venv venv
    if errorlevel 1 (
        echo [❌] venv 생성 실패. Python이 설치되어 있는지 확인하세요.
        pause
        exit /b
    )
)

echo [🌱] 가상환경 활성화 중...
call venv\Scripts\activate

echo [📦] 필요한 패키지 설치 중...
pip install pillow imagehash

if errorlevel 1 (
    echo [❌] 패키지 설치 중 오류 발생!
    pause
    exit /b
)

echo [✅] 설치 완료! 이제 run.bat로 실행하세요.
pause
