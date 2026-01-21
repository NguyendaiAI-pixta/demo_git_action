#!/usr/bin/env python3
import subprocess
import time

def trigger_github_workflow():
    """Trigger GitHub Actions workflow by making a git commit and push"""
    try:
        # Stage all changes
        subprocess.run(['git', 'add', '.'], check=True)
        
        # Commit with message
        subprocess.run(['git', 'commit', '-m', 'Auto trigger: Count reached 20'], check=True)
        
        # Push to GitHub
        subprocess.run(['git', 'push'], check=True)
        
        print("✅ Successfully triggered GitHub Actions workflow!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error triggering workflow: {e}")
        return False

def main():
    print("🚀 Starting count to 20...")
    
    # Count from 1 to 20
    for i in range(1, 21):
        print(f"Count: {i}")
        time.sleep(0.5)  # Wait 0.5 seconds between counts
    
    print("\n🎯 Reached 20!")
    print("📡 Triggering GitHub Actions workflow...")
    
    # Trigger the workflow
    success = trigger_github_workflow()
    
    if success:
        print("\n✨ Check your GitHub repository for the workflow run!")
        print("   The workflow will subtract two numbers: 100 - 42 = 58")
    else:
        print("\n⚠️  Failed to trigger workflow. Please check your git configuration.")

if __name__ == "__main__":
    main()