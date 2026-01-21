#!/bin/bash

echo "🎯 Auto-trigger GitHub Actions Workflow"
echo "========================================"
echo ""

# Make test.py executable
chmod +x test.py

# Run the Python script
python3 test.py

echo ""
echo "🔗 View workflow run at:"
echo "   https://github.com/NguyendaiAI-pixta/demo_git_action/actions"
