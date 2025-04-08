@echo off
chcp 65001
cd /d %~dp0

if not exist venv (
    echo [❌] 가상환경이 없습니다. 먼저 install.bat를 실행하세요.
    pause
    exit /b
)

echo [🌱] 가상환경 활성화 중...
call venv\Scripts\activate

echo [🧹] 유사 이미지 필터링 시작...
python training_data_filter.py

echo [✔] 작업 완료! 창을 닫으려면 아무 키나 누르세요.
pause
