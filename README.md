# 🦅 HJC CLAW (v1.2.0)

**HJC CLAW**는 로컬 OS 제어, 시스템 자동화, 그리고 강력한 AI 추론 능력을 결합한 **하이브리드 AI 자동화 에이전트**입니다. Open Interpreter의 실행력과 로컬 보안 중심의 설계를 통합하여, 사용자의 PC를 지능적으로 제어합니다.

---

## ✨ 핵심 기능 (Key Features)

- **🧠 Multi-AI Brain:** Google Gemini, OpenAI, 그리고 로컬 Gemma(Ollama)를 지원하여 상황에 맞는 최적의 AI를 선택할 수 있습니다.
- **💻 Dynamic Interpreter:** 정해진 규칙 외의 복잡한 명령은 AI가 즉석에서 파이썬 코드를 생성하고 안전하게 실행합니다.
- **🛡️ Security Auditing:** 포트 스캔, 네트워크 분석, 해시 검증 등 화이트해킹 및 보안 점검 도구를 내장하고 있습니다.
- **🧹 Mole Cleaner:** 프로젝트 내 불필요한 더미 파일(cache, logs, temp)을 탐지하고 제거하여 저장 공간을 최적화합니다.
- **🌐 AI Web Search:** 웹 검색 결과를 AI가 분석하고 요약하여 핵심 정보만 빠르게 전달합니다.
- **🔒 Local First:** 모든 작업은 로컬에서 수행되며, AI 모델 선택에 따라 완전한 오프라인 환경에서도 작동 가능합니다.

---

## 🚀 초간편 설치 (Quick Install)

별도의 클론이나 인증 없이 터미널에서 아래 명령어로 즉시 설치 및 업데이트가 가능합니다:

```bash
pip install --upgrade git+https://github.com/hojinfreeacc-lgtm/hjc-claw.git
```

---

## 🧠 AI 기능 활성화 (AI Setup)

HJC CLAW의 지능형 기능을 사용하려면 원하는 모델의 환경 변수를 설정하세요.

### 1. Google Gemini (권장 - 빠르고 강력함)
```bash
export GOOGLE_API_KEY='your-gemini-api-key'
```

### 2. Local Google Gemma (Ollama - 보안 및 오프라인)
```bash
export HJC_USE_OLLAMA='true'
export HJC_OLLAMA_MODEL='gemma2' # gemma, llama3 등 선택 가능
```

### 3. OpenAI
```bash
export OPENAI_API_KEY='your-openai-api-key'
```

---

## 💻 사용 방법 (Usage)

설치 후 터미널 어디서든 `hjc-claw`를 입력하세요.

### 주요 명령어 예시
- **AI 작업:** "파이썬으로 로또 번호 생성기 만들어서 실행해줘"
- **웹 검색:** "최신 AI 뉴스 검색해서 요약해줘"
- **보안 점검:** "내 PC 포트 스캔해줘", "네트워크 정보 보여줘"
- **시스템 정리:** "run mole cleanup", "더미 파일 분석해줘"
- **파일 관리:** ".txt 파일 모두 찾아서 문서 폴더로 옮겨줘"

---

## 🛠 아키텍처 (Architecture)

1. **Decision Engine:** 규칙 기반 매칭과 AI 추론을 결합한 하이브리드 의사결정 시스템.
2. **Plugin Registry:** 새로운 도구를 쉽게 추가하고 관리할 수 있는 확장형 구조.
3. **Safe Executor:** 위험한 명령 실행 전 사용자 승인을 요청하는 가드레일 시스템.
4. **Context Memory:** 과거 명령과 실행 결과를 기억하여 연속적인 작업 수행 가능.

---

## 🔗 링크 (Links)
- **GitHub:** [https://github.com/hojinfreeacc-lgtm/hjc-claw](https://github.com/hojinfreeacc-lgtm/hjc-claw)
- **License:** MIT License
