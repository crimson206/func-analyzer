"""
Basic function analysis example.
"""

from func_analyzer import analyze_function


def sample_user_info(name: str, age: int, email: str = None, active: bool = True) -> dict:
    """
    Create user information dictionary.
    
    Args:
        name: User's full name
        age: User's age in years
        email: User's email address (optional)
        active: Whether user account is active
        
    Returns:
        Dictionary containing user information
    """
    return {
        "name": name,
        "age": age,
        "email": email,
        "active": active
    }


def example_basic_analysis():
    """Demonstrate basic function analysis."""
    info = analyze_function(sample_user_info)
    print(info)


if __name__ == "__main__":
    example_basic_analysis() 