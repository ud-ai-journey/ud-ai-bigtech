#!/usr/bin/env python3
"""
Day 1: My AWS SageMaker Roadshow Adventure & The Birth of My Big Tech Journey
A simple story in code about an inspiring day that changed my perspective
"""

def aws_sagemaker_adventure():
    """My amazing day at the AWS Agentic AI & SageMaker Roadshow"""
    
    print("🚀 Day 1 Story: AWS SageMaker Roadshow Adventure!")
    print("=" * 60)
    
    # Morning preparation
    delegate_badge = True
    laptop_status = "open"
    curiosity_level = "high"
    
    print(f"✅ Delegate badge: {'ON' if delegate_badge else 'OFF'}")
    print(f"💻 Laptop: {laptop_status}")
    print(f"🧠 Curiosity level: {curiosity_level}")
    
    # What I learned today
    aws_learnings = [
        "Amazon SageMaker's MLOps workflow",
        "New Bedrock agents functionality", 
        "RAG (Retrieval Augmented Generation) pipeline",
        "Open-source OSS models",
        "Cost-optimized fine-tuning techniques"
    ]
    
    print("\n📚 Key Learnings:")
    for i, learning in enumerate(aws_learnings, 1):
        print(f"   {i}. {learning}")
    
    # My lightning talk moment
    print("\n🎤 Lightning Talk Achievement:")
    print("   Topic: Rapid prototyping with Bedrock's RAG pipeline")
    print("   Audience reaction: 🔥 (Fire questions and great engagement!)")
    
    return "Successfully completed AWS roadshow!"

def system_design_breakthrough():
    """The moment I realized I love system design"""
    
    print("\n" + "=" * 60)
    print("💡 BREAKTHROUGH MOMENT: System Design Discovery")
    print("=" * 60)
    
    # Uber rides calculation that impressed the panel
    bangalore_population = 10_000_000  # 10M people
    
    # My system design thinking process
    segments = {
        "age_groups": ["young", "middle_aged", "senior"],
        "work_status": ["working_class", "non_working"],
        "transport_modes": ["uber", "ola", "auto", "bus", "metro"],
        "customer_types": ["paid", "prepaid", "regular", "occasional"]
    }
    
    # Market analysis (based on 2024 research data)
    # Uber holds 40-50% market share in cars in India
    uber_market_share = 0.45  # 45% based on research
    
    # More realistic assumptions for Bangalore
    smartphone_users_ratio = 0.75  # 75% smartphone penetration in urban areas
    ride_hailing_adoption = 0.25    # 25% of smartphone users use ride-hailing
    monthly_rides_per_active_user = 8  # Active users take ~8 rides/month
    
    # Updated calculation approach
    potential_users = bangalore_population * smartphone_users_ratio
    active_users = potential_users * ride_hailing_adoption
    uber_users = active_users * uber_market_share
    estimated_monthly_rides = uber_users * monthly_rides_per_active_user
    
    print(f"🏙️  Bangalore Population: {bangalore_population:,}")
    print(f"📱 Smartphone Users (~75%): {int(potential_users):,}")
    print(f"🚗 Ride-hailing Users (~25%): {int(active_users):,}")
    print(f"🎯 Uber Users (45% share): {int(uber_users):,}")
    print(f"📊 Rides per User/Month: {monthly_rides_per_active_user}")
    print(f"🏆 REALISTIC ESTIMATE: {int(estimated_monthly_rides):,} rides/month")
    
    # Your original calculation for comparison
    print(f"\n📋 Original Method Comparison:")
    original_estimate = bangalore_population * 0.6 * 0.3 * 2
    print(f"   Original estimate: {int(original_estimate):,} rides/month")
    
    print("\n🎉 Panel Reaction: APPLAUDED! 👏")
    print("💭 My Realization: I LOVE system design and data architecture!")
    
    return int(estimated_monthly_rides)

def evening_research_plan():
    """Coming home and planning my Big Tech journey"""
    
    print("\n" + "=" * 60)
    print("🏠 EVENING: Research & Planning Phase")
    print("=" * 60)
    
    # My research findings
    learning_stack = {
        "DSA": "Data Structures & Algorithms with Python",
        "Python": "Deep dive into Python for interviews",
        "AWS": "Cloud services and architecture",
        "System_Design": "Scalable systems like Big Tech companies"
    }
    
    # Course I found
    youtube_course = "https://www.youtube.com/watch?v=pkYVOmU3MgA"
    
    print("🔍 Research Results:")
    for topic, description in learning_stack.items():
        print(f"   📌 {topic}: {description}")
    
    print(f"\n🎯 Course Selected: {youtube_course}")
    print("⏰ Current Time: 11:55 PM")
    print("😴 Decision: Time for bed, tomorrow we code!")
    
    return "Ready to start the 100-day journey!"

def main():
    """My complete Day 1 story"""
    
    print("🌟 Welcome to my Day 1 story!")
    print("Today was the day that sparked my Big Tech journey...\n")
    
    # Execute my day's journey
    aws_result = aws_sagemaker_adventure()
    rides_estimate = system_design_breakthrough()
    plan_result = evening_research_plan()
    
    print("\n" + "=" * 60)
    print("📝 DAY 1 SUMMARY")
    print("=" * 60)
    print("✅ Attended AWS SageMaker Roadshow")
    print("✅ Gave successful lightning talk on RAG")
    print("✅ Discovered passion for system design")
    print(f"✅ Calculated {rides_estimate:,} Uber rides/month (got applauded!)")
    print("✅ Researched and planned Big Tech preparation")
    print("✅ Found the perfect course to start with")
    print("✅ Ready to begin 100 days of focused learning")
    
    print("\n🚀 Tomorrow: Day 2 begins the real coding journey!")
    print("💤 For now... good night and sweet dreams of algorithms!")

if __name__ == "__main__":
    main() 