#!/bin/bash

# 1. SETUP: Check for GitHub CLI
#if ! command -v gh &> /dev/null; then
 #   echo "❌ Error: GitHub CLI (gh) is not installed."
  #  echo "Please install it from https://cli.github.com/ first."
   # exit 1
#fi

# 2. CREATE FOLDER STRUCTURE
mkdir -p mcp-student-sandbox
cd mcp-student-sandbox

# 3. CREATE THE 4 CHALLENGE FILES
cat <<EOF > spaghetti_logic.py
def process_data(data):
    res = []
    for d in data:
        val = d * 1.15
        s = f"Total: {val:.2f}"
        print(s)
        res.append(val)
    with open("log.txt", "a") as f:
        f.write(str(res) + "\n")
    return res
EOF

cat <<EOF > failing_calculator.py
def average_ratios(numbers):
    total = 0
    for i in range(len(numbers)):
        # BUG: Crashes on zero
        total += 100 / numbers[i] 
    return total / len(numbers)

print(average_ratios([10, 5, 0]))
EOF

cat <<EOF > secret_leak.py
AWS_SECRET_KEY = "AKIA_FAKE_KEY_123456789_STUDENT_TEST"
def connect():
    print(f"Connecting with: {AWS_SECRET_KEY}")
EOF

cat <<EOF > mystery_module.py
import math
def fn_x(a, b, c):
    d = b**2 - 4*a*c
    if d < 0: return None
    return ((-b + math.sqrt(d))/(2*a), (-b - math.sqrt(d))/(2*a))
EOF

# 4. INITIALIZE GIT & GITHUB REPO
git init
git add .
git commit -m "Initial Sandbox Setup"

# This creates a PUBLIC repo with the name of the current folder
gh repo create mcp-student-sandbox --public --source=. --push

echo "✅ Success! Sandbox is live at: $(gh repo view --json url -q .url)"
