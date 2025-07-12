 #!/bin/bash
set -euo pipefail

# Create secure temporary file
temp_file=$(mktemp)
trap 'rm -f "$temp_file"' EXIT

if [[ -z "${CI_COMMIT_MESSAGE:-}" ]]; then
    if ! git log -1 --pretty=%B > "$temp_file" 2>/dev/null; then
        echo "Error: Failed to get commit message from git" >&2
        exit 1
    fi
else
    echo "$CI_COMMIT_MESSAGE" > "$temp_file"
fi

if ! conventional-pre-commit "$temp_file"; then
    echo "Error: Commit message does not follow conventional format" >&2
    exit 1
fi
