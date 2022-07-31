from dotenv import load_dotenv
from starlette.config import Config

load_dotenv()

config = Config(".env")

DATABASE_URL = config("DATABASE_URL")
FIXER_IO_BASE_URL = config(
    "FIXER_IO_BASE_URL", default="https://api.apilayer.com/fixer"
)
FIXER_IO_LATEST_ENDPOINT_CONTEXT_PATH = config(
    "FIXER_IO_LATEST_ENDPOINT_CONTEXT_PATH", default="/latest"
)
FIXER_IO_API_KEY = config("FIXER_IO_API_KEY")

TEST_MODE = config("TEST_MODE", default=False)
