#!/usr/bin/env python3
"""
Drift Detection System
Simulates data/model drift monitoring and triggers CI/CD pipeline when drift exceeds threshold
"""
import subprocess
import time
import random
import json
from datetime import datetime

# Configuration
DRIFT_THRESHOLD = 0.3  # Trigger pipeline if drift > 30%
CHECK_INTERVAL = 2     # Check every 2 seconds
MAX_CHECKS = 20        # Maximum number of drift checks

class DriftDetector:
    def __init__(self, threshold=0.3):
        self.threshold = threshold
        self.baseline_mean = 100.0
        self.baseline_std = 15.0
        self.drift_history = []
        
    def calculate_drift(self, current_data):
        """
        Simulate drift calculation using statistical distance
        In real scenario: KL divergence, PSI, Wasserstein distance, etc.
        """
        current_mean = sum(current_data) / len(current_data)
        current_std = (sum((x - current_mean) ** 2 for x in current_data) / len(current_data)) ** 0.5
        
        # Normalized difference (simplified drift metric)
        mean_drift = abs(current_mean - self.baseline_mean) / self.baseline_mean
        std_drift = abs(current_std - self.baseline_std) / self.baseline_std
        
        # Combined drift score
        drift_score = (mean_drift + std_drift) / 2
        return drift_score
    
    def simulate_incoming_data(self, check_number):
        """
        Simulate incoming data stream
        Gradually increase drift over time
        """
        # Start with low drift, gradually increase
        drift_factor = check_number / MAX_CHECKS
        
        data = []
        for _ in range(100):
            # Add noise and drift over time
            value = random.gauss(
                self.baseline_mean + (drift_factor * 50),  # Mean drifts up
                self.baseline_std * (1 + drift_factor)     # Std increases
            )
            data.append(value)
        
        return data

def trigger_cicd_pipeline(drift_score):
    """Trigger GitHub Actions CI/CD pipeline"""
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Create drift report
        report = {
            "timestamp": timestamp,
            "drift_score": round(drift_score, 4),
            "threshold": DRIFT_THRESHOLD,
            "status": "DRIFT_DETECTED",
            "action": "TRIGGER_RETRAINING"
        }
        
        # Save report
        with open('drift_report.json', 'w') as f:
            json.dump(report, f, indent=2)
        
        print("\n📝 Drift report saved to drift_report.json")
        
        # Git commit and push to trigger workflow
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run([
            'git', 'commit', '-m', 
            f'🚨 DRIFT DETECTED: {drift_score:.2%} > {DRIFT_THRESHOLD:.2%} - Auto trigger CI/CD'
        ], check=True)
        subprocess.run(['git', 'push'], check=True)
        
        print("✅ Successfully triggered CI/CD pipeline!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error triggering pipeline: {e}")
        return False

def main():
    print("=" * 70)
    print("� DRIFT DETECTION SYSTEM - Starting Monitoring")
    print("=" * 70)
    print(f"\n⚙️  Configuration:")
    print(f"   - Drift Threshold: {DRIFT_THRESHOLD:.1%}")
    print(f"   - Check Interval: {CHECK_INTERVAL}s")
    print(f"   - Max Checks: {MAX_CHECKS}")
    print(f"\n📊 Baseline Statistics:")
    print(f"   - Mean: {100.0}")
    print(f"   - Std Dev: {15.0}")
    print("\n" + "=" * 70 + "\n")
    
    detector = DriftDetector(threshold=DRIFT_THRESHOLD)
    
    for check_num in range(1, MAX_CHECKS + 1):
        print(f"🔄 Check #{check_num}/{MAX_CHECKS}")
        
        # Simulate incoming data
        current_data = detector.simulate_incoming_data(check_num)
        
        # Calculate drift
        drift_score = detector.calculate_drift(current_data)
        detector.drift_history.append(drift_score)
        
        # Calculate current statistics
        current_mean = sum(current_data) / len(current_data)
        
        # Display drift information
        status = "🟢 NORMAL" if drift_score <= DRIFT_THRESHOLD else "🔴 ALERT"
        print(f"   Drift Score: {drift_score:.4f} ({drift_score:.2%}) - {status}")
        print(f"   Current Mean: {current_mean:.2f} (Baseline: {detector.baseline_mean:.2f})")
        print(f"   Threshold: {DRIFT_THRESHOLD:.2%}")
        
        # Check if drift exceeds threshold
        if drift_score > DRIFT_THRESHOLD:
            print("\n" + "!" * 70)
            print("🚨 DRIFT DETECTED! Drift score exceeds threshold!")
            print("!" * 70)
            print(f"\n📈 Drift Analysis:")
            print(f"   - Current Drift: {drift_score:.2%}")
            print(f"   - Threshold: {DRIFT_THRESHOLD:.2%}")
            print(f"   - Excess: {(drift_score - DRIFT_THRESHOLD):.2%}")
            print(f"\n� Action Required: Triggering CI/CD Pipeline...")
            print("   → Data validation")
            print("   → Model retraining")
            print("   → Model evaluation")
            print("   → Deployment")
            
            # Trigger CI/CD pipeline
            success = trigger_cicd_pipeline(drift_score)
            
            if success:
                print("\n✨ CI/CD Pipeline triggered successfully!")
                print("   Check GitHub Actions: https://github.com/NguyendaiAI-pixta/demo_git_action/actions")
                print("\n📊 Drift History:")
                for i, d in enumerate(detector.drift_history, 1):
                    marker = "🔴" if d > DRIFT_THRESHOLD else "🟢"
                    print(f"   Check {i:2d}: {marker} {d:.2%}")
            else:
                print("\n⚠️  Failed to trigger pipeline. Check git configuration.")
            
            break
        
        print()
        time.sleep(CHECK_INTERVAL)
    
    else:
        print("=" * 70)
        print("✅ Monitoring completed. No significant drift detected.")
        print(f"   Max drift observed: {max(detector.drift_history):.2%}")
        print("=" * 70)

if __name__ == "__main__":
    main()