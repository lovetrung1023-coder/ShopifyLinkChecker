# GitHub Authentication Solutions

## Problem
Windows Credential Manager has cached `DucTrung3110` credentials, preventing push as `lovetrung1023-coder`.

## Quick Solutions

### Solution 1: Clear Cached Credentials (Recommended)
Open Command Prompt or PowerShell as Administrator:
```powershell
# Remove cached GitHub credentials
cmdkey /delete:git:https://github.com
```

Then try push again:
```bash
git push origin main
```
Windows will prompt for new credentials - enter `lovetrung1023-coder` credentials.

### Solution 2: Use Personal Access Token (Fastest)
1. Go to GitHub: Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token with `repo` scope
3. Copy the token
4. Push with token:
```bash
git push https://YOUR_TOKEN@github.com/lovetrung1023-coder/ShopifyLinkChecker.git main
```

### Solution 3: Change Remote URL to Use SSH
```bash
git remote set-url origin git@github.com:lovetrung1023-coder/ShopifyLinkChecker.git
git push origin main
```
(Requires SSH key setup)

### Solution 4: Amend Commit Author (If needed)
If commit author needs to be changed:
```bash
git commit --amend --author="lovetrung1023-coder <lovetrung1023@gmail.com>" --no-edit
git push origin main
```

## Current Status
- ✅ Code committed (hash: 0a3ee01)
- ✅ Git config updated
- ❌ Push blocked by cached credentials

## What's in the Commit
- Shuffle-based rotation mechanism
- 50 new About Us templates
- Total: 66 templates (60 About Us + 6 Shipping Policy)
