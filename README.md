<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1f6feb,100:58a6ff&height=180&section=header&text=pete-builds&fontSize=72&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=AI%20tooling%2C%20hardened%20to%20production%20standard&descAlignY=58&descAlign=50" width="100%" />
</div>

<h3 align="center">🔧 I turn ambiguous ops problems into AI tooling, then harden it to a production and supply-chain standard.</h3>

<p align="center"><sub>IT / endpoint engineer (SCCM · Intune · Jamf) building safe AI ops tooling: MCP servers, Claude Code agents, and the verified pipeline that ships them.</sub></p>

<br/>

### Tools I Use

<p align="center">
  <a href="https://modelcontextprotocol.io"><img src="https://img.shields.io/badge/MCP-Model_Context_Protocol-1f6feb?style=for-the-badge&logoColor=white" alt="MCP" /></a>
  <a href="https://claude.com/claude-code"><img src="https://img.shields.io/badge/Claude_Code-D97757?style=for-the-badge&logo=anthropic&logoColor=white" alt="Claude Code" /></a>
</p>

<p align="center">
  <a href="https://python.org"><img src="https://skillicons.dev/icons?i=python" alt="Python" /></a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript"><img src="https://skillicons.dev/icons?i=js" alt="JavaScript" /></a>
  <a href="https://typescriptlang.org"><img src="https://skillicons.dev/icons?i=ts" alt="TypeScript" /></a>
  <a href="https://astro.build"><img src="https://skillicons.dev/icons?i=astro" alt="Astro" /></a>
  <a href="https://docker.com"><img src="https://skillicons.dev/icons?i=docker" alt="Docker" /></a>
  <a href="https://kernel.org"><img src="https://skillicons.dev/icons?i=linux" alt="Linux" /></a>
  <a href="https://git-scm.com"><img src="https://skillicons.dev/icons?i=git" alt="Git" /></a>
  <a href="https://gnu.org/software/bash/"><img src="https://skillicons.dev/icons?i=bash" alt="Bash" /></a>
  <a href="https://sqlite.org"><img src="https://skillicons.dev/icons?i=sqlite" alt="SQLite" /></a>
  <a href="https://nginx.org"><img src="https://skillicons.dev/icons?i=nginx" alt="Nginx" /></a>
  <a href="https://code.visualstudio.com"><img src="https://skillicons.dev/icons?i=vscode" alt="VS Code" /></a>
</p>

---

### 🔒 How these ship

Every service runs as a multi-arch GHCR image carrying a **cosign keyless build-provenance attestation**, deployed through a GitOps pipeline with a **fail-closed verify gate** that rejects unsigned, tampered, and wrong-repo images, plus version-controlled, revertible desired-state.

---

### 🚀 Production-grade

| Project | What it does | Hardening |
|---|---|---|
| [mcp-unifi](https://github.com/pete-builds/mcp-unifi) | Safety-first MCP for self-hosted UniFi. 58 tools across Network/Protect/Access | dry-run previews, JSONL audit log, composite rollback, cosign-attested releases |
| [open-setlist-stash](https://github.com/pete-builds/open-setlist-stash) | Setlist prediction game on a live MCP data feed | Postgres/asyncpg, mypy-strict, Trivy image scan, 167 tests, hash-locked builds |
| [mcp-phish](https://github.com/pete-builds/mcp-phish) | Phish.net / Phish.in MCP, phased vault/live/cache | hash-locked supply chain, 80% coverage gate, dual Trivy scans |
| [phantom-paste](https://github.com/pete-builds/phantom-paste) | Zero-knowledge ephemeral pastebin (Go) | client-side crypto, SRI-pinned deps, XSS + burn-after-read hardened |
| [mcp-threatintel](https://github.com/pete-builds/mcp-threatintel) | Threat-intel MCP: IOC lookups, CVE checks, breach data, OTX pulses | non-root container, thread-safe store, optional bearer auth, tested |
| [strava-mcp-vault](https://github.com/pete-builds/strava-mcp-vault) ⭐12 | Strava MCP with SQLite cache + auto token refresh | Fernet encryption-at-rest, pure-ASGI bearer auth |

---

### 🧪 Also building (experimental, labeled honestly)

[mcp-searxng](https://github.com/pete-builds/mcp-searxng) SSRF-guarded web search · [open-model-arena](https://github.com/pete-builds/open-model-arena) blind LLM ELO arena · [mcp-spotify](https://github.com/pete-builds/mcp-spotify) · [anthropic-tracker-mcp](https://github.com/pete-builds/anthropic-tracker-mcp) · [claude-code-statusline](https://github.com/pete-builds/claude-code-statusline) · [ai-upskill-playbook](https://github.com/pete-builds/ai-upskill-playbook) the 2026 AI stack for IT pros

---

### 📝 Writing

[research-reports](https://github.com/pete-builds/research-reports) · [security-research-reports](https://github.com/pete-builds/security-research-reports) · [stack.brooksnewmedia.com](https://stack.brooksnewmedia.com)

---

### 📈 Contribution Activity

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=pete-builds&theme=github-compact&hide_border=true" width="100%" />
</p>
