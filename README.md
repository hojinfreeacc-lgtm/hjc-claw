# HJC CLAW 🦞

> **LLM/API 없이 작동하는 고도화된 로컬 자동화 CLI 에이전트**

HJC CLAW는 외부 API(OpenAI, Claude 등)나 무거운 로컬 LLM을 전혀 사용하지 않고, 오직 파이썬 내장 라이브러리와 자동화 패키지만을 활용하여 PC를 제어합니다. 

---

## ✨ 주요 특징

- **Registry Pattern:** 새로운 도구를 추가할 때 코드를 수정할 필요 없이 등록만 하면 되는 확장성 있는 구조.
- **Decision Engine:** 키워드 가중치와 퍼지 매칭(Fuzzy Matching)을 결합한 지능형 의도 판별.
- **Human-in-the-loop:** 위험한 명령(파일 삭제 등) 실행 전 반드시 사용자 확인 절차 수행.
- **SQLite Memory:** 실행 이력 및 성공 여부를 로컬 데이터베이스에 영구 저장.
- **Global CLI:** 어디서든 `hjc-claw` 명령어로 실행 가능.

---

## 🚀 초간편 설치 방법 (Quick Install)

인증이나 클론 없이 터미널에서 아래 한 줄만 입력하면 즉시 설치됩니다:

```bash
pip install git+https://github.com/hojinfreeacc-lgtm/hjc-claw.git
```

### 🧠 AI 기능 활성화 (Manus 스타일)
AI 기능을 사용하려면 OpenAI API 키를 설정하세요:
```bash
export OPENAI_API_KEY='your-key-here'
# 또는 로컬 Ollama 사용 시
export HJC_USE_OLLAMA='true'
```

설치 후 터미널 어디서든 `hjc-claw`를 입력하여 실행하세요.

---

## 🛠 수동 설치 방법

```bash
# 1. 레포지토리 클론
git clone https://github.com/hojinfreeacc-lgtm/hjc-claw.git
cd hjc-claw

# 2. 패키지 설치
pip install .
```

---

## 🛠 사용 방법

터미널 어디서든 다음 명령어를 입력하세요:

```bash
hjc-claw
```

### 예시 명령어
- `현재 폴더 목록 보여줘`
- `'test.txt' 삭제해줘` (위험 명령 확인 발생)
- `종료` 또는 `exit`

---

## 🏗 아키텍처

1. **`core/registry.py`**: 플러그인 등록 및 관리 시스템.
2. **`core/decision.py`**: 사용자 입력 분석 및 의도(Intent) 판별 엔진.
3. **`core/executor.py`**: 가드레일을 포함한 명령 실행기.
4. **`plugins/`**: 각 자동화 기능이 구현된 모듈형 도구 모음.
5. **`utils/memory.py`**: SQLite 기반 실행 이력 관리.

---

## 🧩 확장 가이드 (새로운 기능 추가)

`src/hjc_claw/plugins/` 디렉토리에 새로운 파일을 만들고 `BasePlugin`을 상속받아 구현하세요.

```python
from .base import BasePlugin
from ..core.registry import PluginMetadata, registry

@registry.register
class MyNewPlugin(BasePlugin):
    def get_metadata(self):
        return PluginMetadata(
            name="my_plugin",
            description="설명",
            intents=[{
                "intent": "my_action",
                "keywords": ["키워드1", "키워드2"],
                "action": "execute_action"
            }]
        )

    def execute_action(self, **kwargs):
        return "실행 결과"
```

---

## ⚖️ 라이선스
MIT License
