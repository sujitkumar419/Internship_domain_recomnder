# Simple content-based domain recommendation engine

def recommend_domain(profile):
    keywords = profile.lower()
    if "python" in keywords or "data" in keywords:
        return "Data Science"
    elif "html" in keywords or "css" in keywords or "javascript" in keywords:
        return "Web Development"
    elif "network" in keywords or "security" in keywords:
        return "Cybersecurity"
    elif "java" in keywords or "android" in keywords:
        return "App Development"
    else:
        return "General Internship"

# Example usage
user_input = input("Enter your skills and interests: ")
domain = recommend_domain(user_input)
print(f"Recommended Domain: {domain}")
