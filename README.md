#  Military Service Application - DevOps Project

Αυτή η εφαρμογή αποτελεί ένα ολοκληρωμένο έργο DevOps για την αυτοματοποιημένη ανάπτυξη (deployment) και δοκιμή (testing) της εφαρμογής "Military Service".

##  Αρχιτεκτονική & Τεχνολογίες
- **Backend Framework:** Python FastAPI
- **Database:** PostgreSQL 15
- **Authentication:** Keycloak 24
- **Email Service:** MailHog
- **Containerization:** Docker & Docker Compose (με Healthchecks)
- **CI/CD Pipeline:** GitHub Actions & Jenkins
- **Automated Testing:** Pytest
- **Configuration Management / Deployment:** Ansible
- **Kubernetes Support:** Manifests για MicroK8s

---

##  Οδηγίες Τοπικής Εκτέλεσης (Docker)

### 1. Εκκίνηση Υπηρεσιών
```bash
docker compose up -d --build
```

### 2. Έλεγχος Κατάστασης (Health Status)
```bash
docker compose ps
```

##  Εκτέλεση Automated Tests (Pytest)
```bash
cd app
python -m pytest
```
##  Deployment μέσω Ansible
```bash
ansible-playbook -i inventory.ini deploy.yml
```