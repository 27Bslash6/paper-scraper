import argparse
import paperscraper

LOGGER = paperscraper.LOGGER

parser = argparse.ArgumentParser(
    prog="ProgramName",
    description="What the program does",
    epilog="Text at the bottom of help",
)

parser.add_argument("query")
parser.add_argument("-c", "--count", default=100)
parser.add_argument("-d", "--dir", default="download")
parser.add_argument(
    "-v", "--verbose", default=False, action=argparse.BooleanOptionalAction
)

args = parser.parse_args()

papers = paperscraper.search_papers(
    args.query, args.count, args.dir, args.verbose, logger=LOGGER.info
)
