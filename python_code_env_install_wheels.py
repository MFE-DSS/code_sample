import logging
import os
import subprocess
import sys
from pathlib import Path

# Import inutile supprimé (capture de mako.runtime supprimé)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # On peut configurer le niveau de log

def install_wheels():
    try:
        wheel_path = Path("/dataiku/dss_data/code-envs/ressources/python/code_env_name/folder/wheels")
        if not wheel_path.exists():
            logger.error(f"Directory not found: {wheel_path}")
            return

        wheel_files = list(wheel_path.glob('**/*.whl'))
        if not wheel_files:
            logger.error(f"No wheel files found in directory: {wheel_path}")
            return

        logger.info(f"Found {len(wheel_files)} wheel file(s):")
        for wheel in wheel_files:
            logger.info(f"- {wheel.name}")

        for wheel in wheel_files:
            logger.info(f"Installing {wheel.name}")
            cmd = [sys.executable, "-m", "pip", "install", str(wheel)]
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,  # Correction apportée ici
                check=False
            )

            if result.returncode == 0:
                logger.info(f"Successfully installed {wheel.name}")
            else:
                logger.error(f"Failed to install {wheel.name}: {result.stderr}")

    except Exception as e:
        logger.error(f"Installation error: {str(e)}")

def main():
    try:
        logger.info("Starting wheels installation process")
        install_wheels()
        logger.info("Wheels installation process completed")
    except Exception as e:
        logger.error(f"Process Failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
