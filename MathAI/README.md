# 프로젝트 소개

## 프로젝트 명: MathAI

### 슬로건
MNOP : Math와 Programming 사이 NO-Problem!

### 프로젝트 소개
- 인공지능을 이용하여 수학 문제를 자체 AI 모델을 통해 전처리
- 풀이과정과 답을 파이썬 코드로 제공

![기능](https://github.com/hwbest403/Portfolio/assets/81586177/7d882e14-1da5-4701-8340-7d15b9ea0213)

### 프로젝트 설명
- 파이썬 결과 도출 과정 Pipeline
  - 1) 모델학습
    - 데이터 전처리
      - 입출력 데이터
        - input: 전처리된 수학 문제 데이터
        - output : binary expression tree 구조의 풀이
          - ![학습과정_다시](https://github.com/hwbest403/Portfolio/assets/81586177/76037b51-9c87-4799-8666-d275d1d238f0)
  - 2) 함수식 추론 및 후처리
    - tree구조에서 유형분석, 함수식 추론 및 후처리
      - ![추론과정_다시 (1)](https://github.com/hwbest403/Portfolio/assets/81586177/6420be10-b395-4f8c-8715-58d50a10025c)
    - 유형분석모델성능
      - ![유형분석모델성능_다시](https://github.com/hwbest403/Portfolio/assets/81586177/514908c5-298f-4894-a7e0-9cd3c2f7bcec)
  - 3) 결과
    - 후처리된 데이터를 통해 최종 결과 도출
    - ![풀이예측과정_다시](https://github.com/hwbest403/Portfolio/assets/81586177/602ca663-5593-4da3-bb47-39b89fb8b969)
    - ![풀이생성과정_다시](https://github.com/hwbest403/Portfolio/assets/81586177/b90cc135-3aa1-4610-8786-d0ddb44d8583)
   
### 문제 유형

![문제유형_및_예시](https://github.com/hwbest403/Portfolio/assets/81586177/235cd5b3-9dea-4602-a777-b22f01a4057a)

### 프로젝트 모델
- Graph2Tree 모델
  저희 팀의 모델은 풀이가 사칙연산으로만 이루어져 있는 영어 서술형 수학 문제 데이터셋에 대하여 뛰어난 성능을 보인 Graph2Tree모델을 기반으로 모델을 구축하였습니다.<br><br>
  ![Image](https://github.com/hwbest403/Portfolio/assets/81586177/f972c8f2-6e2f-4189-aaa7-a1102b34864f)
  Graph2Tree 모델은 관계성과 순서정보를 두 개의 그래프, Quantity Cell Graph와 Quantity Comparison Graph를 사용하여 MWP 문제 내의 quantity를효과적으로 표현합니다.<br>
  Quantity Cell Graph는 quantity와문장 내 중요한 단어들을 연관 짓는 그래프, 
  Quantity Comparison Graph는 quantity 간에 관계를 나타내는 그래프입니다.<br>
  또한 그래프 기반의 인코더와 트리 기반의디코더를 활용하여 더 나은 풀이 표현을 생성합니다.<br>
- KoGraph2Tree 모델
  KoGraph2Tree 모델은 기본적인 사칙연산뿐만 아니라 일반적인 서술형 수학 문제에서 사용하는 풀이들을 모두 지원합니다.<br>
  소수점의 이동으로 인한 차이 계산, 원의 넓이 계산, 몇 가지의 숫자로 만들 수 있는 조합/순열 등등 수많은 풀이들에 대하여 학습되어있습니다.<br>
  또한 한국어의 특성에 걸맞게 기존 Graph2Tree가 제시된 논문의 Quantity Cell을 결정하는 방식을 수정하여 한국어에 더 잘 맞는 모델을 구축하였습니다.<br>
  아래는 저희 팀이 구축한 KoGraph2Tree의 모델 구조도 입니다.<br><br>
  ![Image_(1)](https://github.com/hwbest403/Portfolio/assets/81586177/56d7efd0-67c6-4435-b20f-8a7f8be65f37)

# 팀 소개
## 팀명: 수퀴즈~ 예스!

### 팀원 구성
| 역할     | 이름    | 소속         |
|---------|---------|--------------|
| 팀장     | 김동근  |   KoGraph2Tree 모델 구축, 데이터 구축        |
| 팀원     | 이나연  |   KoGraph2Tree 모델 구축 도움, 데이터 구축      |
| 팀원     | 심현우  |   웹 페이지 구축, 데이터 구축          |

### 지도교수 및 멘토
| 역할    | 이름   | 소속      |
|--------|--------|-----------|
| 지도교수 | 구명완 | 서강대학교 |
| 멘토    | 김진범  | 재능교육  |

### Link : http://cscp2.sogang.ac.kr/CSE4187/index.php/MathAI(%EB%A9%94%EC%8E%84%EC%9D%B4)
