def mock_lead_capture(name: str, email: str, platform: str):
    """
    Simulates capturing a lead. In a real application, this would 
    save the lead information to a database or CRM.
    """
    print(f"\n[LEAD CAPTURED]")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Platform: {platform}")
    print("-" * 20)
    return True
