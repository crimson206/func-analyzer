"""
Annotation cleaning examples.
"""

from typing import List, Dict, Optional, Any, Union
from func_analyzer import clean_annotation_string, analyze_function


def sample_basic_types(name: str, age: int, score: float, active: bool) -> str:
    """
    Function with basic type annotations.
    
    Args:
        name: User name
        age: User age
        score: User score
        active: User status
        
    Returns:
        Formatted string
    """
    return f"{name} ({age}) - Score: {score}, Active: {active}"


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


def sample_union_types(value: Union[str, int, float]) -> str:
    """
    Function with Union type annotations.
    
    Args:
        value: String, integer, or float value
        
    Returns:
        String representation
    """
    return str(value)


def sample_nested_types(items: List[Dict[str, Union[str, int]]]) -> List[str]:
    """
    Function with nested complex type annotations.
    
    Args:
        items: List of dictionaries with string or integer values
        
    Returns:
        List of string representations
    """
    return [str(item) for item in items]


def example_annotation_cleaning():
    """Demonstrate annotation cleaning functionality."""
    print("Annotation Cleaning Examples:")
    print("=" * 50)
    
    # Test basic types
    basic_types = [str, int, float, bool, list, dict]
    expected_basic = ["str", "int", "float", "bool", "list", "dict"]
    
    print("\nBasic Types:")
    for annotation, expected in zip(basic_types, expected_basic):
        cleaned = clean_annotation_string(annotation)
        print(f"  {annotation!r:20} -> {cleaned!r}")
        assert cleaned == expected, f"Expected {expected}, got {cleaned}"
    
    # Test string representations
    string_types = [
        "<class 'str'>",
        "<class 'int'>", 
        "<class 'float'>",
        "<class 'bool'>"
    ]
    expected_strings = ["str", "int", "float", "bool"]
    
    print("\nString Representations:")
    for annotation, expected in zip(string_types, expected_strings):
        cleaned = clean_annotation_string(annotation)
        print(f"  {annotation!r:20} -> {cleaned!r}")
        assert cleaned == expected, f"Expected {expected}, got {cleaned}"
    
    # Test typing module types
    typing_types = [
        "typing.List[str]",
        "typing.Dict[str, Any]",
        "typing.Optional[str]",
        "typing.Union[str, int]",
        "List[Dict[str, Any]]",
        "Optional[Dict[str, str]]",
        "Union[str, int, float]"
    ]
    expected_typing = [
        "List[str]",
        "Dict[str, Any]",
        "Optional[str]",
        "Union[str, int]",
        "List[Dict[str, Any]]",
        "Optional[Dict[str, str]]",
        "Union[str, int, float]"
    ]
    
    print("\nTyping Module Types:")
    for annotation, expected in zip(typing_types, expected_typing):
        cleaned = clean_annotation_string(annotation)
        print(f"  {annotation!r:30} -> {cleaned!r}")
        assert cleaned == expected, f"Expected {expected}, got {cleaned}"
    
    # Test complex nested types
    complex_types = [
        "List[Dict[str, Union[str, int]]]",
        "Optional[List[Dict[str, Any]]]",
        "Dict[str, Union[List[str], Dict[str, int]]]"
    ]
    expected_complex = [
        "List[Dict[str, Union[str, int]]]",
        "Optional[List[Dict[str, Any]]]",
        "Dict[str, Union[List[str], Dict[str, int]]]"
    ]
    
    print("\nComplex Nested Types:")
    for annotation, expected in zip(complex_types, expected_complex):
        cleaned = clean_annotation_string(annotation)
        print(f"  {annotation!r:40} -> {cleaned!r}")
        assert cleaned == expected, f"Expected {expected}, got {cleaned}"
    
    print("\n✅ All annotation cleaning tests passed!")


def example_function_analysis_with_cleaning():
    """Demonstrate function analysis with cleaned annotations."""
    print("\n" + "=" * 50)
    print("Function Analysis with Cleaned Annotations:")
    print("=" * 50)
    
    functions = [
        sample_basic_types,
        sample_complex_types,
        sample_union_types,
        sample_nested_types
    ]
    
    expected_return_types = ["str", "Dict[str, Any]", "str", "List[str]"]
    
    for func, expected_return in zip(functions, expected_return_types):
        info = analyze_function(func)
        print(f"\n{func.__name__}:")
        print(f"  Return type: {info['return_annotation']}")
        print("  Parameters:")
        for param in info['parameters']:
            print(f"    {param['name']}: {param['annotation']}")
            if param['default'] is not None:
                print(f"      (default: {param['default']})")
        
        # Assert return type is cleaned
        assert info['return_annotation'] == expected_return, \
            f"Expected return type {expected_return}, got {info['return_annotation']}"
        
        # Assert all parameter annotations are cleaned (no typing. prefix)
        for param in info['parameters']:
            assert not param['annotation'].startswith('typing.'), \
                f"Parameter {param['name']} has uncleaned annotation: {param['annotation']}"
            assert not '<class' in param['annotation'], \
                f"Parameter {param['name']} has uncleaned annotation: {param['annotation']}"
    
    print("\n✅ All function analysis tests passed!")


def example_comparison_before_after():
    """Compare raw vs cleaned annotations."""
    print("\n" + "=" * 50)
    print("Before vs After Cleaning:")
    print("=" * 50)
    
    # Raw annotations (what inspect.signature returns)
    raw_annotations = [
        str,
        int,
        "typing.List[str]",
        "typing.Optional[typing.Dict[str, typing.Any]]",
        "<class 'str'>",
        "<class 'int'>"
    ]
    
    expected_cleaned = [
        "str",
        "int", 
        "List[str]",
        "Optional[Dict[str, Any]]",
        "str",
        "int"
    ]
    
    print("\nRaw Annotation -> Cleaned Annotation:")
    for annotation, expected in zip(raw_annotations, expected_cleaned):
        raw_str = str(annotation)
        cleaned = clean_annotation_string(annotation)
        print(f"  {raw_str:40} -> {cleaned}")
        assert cleaned == expected, f"Expected {expected}, got {cleaned}"
    
    print("\n✅ All comparison tests passed!")


if __name__ == "__main__":
    example_annotation_cleaning()
    example_function_analysis_with_cleaning()
    example_comparison_before_after()
    print("\n🎉 All tests completed successfully!") 