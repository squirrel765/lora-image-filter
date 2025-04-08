import os
import shutil
from PIL import Image
import imagehash

# 이미지 해시 계산 함수 (pHash 사용)
def get_image_hashes(folder):
    hashes = []
    filenames = []
    for fname in os.listdir(folder):
        if fname.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp')):
            try:
                img_path = os.path.join(folder, fname)
                img = Image.open(img_path).convert("RGB")
                h = imagehash.phash(img)  # 또는 imagehash.dhash(img)
                hashes.append(h)
                filenames.append(img_path)
            except Exception as e:
                print(f"[오류] {fname} 처리 중 문제 발생: {e}")
    return hashes, filenames

# 유사 이미지 그룹핑 및 이동
def group_near_identical_images(folder, output_dir, max_distance=3):
    print("🔍 이미지 해시 계산 중...")
    hashes, filenames = get_image_hashes(folder)

    used = [False] * len(filenames)
    group_id = 1
    moved_count = 0

    for i in range(len(filenames)):
        if used[i]:
            continue
        group = [i]
        used[i] = True

        for j in range(i+1, len(filenames)):
            if not used[j]:
                dist = hashes[i] - hashes[j]
                if dist <= max_distance:
                    group.append(j)
                    used[j] = True

        if len(group) > 1:
            group_folder = os.path.join(output_dir, f"유사{group_id}")
            os.makedirs(group_folder, exist_ok=True)

            for idx, g in enumerate(group):
                ext = os.path.splitext(filenames[g])[1]
                new_name = f"유사{group_id}_{idx+1}{ext}"
                dest_path = os.path.join(group_folder, new_name)

                # 이미지 이동 (원본 폴더에서 제거됨)
                shutil.move(filenames[g], dest_path)
                moved_count += 1

            print(f"📦 그룹 유사{group_id} -> {len(group)}개 이동 완료")
            group_id += 1

    print(f"\n✅ 완료: 총 {group_id - 1}개 그룹, {moved_count}개 이미지 이동됨.")
    print(f"📁 확인 경로: {output_dir}")

# 경로 설정 (원하는 경로로 수정)
input_folder = "input_images"             # 원본 이미지 폴더
output_folder = "grouped_duplicates"      # 유사 이미지 그룹 폴더
max_hash_distance = 3                     # 유사도 기준 (0~3 추천)

# 실행
if __name__ == "__main__":
    os.makedirs(output_folder, exist_ok=True)
    group_near_identical_images(input_folder, output_folder, max_distance=max_hash_distance)
