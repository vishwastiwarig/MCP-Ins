# MCP-Ins
 It implements a simple MCP (Model Context Protocol) server in Python.

The server exposes a single tool, `search_keyword_in_file`, which finds the first occurrence of a given keyword within the `data.txt` file.

## Project Structure

- `mcp_server.py`: The main server code with the tool logic.
- `data.txt`: The sample file to be searched.
- `requirements.txt`: Python dependencies.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/ressl-mcp-assignment.git](https://github.com/YOUR_USERNAME/ressl-mcp-assignment.git)
    cd ressl-mcp-assignment
    ```

2.  **Create and activate a Python virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Node.js (Required for Tester):**
    You must have [Node.js](https://nodejs.org/) installed on your system to run the `npx` command for the MCP Inspector.

## How to Run and Test

This server is designed to be run and tested using the MCP Inspector.

1.  From your terminal, run the following command:
    ```bash
    npx @modelcontextprotocol/inspector python mcp_server.py
    ```

2.  Open the Inspector URL in your browser (usually `http://127.0.0.1:6274`).

3.  Click **Connect**, then go to the **Tools** tab.

4.  Click **List Tools** and select `search_keyword_in_file`.

5.  Enter your inputs in the form:
    -   `keyword`: `Ressl` (or any word from `data.txt`)
    -   `file_path`: `data.txt`

6.  Click **Run Tool** to see the JSON output.
