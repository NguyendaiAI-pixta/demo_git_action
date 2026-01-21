# 🔍 Drift Detection & ML CI/CD Pipeline

Automated drift detection system that triggers ML model retraining pipeline when data/model drift exceeds threshold.

## 🎯 System Overview

```
┌─────────────────┐      ┌──────────────┐      ┌─────────────────┐
│ Drift Detection │ ───> │ Threshold    │ ───> │ CI/CD Pipeline  │
│  (Monitor Data) │      │ Check (>30%) │      │  (Retrain+Deploy)│
└─────────────────┘      └──────────────┘      └─────────────────┘
```

## 📋 Features

- ✅ **Drift Detection**: Monitors data distribution changes
- ✅ **Automatic Triggering**: Auto-triggers CI/CD when drift > threshold
- ✅ **Complete ML Pipeline**:
  - Data validation
  - Data processing (ETL)
  - Model training
  - Model evaluation
  - Deployment (Staging → Production)
  - Monitoring setup

## ⚙️ Configuration

### Drift Detection Parameters

```python
DRIFT_THRESHOLD = 0.3    # Trigger if drift > 30%
CHECK_INTERVAL = 2       # Check every 2 seconds
MAX_CHECKS = 20          # Maximum number of checks
```

### Baseline Statistics

- **Mean**: 100.0
- **Standard Deviation**: 15.0

## 🚀 Usage

### Run Drift Detection

```bash
# Method 1: Direct Python execution
python3 test.py

# Method 2: Using bash script
chmod +x run_and_trigger.sh
./run_and_trigger.sh
```

### Output Example

```
══════════════════════════════════════════════════════════════════
🔍 DRIFT DETECTION SYSTEM - Starting Monitoring
══════════════════════════════════════════════════════════════════

⚙️  Configuration:
   - Drift Threshold: 30.0%
   - Check Interval: 2s
   - Max Checks: 20

📊 Baseline Statistics:
   - Mean: 100.0
   - Std Dev: 15.0

🔄 Check #1/20
   Drift Score: 0.0234 (2.34%) - 🟢 NORMAL
   Current Mean: 102.34 (Baseline: 100.00)
   Threshold: 30.0%

🔄 Check #8/20
   Drift Score: 0.3421 (34.21%) - 🔴 ALERT

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
🚨 DRIFT DETECTED! Drift score exceeds threshold!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

🔧 Action Required: Triggering CI/CD Pipeline...
   → Data validation
   → Model retraining
   → Model evaluation
   → Deployment

✨ CI/CD Pipeline triggered successfully!
```

## 📊 CI/CD Pipeline Stages

### 1. 📊 Drift Analysis
- Read drift report
- Analyze drift metrics

### 2. 🔍 Data Validation
- Schema validation
- Data type checks
- Missing value detection
- Outlier detection

### 3. 🔄 Data Pipeline
- **Extract**: From DB, APIs, S3
- **Transform**: Cleaning, feature engineering
- **Load**: Train/Val/Test split (70/15/15)

### 4. 🤖 Model Training
- Train new model
- Hyperparameter tuning
- Performance evaluation
  - Accuracy: ~93%
  - Precision: ~91%
  - Recall: ~93%
  - F1-Score: ~92%

### 5. 🚀 Deployment
- Build Docker container
- Deploy to staging
- Run integration tests
- Blue-green deployment to production

### 6. 📡 Monitoring
- Configure drift detection
- Setup performance metrics
- Create dashboards

## 📁 Generated Files

### drift_report.json
```json
{
  "timestamp": "2026-01-21 10:30:45",
  "drift_score": 0.3421,
  "threshold": 0.3,
  "status": "DRIFT_DETECTED",
  "action": "TRIGGER_RETRAINING"
}
```

## 🔧 How It Works

1. **Monitoring Phase**:
   - Script continuously monitors incoming data
   - Calculates drift score using statistical metrics
   - Compares against baseline distribution

2. **Detection Phase**:
   - When drift > 30%, system triggers alert
   - Creates drift report
   - Commits changes to git

3. **CI/CD Phase**:
   - Git push triggers GitHub Actions
   - Pipeline validates data
   - Retrains model with new data
   - Deploys updated model

4. **Production Phase**:
   - New model serves predictions
   - Monitoring continues for next drift

## 📈 Drift Calculation

```python
# Simplified drift metric
mean_drift = abs(current_mean - baseline_mean) / baseline_mean
std_drift = abs(current_std - baseline_std) / baseline_std
drift_score = (mean_drift + std_drift) / 2
```

Real-world alternatives:
- **PSI** (Population Stability Index)
- **KL Divergence** (Kullback-Leibler)
- **Wasserstein Distance**
- **Kolmogorov-Smirnov Test**

## 🌐 View Pipeline

After drift detection:
- **GitHub Actions**: https://github.com/NguyendaiAI-pixta/demo_git_action/actions
- **Workflow Runs**: Check latest run for detailed logs

## 🎓 Educational Value

This simulation demonstrates:
- ✅ ML monitoring best practices
- ✅ Automated MLOps workflows
- ✅ CI/CD for ML models
- ✅ Drift detection strategies
- ✅ Continuous model improvement

## 📝 Notes

- This is a **simulation** for educational purposes
- In production, use tools like:
  - **Evidently AI** for drift detection
  - **MLflow** for model tracking
  - **Kubeflow** for ML pipelines
  - **Airflow** for orchestration

## 🔗 Resources

- [Evidently AI](https://www.evidentlyai.com/)
- [MLflow](https://mlflow.org/)
- [GitHub Actions](https://docs.github.com/en/actions)
