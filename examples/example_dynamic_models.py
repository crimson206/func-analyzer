"""
Dynamic model generation examples.
"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from func_analyzer import create_function_model, analyze_function


class SampleUserConfig(BaseModel):
    """Configuration for user processing."""
    name: str = Field(description="User's full name")
    age: int = Field(description="User's age in years", ge=0)
    email: Optional[str] = Field(None, description="User's email address")


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


def sample_pydantic_input(data: List[Dict[str, Any]], config: SampleUserConfig) -> str:
    """
    Function that takes a Pydantic model as input.
    
    Args:
        config: User configuration object
        
    Returns:
        Formatted user information string
    """
    result = f"User: {config.name}, Age: {config.age}"
    if config.email:
        result += f", Email: {config.email}"
    return result


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
    
    # Create model from function with Pydantic input
    PydanticModel = create_function_model(sample_pydantic_input)
    print("Pydantic Function Model:")
    print(PydanticModel)
    print()
    


def example_model_usage():
    """Demonstrate how to use the generated models."""
    # Create model
    Model = create_function_model(sample_simple_function)
    
    # Use with valid data
    try:
        instance = Model(name="John", age=30)
        print("Valid instance:", instance)
        print("Name:", instance.name)
        print("Age:", instance.age)
    except Exception as e:
        print("Error:", e)
    
    # Use with invalid data
    try:
        instance = Model(name="John", age="invalid")
        print("Invalid instance:", instance)
    except Exception as e:
        print("Validation error:", e)
    print()


def example_schema_generation():
    """Demonstrate JSON Schema generation."""
    # Create model
    Model = create_function_model(sample_simple_function)
    
    # Generate JSON Schema
    schema = Model.model_json_schema()
    print("JSON Schema:")
    print(schema)
    print()
    
    # Generate OpenAPI schema
    openapi_schema = {
        "openapi": "3.0.0",
        "info": {
            "title": "Function API",
            "version": "1.0.0"
        },
        "paths": {
            "/sample_simple_function": {
                "post": {
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": schema
                            }
                        }
                    }
                }
            }
        }
    }
    print("OpenAPI Schema:")
    print(openapi_schema)


def example_function_analysis():
    """Demonstrate function analysis."""
    # Analyze simple function
    info = analyze_function(sample_simple_function)
    print("Function Analysis:")
    print(info)
    print()
    
    # Analyze complex function
    info = analyze_function(sample_complex_types)
    print("Complex Function Analysis:")
    print(info)

    # Analyze pydantic function
    info = analyze_function(sample_pydantic_input)
    print("Pydantic Function Analysis:")
    print(info)



if __name__ == "__main__":
    example_dynamic_model_creation()
    print("="*50)
    example_model_usage()
    print("="*50)
    example_schema_generation()
    print("="*50)
    example_function_analysis() 