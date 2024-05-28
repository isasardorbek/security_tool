# scan/scanner.py
import re

patterns = {
    'SQL Injection': re.compile(r"[^a-zA-Z](SELECT|INSERT|UPDATE|DELETE)[^a-zA-Z]"),
    'XSS': re.compile(r"<script>.*</script>")
}

def scan_code(code):
    vulnerabilities = []
    for vuln_name, pattern in patterns.items():
        if pattern.search(code):
            vulnerabilities.append(vuln_name)
    return vulnerabilities
