# 심전도 데이터 기반 심장 질환 진단 모델링

> Period: 2021.12 ~ 2022.01

##### 23.02.14 last edit
---

## 0. Environment

+ Language : Python

---
## 1. Introduction

**Background**

사망률이 높은 질환이 심장 질환은 조기 진단이 중요함. 디지털 의료기기의 심전도 데이터를 활용하여 보다 정확하고 빠른 심장 질환을 진단하는 모델을 개발하고자 함.

---
## 2. Data Set

**Dataset Info.**

Data Source: Physionet's PTB Diagnostic Database


https://www.physionet.org/content/ptbdb/1.0.0/

<br/>


**File count**

14,550 samples


---
## 3. Summary

**(1) 과정**

- 데이터 수집 (14,550 samples)

- 시각화 및 전처리 진행 (one hot encoding)

- 딥러닝 모델 적용 후 비교

<br/>


**(2) Result**

- 모델 선정 및 93% 이상의 정확도
- Confusion Matrix 생성
- 환자의 심전도 패턴 분석 