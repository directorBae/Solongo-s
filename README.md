# Solongo!s 백엔드 코드

## 협업 시 주의사항

1. 업데이트 사항을 Readme에 업데이트하고 커밋 및 푸시합니다(혹은 노션을 이용해 업데이트 사항을 구체적으로 명시합니다.)
2. Git Branch 정책을 잘 수립하여 그 정책을 통해 협업을 진행하도록 합니다.

## 브랜치 정책

[Git 브랜치 정책 정리](https://inpa.tistory.com/entry/GIT-%E2%9A%A1%EF%B8%8F-github-flow-git-flow-%F0%9F%93%88-%EB%B8%8C%EB%9E%9C%EC%B9%98-%EC%A0%84%EB%9E%B5)

- 우리는 위 링크 중에서 GITHUB-FLOW를 따르기로 합니다.

1. main 브랜치는 모든 개발 사항이 추후 merge되는 브랜치입니다. 각자 개발이 끝나고, **자신이 개발한 부분에 대해 개발이 완료되면 과업 진행 중인 브랜치를 main 브랜치에 PR하도록 합니다.**
2. 새로운 브랜치는 항상 main 브랜치에서 만들어집니다. 버전관리가 명확하지 않기 때문에, 자신의 과업을 노션을 통해 확인하고 잘 업데이트합니다. **자신의 과업을 바탕으로 브랜치 이름을 작성하여 어떤 브랜치가 어떤 신규 개발 사항이 있는지 알기 쉽도록 하는 것이 좋습니다.**
3. Readme 파일 혹은 노션 업데이트를 잘 진행하도록 합니다. README 파일에 공간을 만들어둘 것이니, **자신의 과업 진행 내용을 날짜와 간략한 내용에 맞게** 작성합니다.
4. **PR이 발생하면 그 PR을 처리하는 Merge 회의까지 각자 코드리뷰를 알아서 해오고 토의합니다.** 더불어 각 PR 지점들을 과업표에 맞게 잘 만들어야 합니다.
   (6/15-16 회의가 예정되어 있습니다. 이때 PR 주기를 이야기해보도록 합니다.)
5. PR에서 문제가 발견되지 않으면, main 브랜치로 merge합니다.

## Memo

- 개인적으로 PR 주기는 매주 과업을 진행하고, 매주 주말이나 PR할게 많이 쌓이면 2주마다 진행하는 게 좋을 것 같습니다.
- 과하게 PR 주기가 길어지면, 서로가 서로의 코드에 대해 익숙하지 않아 코드가 섞일 수 있으므로 비슷한 영역을 코딩할 경우 PR과 관계없이 깃허브에 접속하여 상대방의 코드를 참고하여 코딩하는 것이 좋을 것 같습니다.

## R&R 분배

> 백엔드 단에서의 과업 분배를 정해봅시다.

- 배정원

  - [ ] routes 디렉토리. 프론트엔드와 직접적으로 통신하는 엔드포인트.
  - [ ] models 디렉토리. Agent Model을 다룰 때 사용. ChatGPT 모델을 활용한 Agent 모델 개발.

- 조성운
  - [ ] db 디렉토리 및 db. SQLite3와 SQL-Alchemy를 활용한 데이터베이스 운용 및 관리.
  - [ ] utils 디렉토리. TourAPI 및 KakaoAPI, 기타 모듈 관리. 이 부분은 배정원 과업에 따라 배정원도 개발에 참여할 수 있음.

## 개발노트

> 개발 사항에 대한 노트테이킹입니다.
> **기본적으로 표 안에 과업을 입력하고, 과업에 대한 간략한 내용을 작성학세요.**
> 자세한 내용은 toggle을 만들어 그 안에 작성바랍니다.

<details>
  <summary>Toggle 만드는 법</summary>
  HTML 태그를 사용하여 마크다운에서 토글을 만들 수 있습니다.
  아래와 같이 작성합니다.

```HTML
<details>
<summary>토글 제목</summary>
  숨겨진 내용입니다. 여기에 원하는 텍스트를 추가할 수 있습니다.
  - 항목 1
  - 항목 2
</details>
```

</details>

---

아래 표는 개발이나 PR 시 main에도 merge해야 하는 개발 진행표입니다.
각자 과업 단위가 끝나면 아래 표에 마크다운 문법을 맞추어서 각자 브랜치에 커밋 후 푸시합니다.

- 날짜는 과업 종료 날짜(커밋 날짜)를 나타냅니다.
- 브랜치명은 현재 작업 중인 브랜치를 나타냅니다.
- 작업 내용 요약은 20자 이내로 간결하게 작성하도록 합니다.
  - 해당 브랜치 및 과업 전체의 설명과도 같습니다.
  - 이때 더 설명할 부분이 있다면 토글을 표 아래쪽에 만들어 마크다운을 작성합니다.
- merge 여부는 해당 브랜치가 현재 main에 merge되어있는지 나타내는 것입니다.
  - PR 회의 중간중간에 진행하도록 합니다.

| 날짜     | 브랜치명 | 작업 내용 요약              | merge 여부 |
| :------- | :------: | --------------------------- | :--------: |
| 24.06.13 |   main   | 첫 커밋, 스켈레톤 코드 작성 |     O      |
|          |          |                             |            |

---

### 개발노트 Toggles

---
