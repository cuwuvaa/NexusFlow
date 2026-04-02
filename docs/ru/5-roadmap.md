
# Roadmap

## Цель roadmap

Roadmap нужен для того, чтобы вести разработку NexusFlow **поэтапно, инженерно и контролируемо**.

---

## Этап 1

### Цель
Подготовить инженерную основу проекта.

### Что должно быть сделано

#### Product / Project Setup
- финализация scope MVP
- подготовка docs/
- определение domain-модели
- выбор naming conventions
- базовый backlog

#### Repository / Engineering Setup
- инициализация backend-репозитория
- настройка структуры проекта
- конфигурация окружения
- Docker / Docker Compose
- pre-commit hooks
- линтеры / форматтеры
- базовый CI

#### Backend Core
- FastAPI bootstrap
- config management
- logging
- database connection
- Alembic migrations
- base models / shared abstractions
- error handling strategy

### Результат этапа
К концу этапа должен быть **чистый, готовый к развитию backend skeleton**.

---

## Этап 2 — Auth / Users / Teams

### Цель
Собрать базовую идентичность и организационную структуру продукта.

### Что должно быть сделано

#### Auth
- registration
- login
- JWT access / refresh
- logout
- password hashing
- auth dependencies

#### Users
- user profile
- profile update
- self account endpoint

#### Teams
- create team
- team detail
- invite members
- join flow
- member list

#### Roles
- predefined team roles
- role assignment
- role display in team context

### Результат этапа
К концу этапа пользователь должен уметь:

- зарегистрироваться,
- зайти,
- создать команду,
- пригласить людей,
- организовать команду по ролям.

---

## Этап 3 — Tasks / Chat

### Цель
Собрать основной рабочий контур продукта.

### Что должно быть сделано

#### Tasks
- create task
- edit task
- assign task
- task status lifecycle
- task listing
- filtering basics

#### Chat
- team channels
- send message
- read message history
- basic WebSocket support
- real-time delivery

#### Team Workflow Integration
- связка team → members → tasks → chat
- единая модель доступа

### Результат этапа
К концу этапа команда уже может **реально использовать продукт для координации работы**.

---

## Этап 4 — AI Layer

### Цель
Добавить первый полезный AI-сценарий, встроенный в продукт.

### Что должно быть сделано

#### AI Infrastructure
- AI module scaffold
- provider abstraction
- prompt management
- async job pipeline

#### AI Features
- summarize chat messages
- extract key discussion points
- generate discussion digest
- basic summary persistence

#### Reliability / Cost Control
- retries
- request logging
- token / usage tracking
- fallback handling

### Результат этапа
К концу этапа продукт должен иметь **реально полезный AI feature**, встроенный в основной workflow.

---

## Этап 5 — Hardening

### Цель
Сделать систему более стабильной, чистой и готовой к демонстрации / развитию.

### Что должно быть сделано

#### Backend Hardening
- permission cleanup
- validation hardening
- error contract cleanup
- API consistency pass
- code refactoring

#### Performance / Infra
- Redis usage refinement
- background jobs stabilization
- DB query optimization
- observability basics

#### Testing
- unit tests for services
- integration tests for critical flows
- auth / team / task / chat smoke coverage

#### Documentation
- API docs refinement
- architecture updates
- deployment notes
- onboarding notes

### Результат этапа
К концу этапа проект должен выглядеть как **собранная, инженерно серьёзная MVP-система**, а не как набор фич.

---

## Post-MVP Direction

После завершения MVP и hardening можно переходить к следующим направлениям.

### Candidate Post-MVP Features
- voice / video calls
- board / collaborative canvas
- architecture graph editor
- GitHub integration
- advanced notifications
- analytics / activity insights
- mobile-first clients

---

## Summary

Порядок развития NexusFlow:

1. **Foundation**
2. **Auth / Users / Teams**
3. **Tasks / Chat**
4. **AI**
5. **Hardening**

Это даёт реалистичный путь к сильному MVP без архитектурного распада и без расползания проекта.