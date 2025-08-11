# Instructions to Push to GitHub

## After creating the repository on GitHub, run these commands:

# Navigate to your project directory
cd "d:\BS Data Science\QF2\Quiz_Management-main - Copy"

# The remote is already set, so just push
git push -u origin main

## If you get authentication errors:

1. When prompted for username: enter "Shivam-Shukla0"
2. When prompted for password: DO NOT use your GitHub password
   Instead, use a Personal Access Token:
   
   - Go to: https://github.com/settings/tokens/new
   - Give it a name like "Quiz Management System"
   - Select "repo" scope
   - Generate the token
   - Copy and paste it as your password

## Alternative: Using SSH (if you prefer)

# Generate SSH key (if you don't have one)
ssh-keygen -t ed25519 -C "your-email@example.com"

# Add SSH key to GitHub
# Copy the public key content and add it to GitHub Settings > SSH Keys

# Change remote to SSH
git remote set-url origin git@github.com:Shivam-Shukla0/ai-quiz-management-system.git

# Then push
git push -u origin main

## Your project includes:
- ✅ 40 files ready to upload
- ✅ Complete documentation
- ✅ AI Quiz Generator functionality
- ✅ API key management system
- ✅ Professional README.md
- ✅ Proper .gitignore (excludes sensitive files)
