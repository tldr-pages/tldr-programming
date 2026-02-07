"""
A Python script to add or update the keywords for all translations of a page.

Usage:
    python3 scripts/set-keywords.py [-p PAGE] [-S] [-l LANGUAGE] [-n] [KEYWORDS...]

Options:
    -p, --page PAGE
        Specify the page in the format "platform/command". This option allows setting the link for a specific page.
    -S, --sync
        Synchronize each translation's keywords with that of the English page.
    -l, --language LANGUAGE
        Specify the language, a POSIX Locale Name in the form of "ll" or "ll_CC" (e.g. "fr" or "pt_BR").
    -n, --dry-run
        Show what changes would be made without actually modifying the page.

Positional Argument:
    KEYWORDS          The keywords to be set

Examples:
    1. Set the keywords for a specific page:
       python3 scripts/set-keywords.py -p python/file-io open,read,write,readlines
       python3 scripts/set-keywords.py --page python/file-io open,read,write,readlines

    2. Read English pages and synchronize the keywords across translations:
       python3 scripts/set-keywords.py -S
       python3 scripts/set-keywords.py --sync

    3. Read English pages and synchronize the keywords for Dutch pages only:
       python3 scripts/set-keywords.py -S -l nl
       python3 scripts/set-keywords.py --sync --language nl

    4. Show what changes would be made across translations:
       python3 scripts/set-keywords.py -Sn
       python3 scripts/set-keywords.py --sync --dry-run
"""

import sys
from pathlib import Path

from _common import create_argument_parser

PROJECT_ROOT = Path(__file__).parent.parent
PAGES_DIR = PROJECT_ROOT / "pages"
KEYWORDS_LINE_INDEX = 1


def sync_single_page(
    relative_page_path: str, language_suffix: str, dry_run: bool
) -> None:
    """Sync a translation page.

    Args:
        relative_page_path (str): Relative page path, e.g. python/hello-world.md
        language_suffix (str): The suffix of the language, e.g. "nl" for Dutch
        dry_run (bool): If True, don't write to page
    """
    if not relative_page_path.endswith(".md"):
        relative_page_path += ".md"

    translation_pages_dir = PROJECT_ROOT / f"pages.{language_suffix}"
    translation_page = translation_pages_dir / relative_page_path

    if not translation_page.exists():
        print(f"Translation for {relative_page_path} does not exist yet, skipping...")
        return

    english_keyword_line = _get_keywords(PAGES_DIR / relative_page_path)
    translation_keyword_line = _get_keywords(translation_page)

    if english_keyword_line == translation_keyword_line:
        print(
            f"{translation_page.relative_to(PROJECT_ROOT)} is up to date, skipping..."
        )
        return
    print(f"Updating keywords for {translation_page.relative_to(PROJECT_ROOT)}...")

    if dry_run:
        return

    keywords_block = f"---\n{english_keyword_line}\n---\n"

    _update_keywords(translation_page, keywords_block)


def sync_language(language_suffix: str, dry_run: bool) -> None:
    """Sync all pages in a language.

    Args:
        language_suffix (str): The suffix of the language, e.g. "nl" for Dutch
        dry_run (bool): If True, don't write to any files
    """
    for programming_language_dir in PAGES_DIR.iterdir():
        if programming_language_dir.is_dir():
            for page in programming_language_dir.glob("*.md"):
                sync_single_page(
                    str(page.relative_to(PAGES_DIR)), language_suffix, dry_run
                )


def set_keywords(relative_page_path: str, keywords: list[str], dry_run: bool) -> None:
    """Set keywords for a page.

    Args:
        relative_page_path (Path): Relative path to the page, e.g. python/hello-world
        keywords (list[str]): List with keywords to set
        dry_run (bool): If True, don't write to page
    """
    if not relative_page_path.endswith(".md"):
        relative_page_path += ".md"

    page_path = PAGES_DIR / relative_page_path

    if not page_path.exists():
        print(f"Page {relative_page_path} does not exist yet")
        return
    print(f"Setting the keywords for {relative_page_path} to [{", ".join(keywords)}]")

    keywords_block = f"---\nkeywords: [{", ".join(keywords)}]\n---\n"
    _update_keywords(page_path, keywords_block)


def _get_keywords(page_path: Path) -> str:
    """Get keywords from a page.

    Args:
        page_path (Path): Path to the page

    Returns:
        str: The keyword line, e.g. "keywords: [print]"
    """
    with open(page_path, "r") as f:
        lines = f.readlines()
    return lines[KEYWORDS_LINE_INDEX].strip()


def _update_keywords(page_path: Path, keywords_block: str) -> None:
    """Update the keywords in a page.

    Args:
        page_path (Path): Path to the page
        keywords_block (str): Keyword block that needs to be updated/inserted
    """
    keyword_line = _get_keywords(page_path)

    with open(page_path, "r") as f:
        original_text = f.read()

    with open(page_path, "w") as f:
        if not keyword_line.startswith("keywords:"):
            f.write(keywords_block + original_text)
        else:  # Keywords already exist, but need to be updated
            lines = original_text.splitlines(keepends=True)
            page_without_keywords = lines[3:]
            f.write(keywords_block + "".join(page_without_keywords))


def main() -> None:
    parser = create_argument_parser("Sets the keywords for all translations of a page")
    parser.add_argument("keywords", type=str, nargs="?", default="")
    args = parser.parse_args()

    # Print usage information if no arguments were provided
    if len(sys.argv) == 1:
        parser.print_help()
        return

    # Use '--dry-run' option
    if args.dry_run:
        print("Dry-run, not writing to any files")

    # Use '--sync' option
    if args.sync:
        if args.page != "":  # Sync a single page
            if args.language == "":
                print("You must specify a language using --language")
                return
            sync_single_page(args.page, args.language, args.dry_run)
        elif args.language != "":  # Sync all pages for a language
            sync_language(args.language, args.dry_run)
        else:  # Sync all pages in all languages
            for dir in PROJECT_ROOT.iterdir():
                if "pages" in str(dir.name) and not dir.name == "pages":
                    language_suffix = dir.name.replace("pages.", "")
                    sync_language(language_suffix, args.dry_run)

    # Use '--page' option
    elif args.page != "":
        keywords = args.keywords.split(",")
        set_keywords(args.page, keywords, args.dry_run)


if __name__ == "__main__":
    main()
