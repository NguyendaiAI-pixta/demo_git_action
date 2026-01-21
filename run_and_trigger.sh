#!/bin/bash

echo "══════════════════════════════════════════════════════════════════"
echo "🔍 DRIFT DETECTION & ML CI/CD SYSTEM"
echo "══════════════════════════════════════════════════════════════════"
echo ""
echo "This script will:"
echo "  1. Monitor data distribution for drift"
echo "  2. Detect when drift exceeds 30% threshold"
echo "  3. Automatically trigger ML retraining pipeline"
echo ""
echo "══════════════════════════════════════════════════════════════════"
echo ""

# Make test.py executable
chmod +x test.py

# Run the drift detection script
echo "🚀 Starting drift detection monitoring..."
echo ""
python3 test.py

echo ""
echo "══════════════════════════════════════════════════════════════════"
echo "� Monitoring Session Complete"
echo "══════════════════════════════════════════════════════════════════"
echo ""
echo "🔗 View CI/CD pipeline execution:"
echo "   https://github.com/NguyendaiAI-pixta/demo_git_action/actions"
echo ""
echo "📝 Check drift_report.json for detailed metrics"
echo "══════════════════════════════════════════════════════════════════"
