import os
import json
import PyPDF2
from docx import Document  # pip install python-docx

# Define the path to the CTF problems repository
repo_path = 'C:\\Users\\jomue\\TAMUctf-2023-master\\TAMUctf-2023-master'  # Update with your repo path

# Directory where you want to save the JSON files
output_dir = 'ctf_2023_challenge_jsons'
os.makedirs(output_dir, exist_ok=True)  # Create the output directory if it doesn't exist

# skip_path = r'C:\Users\jomue\TAMUctf-2021-master\TAMUctf-2021-master\forensics'

# Set to track unsupported/unprocessed file extensions
unsupported_file_extensions = set()

def split_problem_solution(content):
    """Splits README content into problem statement and solution based on the '## Solution' header."""
    parts = content.split('## Solution', 1)
    problem_statement = parts[0].strip()
    solution = parts[1].strip() if len(parts) > 1 else None
    return problem_statement, solution

def extract_text_from_file(file_path):
    """Extract text from different file types."""
    # Special handling for Dockerfile (it may not have an extension)
    if os.path.basename(file_path).lower() == 'dockerfile':
        file_ext = 'dockerfile'
    elif os.path.basename(file_path).lower() == 'makefile':
        file_ext = 'makefile'
    elif os.path.basename(file_path).lower() == 'Dockerfile-base':
        file_ext = 'dockerfile'
    elif os.path.basename(file_path).lower() == 'Dockerfile-bind':
        file_ext = 'dockerfile'
    elif os.path.basename(file_path).lower() == 'Dockerfile-python':
        file_ext = 'dockerfile'
    elif os.path.basename(file_path).lower() == 'dockerfile-base':
        file_ext = 'dockerfile'
    elif os.path.basename(file_path).lower() == 'dockerfile-python':
        file_ext = 'dockerfile'
    elif os.path.basename(file_path).lower() == 'dockerfile-bind':
        file_ext = 'dockerfile'
    elif os.path.basename(file_path).lower() == 'arpon-start':
        file_ext = 'start'
    elif os.path.basename(file_path).lower() == 'vagrantfile':
        file_ext = 'vagrantfile'
    elif os.path.basename(file_path).lower() == 'vagrantfile-template':
        file_ext = 'vagrantfile'
    elif os.path.basename(file_path).lower() == 'hostname':
        file_ext = 'hostname'
    elif os.path.basename(file_path).lower() == 'cert':
        file_ext = 'cert'
    elif os.path.basename(file_path).lower() == 'license':
        file_ext = 'license'
    elif os.path.basename(file_path).lower() == 'builder':
        file_ext = 'builder'
    elif os.path.basename(file_path).lower() == 'id_rsa':
        file_ext = 'id_rsa'
    elif os.path.basename(file_path).lower() == 'error_log':
        file_ext = 'error_log'
    elif os.path.basename(file_path).lower() == 'gradlew':
        file_ext = 'gradle'
    elif os.path.basename(file_path).lower() == 'preinst':
        file_ext = 'preinst'
    elif os.path.basename(file_path).lower() == 'kbuild':
        file_ext = 'kbuild'
    elif os.path.basename(file_path).lower() == 'common-auth':
        file_ext = 'common-auth'
    elif os.path.basename(file_path).lower() == 'expected_stdout':
        file_ext = 'expected_stdout'
    elif os.path.basename(file_path).lower() == 'pwn-sudoer':
        file_ext = 'pwn-sudoer'
    else:
        file_ext = file_path.lower().split('.')[-1]

    # Handle text-based files
    try:
        if file_ext in ['md', 'txt', 'py', 'c', 'sh', 'php', 'json', 'makefile', 'dockerfile', 'conf', 'motd', 'key', 'crt', 'go', 'yml', 'yaml', 'h', 'html', 'java', 'start', 'cpp', 'js', 'css', 'xml', 'rst','less', 'pub', 'map','vtt', 'po', 'csr','s', 'scss', 'htaccess', 'vagrantfile', 'cert', 'error_log', 'license', 'hostname', 'id_rsa', 'rs', 'builder', 'bat', 'properties', 'pug', 'cc', 'config', 'lock', 'processor', 'gradle', 'toml', 'proto', 'bin', 'gradle', 'build', 'gitignore', 'dockerignore', 'preinst', 'template', 'common-auth', 'kbuild', 'mod', 'sql', 'hdl', 'sum', 'pwn-sudoer', 'diff', 'patch', 'hex', 'expected_stdout']:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read()

        # Handle PDF files
        elif file_ext == 'pdf':
            with open(file_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                return "\n".join([page.extract_text() for page in reader.pages])

        # Handle DOCX files
        elif file_ext == 'docx':
            doc = Document(file_path)
            return "\n".join([para.text for para in doc.paragraphs])

        # Handle other file types as binary (log as binary)
        else:
            if(file_ext not in ['jpeg', 'png', 'webp', 'svg', 'gif', 'zip', 'phar', 'psd', 'eot', 'ttf', 'db', 'jpg', 'pcap', 'swf', 'woff2', 'ico', 'woff', 'mo', 'o', 'pyc', 'aes', 'jar', '6', 'sqlite3', 'out', 'wav', 'enc', 'class', 'mp3', 'data', 'gz']):
                unsupported_file_extensions.add(file_ext)
                print(file_path)
            return f"[Binary file or unsupported type: {file_ext}]"

    except Exception as e:
        return f"[Error reading file: {str(e)}]"



def collect_files_from_directory(problem_path):
    """Recursively collect all relevant files in the problem directory and its subdirectories."""
    collected_files = {}

    for root, dirs, files in os.walk(problem_path):
        for file in files:
            file_path = os.path.join(root, file)

            # # Skip files in the skip path
            # if file_path.startswith(skip_path):
            #     print(f"Skipping file: {file_path}")
            #     continue

            # Generate the relative path for each file, relative to the problem directory
            relative_file_path = os.path.relpath(file_path, problem_path)

            # Extract the text from the file, regardless of type
            file_content = extract_text_from_file(file_path)
            collected_files[relative_file_path] = file_content

    return collected_files

# Walk through the repository to find CTF challenges
for root, dirs, files in os.walk(repo_path):
    # Ensure we are one directory level deep (i.e., problem folder inside category folder)
    relative_path = os.path.relpath(root, repo_path)
    depth = len(relative_path.split(os.sep))

    if depth != 2:  # We only want directories that are exactly one level deep (category/problem)
        continue

    category = os.path.basename(os.path.dirname(root))
    challenge = {}

    # Collect all files from the problem directory and its subdirectories
    challenge.update(collect_files_from_directory(root))

    # Only proceed if we have gathered data for this challenge
    if challenge:
        challenge_name = os.path.basename(root)
        challenge['category'] = category
        json_output_path = os.path.join(output_dir, f"{challenge_name}.json")

        # Write the challenge data to a JSON file
        with open(json_output_path, 'w') as json_file:
            json.dump(challenge, json_file, indent=4)

        print(f"Saved challenge {challenge_name} in category {category} to {json_output_path}")
print("\nUnsupported or unprocessed file extensions encountered:")
print(unsupported_file_extensions)
print(len(unsupported_file_extensions))
print("CTF challenges with problem statements, solutions, and additional files from subdirectories have been successfully extracted into individual JSON files.")
