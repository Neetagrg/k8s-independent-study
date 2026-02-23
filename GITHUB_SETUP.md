# GitHub Setup Guide

## 📋 Complete GitHub Setup Instructions

---

## Step 1: Create GitHub Repository

1. **Go to GitHub:** https://github.com
2. **Click "New"** (green button) or **"+" → "New repository"**
3. **Repository Settings:**
   ```
   Repository name: k8s-independent-study
   Description: Resilient Kubernetes-Based CI/CD Deployment - Spring 2026
   Visibility: ✅ Public
   Initialize: ❌ DO NOT check any boxes
   ```
4. **Click "Create repository"**

---

## Step 2: Organize Your Files

### Current Structure (from zip):
```
Neeta_Misericordia_K8s_Weeks_1-4/
├── app.py
├── Dockerfile
├── requirements.txt
├── PROGRESS_REPORT.md
├── kubernetes/
│   ├── deployment.yaml
│   └── service.yaml
└── screenshots/
```

### Create This New Structure:

```bash
# In your project folder
mkdir -p .github/workflows
mkdir -p docs
mkdir -p tests

# Move files
mv app.py app.py
mv requirements.txt requirements.txt  
mv Dockerfile Dockerfile
mv PROGRESS_REPORT.md docs/week-1-4-report.md
mv screenshots docs/screenshots

# Copy new files from downloads:
# - README.md (new comprehensive version)
# - .gitignore
# - .github/workflows/ci.yml
```

### Final Structure:
```
k8s-independent-study/
├── .github/
│   └── workflows/
│       └── ci.yml
├── kubernetes/
│   ├── deployment.yaml
│   └── service.yaml
├── docs/
│   ├── week-1-4-report.md
│   └── screenshots/
├── tests/
│   └── (empty for now)
├── app.py
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

---

## Step 3: Initialize Git and Push

```bash
# Navigate to your project folder
cd k8s-independent-study

# Initialize git
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: Weeks 1-4 Containerization and Kubernetes deployment"

# Add GitHub remote (replace YOUR-USERNAME)
git remote add origin https://github.com/YOUR-USERNAME/k8s-independent-study.git

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main
```

---

## Step 4: Set Up GitHub Secrets (for CI/CD)

For Week 5-8, you'll need Docker Hub credentials:

### 4a. Create Docker Hub Account

1. Go to https://hub.docker.com
2. Sign up (free account)
3. Remember your username

### 4b. Create Docker Hub Access Token

1. Login to Docker Hub
2. Click your **profile icon** → **Account Settings**
3. Go to **Security** → **New Access Token**
4. Name: `github-actions-ci`
5. Permissions: **Read, Write, Delete**
6. **Copy the token** (you won't see it again!)

### 4c. Add Secrets to GitHub

1. Go to your GitHub repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**

**Add two secrets:**

**Secret 1:**
```
Name: DOCKER_HUB_USERNAME
Secret: your-dockerhub-username
```

**Secret 2:**
```
Name: DOCKER_HUB_TOKEN
Secret: paste-your-access-token-here
```

---

## Step 5: Verify Everything Works

### Check Repository
```bash
# Visit your repo
https://github.com/YOUR-USERNAME/k8s-independent-study

# You should see:
✅ README.md displayed
✅ All folders and files
✅ Nice badges and formatting
```

### Test CI/CD (Week 5-8)
```bash
# Make a small change
echo "# Test" >> README.md

# Commit and push
git add README.md
git commit -m "test: Trigger CI pipeline"
git push

# Go to GitHub → Actions tab
# You should see your workflow running!
```

---

## Step 6: Share with Professor

### Option A: Email
```
Subject: Independent Study - GitHub Repository Link

Dear Professor [Name],

I have uploaded my independent study project to GitHub:

Repository: https://github.com/YOUR-USERNAME/k8s-independent-study

Current Status:
✅ Week 1-4: Complete (Containerization & Kubernetes)
🔄 Week 5-8: In Progress (CI/CD Pipeline)

The repository includes:
- Complete source code
- Kubernetes manifests
- Progress reports in /docs
- Automated CI/CD pipeline (GitHub Actions)

Best regards,
Neeta Misericordia
```

### Option B: Update Progress Report

Add to `docs/week-1-4-report.md`:
```markdown
## GitHub Repository

Project code is available at:
https://github.com/YOUR-USERNAME/k8s-independent-study
```

---

## 🔧 Common Git Commands for This Project

### Daily Workflow
```bash
# Check status
git status

# Add new/changed files
git add .

# Commit changes
git commit -m "feat: Add new feature"

# Push to GitHub
git push
```

### Commit Message Format
```bash
# Use conventional commits:
git commit -m "feat: Add Prometheus monitoring"
git commit -m "fix: Correct deployment replica count"
git commit -m "docs: Update week 5-8 report"
git commit -m "test: Add unit tests for /health endpoint"
```

### View History
```bash
# See commits
git log --oneline

# See changes
git diff
```

---

## 📊 GitHub Actions Workflow Explanation

The `.github/workflows/ci.yml` file does:

1. **Triggers:** Runs on every push to `main` branch
2. **Build:** Creates Docker image
3. **Test:** Checks health endpoints
4. **Push:** Uploads to Docker Hub (on main branch only)

### View Workflow Status
```
GitHub Repo → Actions tab → See all runs
```

---

## ✅ Verification Checklist

Before submitting Week 5-8:

- [ ] GitHub repository created
- [ ] All Week 1-4 files pushed
- [ ] README.md looks professional
- [ ] Docker Hub account created
- [ ] GitHub secrets configured
- [ ] CI/CD workflow file added
- [ ] First workflow run successful
- [ ] Repository link shared with professor

---

## 🆘 Troubleshooting

### Can't push to GitHub
```bash
# Check remote
git remote -v

# Should show:
origin  https://github.com/YOUR-USERNAME/k8s-independent-study.git (fetch)
origin  https://github.com/YOUR-USERNAME/k8s-independent-study.git (push)

# If wrong, fix it:
git remote remove origin
git remote add origin https://github.com/YOUR-USERNAME/k8s-independent-study.git
```

### CI/CD workflow failing
1. Check **Actions** tab on GitHub
2. Click failed run
3. Read error messages
4. Common issues:
   - Missing Docker Hub secrets
   - Wrong username/token
   - App.py syntax errors

### Large files rejected
```bash
# Add to .gitignore
echo "screenshots/*.png" >> .gitignore
git rm --cached screenshots/*.png
git commit -m "fix: Remove large screenshots"
```

---

## 📚 Next Steps (Week 5-8)

1. ✅ Push Week 1-4 code to GitHub
2. ✅ Set up Docker Hub account
3. ✅ Configure GitHub secrets
4. ✅ Add CI/CD workflow
5. 🔄 Test automated builds
6. 🔄 Write Week 5-8 report
7. ⏳ Submit by March 14, 2026

---

**Questions? Check GitHub Docs:** https://docs.github.com
