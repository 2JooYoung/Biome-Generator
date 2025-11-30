# Biome Generator
Maya 스크립트를 이용해 빠르게 다양한 배경(바이옴)을 자동 생성할 수 있는 툴

---

## Overview
Biome Generator는 게임 또는 애니메이션 제작 시 반복적으로 배경을 만들어야 하는 시간을 줄이기 위해 제작된 자동화 도구입니다.  
사용자는 지형(Terrain), 나무(Trees), 돌(Rocks), 계절/날씨를 선택하여 즉석에서 다양한 환경을 생성할 수 있습니다.

---

## Features

### Terrain (지형 생성)
- Flat: 평평한 지형  
- Mountain: 울퉁불퉁한 산악 지형  
- Generate 버튼 클릭 시 즉시 생성  
- 계절별 자동 색상 적용  
  - 봄: 연두색  
  - 여름: 진초록  
  - 가을: 갈색  
  - 겨울: 흰색  

---

### Trees (나무 생성)
계절 선택에 따라 서로 다른 형태의 나무가 생성됩니다.

- 봄 / 여름 → 잎이 무성한 나무  
- 가을 → 두 종류의 나무가 섞여 생성  
- 겨울 → 잎이 모두 떨어진 나무  

---

### Rocks (돌 생성)
- 슬라이드바로 생성할 돌의 개수 조절  
- 다양한 크기와 위치로 자연스럽게 배치  

---

### Season & Weather
- **봄 / 여름 / 가을 / 겨울** 중 선택  
- 선택된 계절에 따라 지형과 오브젝트의 색조가 자동 변경  

---

## User Interface
UI는 다음 요소들로 구성되어 있습니다:

- Terrain 탭  
- Trees 탭  
- Rocks 탭  
- Season / Weather 선택  

---

## How It Works

### 1. UI 실행
스크립트를 실행하면 Biome Generator 창이 나타납니다.
<img width="933" height="581" alt="image" src="https://github.com/user-attachments/assets/3f59d847-6971-4893-bd96-622257644c78" />

### 2. 옵션 선택
- 계절 선택  
- 지형 선택  
- 나무/돌 개수 조절  

### 3. Generate 버튼 클릭
→ 선택한 설정에 따라 지형 + 오브젝트가 자동 생성됩니다.  
→ Maya 씬에서 바로 렌더링·수정 가능  

---

## Examples

### ▪ Winter + Flat + Trees 17  
<img width="940" height="468" alt="image" src="https://github.com/user-attachments/assets/aa87dd4f-36db-41a0-9a9d-7d215e3b8d63" />


### ▪ Summer + Mountain + Trees 2  
<img width="940" height="628" alt="image" src="https://github.com/user-attachments/assets/7fe9dd68-e231-4fb8-a6d6-5c3dc2108381" />


### ▪ Autumn + Flat + Trees 29  
<img width="940" height="549" alt="image" src="https://github.com/user-attachments/assets/dcaf0339-e886-4d67-b2b8-767605e00ebb" />


---

## 💡 Use Cases
Biome Generator는 다음과 같은 작업에 활용될 수 있습니다:

- 게임 배경 자동 생성
- 애니메이션 배경 구축 시간 단축
- 렌더링용 배경 이미지 생성 
- 프로토타입 환경 셋업

---
