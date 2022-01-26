import re
import sys


def check():
    prefix = ["fix", "feat", "test", "update"]

    commit_file = sys.argv[1]

    with open(commit_file, encoding="utf8") as commit_desc:
        commit_line = commit_desc.readlines()

        if len(commit_line) == 0:
            sys.exit("empty")

        match = re.search("^(.*): (.*)$", commit_line[0])
        if not match or len(match.groups()) != 2:
            sys.exit("format-> type: message")

        commit_type, commit_title = match.groups()

        if commit_type.split()[-1] not in prefix:
            sys.exit("invalid commit type")

        if len(commit_title) > 50:
            sys.exit(f"title length is long {len(commit_title)}")

        if len(commit_line) > 1 and len(commit_line[1].strip()) > 0:
            sys.exit("second line not empty")
        if len(commit_line) > 2 and (
            len(commit_line[2]) == 0 or len(commit_line[2]) > 72
        ):
            sys.exit("body length not valid")
    sys.exit(0)


if __name__ == "__main__":
    check()
