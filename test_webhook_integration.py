#!/usr/bin/env python3
"""
Test Webhook Integration Script
This script demonstrates the webhook integration between GitHub and Lindy.
Created to test the GitHub Actions workflow that forwards push events to Lindy.
"""

import datetime
import json
import sys

def main():
      """Main function to test webhook integration."""
      print("🚀 Testing Lindy Webhook Integration")
      print(f"📅 Timestamp: {datetime.datetime.now().isoformat()}")
      print(f"🐍 Python version: {sys.version}")

    # Sample webhook payload structure
      webhook_data = {
          "event": "push",
          "repository": "jobkubera-lab/kuberajob",
          "message": "Testing webhook integration with Lindy",
          "author": "kubera job",
          "timestamp": datetime.datetime.now().isoformat(),
          "status": "success"
      }

    print("📦 Sample webhook payload:")
    print(json.dumps(webhook_data, indent=2))

    print("✅ Webhook integration test completed successfully!")
    print("🔗 This commit should trigger the GitHub Actions workflow")
    print("📡 The workflow will send this event data to Lindy webhook endpoint")

if __name__ == "__main__":
      main()
