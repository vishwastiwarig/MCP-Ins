import os
from mcp.server.fastmcp import FastMCP

#  your MCP server

mcp = FastMCP("FileSearchServer")

print("MCP Server is starting...")

#  @mcp.tool() decorator
@mcp.tool()
def search_keyword_in_file(keyword: str, file_path: str) -> dict:
    """
    Searches for a specific keyword in a file and returns
    the first line number where it was found.

    :param keyword: The word to search for.
    :param file_path: The path to the file (e.g., 'data.txt').
    :return: A dictionary with search results.
    """
    
    print(f"Tool triggered: Searching for '{keyword}' in '{file_path}'")
    
    
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return {
            "found": False,
            "line_number": -1,
            "error": f"File not found: {file_path}"
        }

    try:
        
        with open(file_path, 'r') as f:
            for i, line in enumerate(f):
                if keyword in line:
                    
                    print(f"Found keyword on line {i + 1}")
                    return {
                        "found": True,
                        "line_number": i + 1,
                        "line_content": line.strip(),
                        "error": None
                    }
        
        
        print("Keyword not found.")
        return {
            "found": False,
            "line_number": -1,
            "error": "Keyword not found in file."
        }

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return {
            "found": False,
            "line_number": -1,
            "error": str(e)
        }


if __name__ == "__main__":
   
    mcp.run(transport="stdio")