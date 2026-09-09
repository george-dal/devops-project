# Military Service Application - DevOps Project

Αυτή η εφαρμογή αποτελεί ένα ολοκληρωμένο έργο DevOps για την αυτοματοποιημένη ανάπτυξη (deployment) και δοκιμή (testing) της εφαρμογής "Military Service".

##  Αρχιτεκτονική & Τεχνολογίες
- **Backend Framework:** Python FastAPI
- **Database:** PostgreSQL 15
- **Authentication:** Keycloak 24
- **Email Service:** MailHog
- **Containerization:** Docker & Docker Compose (με Healthchecks)
- **CI/CD Pipeline:** GitHub Actions & Pytest
- **Configuration Management / Deployment:** Ansible

---

##  Οδηγίες Τοπικής Εκτέλεσης (Docker)

### 1. Εκκίνηση Υπηρεσιών
```bash
docker compose up -d --build
