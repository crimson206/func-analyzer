"""
Basic function analysis examples.
"""

from typing import List, Optional, Dict, Any
from func_analyzer import create_function_model, analyze_function


def sample_simple_function(name: str, age: int = 25) -> str:
    """
    A simple function with basic parameters.
    
    Args:
        name: The person's name
        age: The person's age (default: 25)
        
    Returns:
        A greeting message
    """
    return f"Hello {name}, you are {age} years old!"


def sample_complex_types(data: List[Dict[str, Any]], config: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """
    Function with complex type annotations.
    
    Args:
        data: List of dictionaries containing data
        config: Optional configuration dictionary
        
    Returns:
        Processed data dictionary
    """
    if config is None:
        config = {}
    
    result = {"processed": len(data), "config": config}
    return result


def sample_no_docstring(param1: str, param2: int) -> bool:
    # This function has no docstring
    return param1 == str(param2)


def sample_missing_type_hints(name, age=25):
    """
    Function with missing type hints.
    
    Args:
        name: The person's name
        age: The person's age
        
    Returns:
        A greeting message
    """
    return f"Hello {name}, you are {age} years old!"


def sample_async_function(data: List[int]) -> List[int]:
    """
    Async function example.
    
    Args:
        data: List of integers to process
        
    Returns:
        Processed list of integers
    """
    async def process():
        return [x * 2 for x in data]
    
    return data


def sample_generator_function(start: int, end: int) -> int:
    """
    Generator function example.
    
    Args:
        start: Starting number
        end: Ending number
        
    Yields:
        Numbers from start to end
    """
    for i in range(start, end + 1):
        yield i


def example_dynamic_model_creation():
    """Demonstrate dynamic model creation."""
    # Create model from simple function
    SimpleModel = create_function_model(sample_simple_function)
    print("Simple Function Model:")
    print(SimpleModel)
    print()
    
    # Create model from complex function
    ComplexModel = create_function_model(sample_complex_types)
    print("Complex Function Model:")
    print(ComplexModel)
    print()
    
    # Create model from function with no docstring
    NoDocModel = create_function_model(sample_no_docstring)
    print("No Docstring Model:")
    print(NoDocModel)
    print()
    
    # Create model from function with missing type hints
    NoTypeModel = create_function_model(sample_missing_type_hints)
    print("Missing Type Hints Model:")
    print(NoTypeModel)
    print()


def example_model_usage():
    """Demonstrate model usage and validation."""
    # Create model
    Model = create_function_model(sample_simple_function)
    
    # Valid usage
    try:
        instance = Model(name="John", age=30)
        print("Valid instance:", instance)
        print("Name:", instance.name)
        print("Age:", instance.age)
    except Exception as e:
        print("Error:", e)
    
    # Invalid usage (wrong type)
    try:
        instance = Model(name="John", age="invalid")
        print("Invalid instance:", instance)
    except Exception as e:
        print("Validation error:", e)
    
    # Missing required field
    try:
        instance = Model(name="John")  # age is required
        print("Missing field instance:", instance)
    except Exception as e:
        print("Missing field error:", e)
    print()


def example_function_analysis():
    """Demonstrate function analysis."""
    functions = [
        sample_simple_function,
        sample_complex_types,
        sample_no_docstring,
        sample_missing_type_hints,
        sample_async_function,
        sample_generator_function
    ]
    
    print("Function Analysis Results:")
    for func in functions:
        info = analyze_function(func)
        print(f"\n{func.__name__}:")
        print(info)


if __name__ == "__main__":
    example_dynamic_model_creation()
    print("\n" + "="*50 + "\n")
    example_model_usage()
    print("\n" + "="*50 + "\n")
    example_function_analysis() 