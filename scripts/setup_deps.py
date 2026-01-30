#!/usr/bin/env python3
"""
Setup script for sindarin-libs vcpkg dependencies.
Handles cross-platform vcpkg installation and dependency building.
"""

import os
import sys
import subprocess
import platform
import shutil
import argparse
from pathlib import Path


def get_platform():
    """Get the current platform name."""
    return platform.system().lower()


def get_triplet():
    """Get the vcpkg triplet for the current platform."""
    system = platform.system().lower()
    machine = platform.machine().lower()

    if system == "windows":
        return "x64-mingw-static"
    elif system == "darwin":
        if machine == "arm64":
            return "arm64-osx"
        return "x64-osx"
    else:  # Linux
        return "x64-linux"


def run_command(cmd, cwd=None, env=None, capture=False):
    """Run a command and optionally capture output."""
    print(f"Running: {' '.join(cmd) if isinstance(cmd, list) else cmd}")

    if isinstance(cmd, str):
        cmd = cmd.split()

    merged_env = os.environ.copy()
    if env:
        merged_env.update(env)

    try:
        if capture:
            result = subprocess.run(
                cmd,
                cwd=cwd,
                env=merged_env,
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        else:
            subprocess.run(cmd, cwd=cwd, env=merged_env, check=True)
            return None
    except subprocess.CalledProcessError as e:
        print(f"Command failed with exit code {e.returncode}")
        if capture and e.stderr:
            print(f"Error: {e.stderr}")
        raise


def check_tool(tool):
    """Check if a tool is available in PATH."""
    return shutil.which(tool) is not None


def check_dependencies():
    """Check that required tools are installed."""
    required = ["git", "cmake", "ninja"]

    system = platform.system().lower()
    if system == "windows":
        required.append("clang")
    elif system == "darwin":
        required.append("clang")
    else:
        required.append("gcc")

    missing = []
    for tool in required:
        if not check_tool(tool):
            missing.append(tool)

    if missing:
        print(f"Missing required tools: {', '.join(missing)}")
        print("\nPlease install the missing tools:")
        if system == "linux":
            print("  sudo apt-get install build-essential cmake ninja-build git")
        elif system == "darwin":
            print("  brew install cmake ninja git")
        else:  # Windows
            print("  choco install cmake ninja git llvm")
        return False

    return True


def setup_vcpkg(project_root, verbose=False):
    """Clone and bootstrap vcpkg if needed."""
    vcpkg_dir = project_root / "vcpkg"

    if not vcpkg_dir.exists():
        print("Cloning vcpkg...")
        run_command([
            "git", "clone",
            "https://github.com/microsoft/vcpkg.git",
            str(vcpkg_dir)
        ])
    else:
        print("Updating vcpkg...")
        run_command(["git", "pull"], cwd=vcpkg_dir)

    # Bootstrap vcpkg
    system = platform.system().lower()
    if system == "windows":
        bootstrap_script = vcpkg_dir / "bootstrap-vcpkg.bat"
        run_command([str(bootstrap_script), "-disableMetrics"], cwd=vcpkg_dir)
    else:
        bootstrap_script = vcpkg_dir / "bootstrap-vcpkg.sh"
        run_command(["sh", str(bootstrap_script), "-disableMetrics"], cwd=vcpkg_dir)

    return vcpkg_dir


def install_dependencies(vcpkg_dir, project_root, triplet, verbose=False):
    """Install vcpkg dependencies."""
    system = platform.system().lower()
    vcpkg_exe = vcpkg_dir / ("vcpkg.exe" if system == "windows" else "vcpkg")

    if not vcpkg_exe.exists():
        raise RuntimeError(f"vcpkg executable not found at {vcpkg_exe}")

    print(f"Installing dependencies for triplet: {triplet}")

    cmd = [
        str(vcpkg_exe),
        "install",
        f"--triplet={triplet}",
        f"--x-manifest-root={project_root}",
        f"--x-install-root={project_root / 'vcpkg_installed'}"
    ]

    if verbose:
        cmd.append("--debug")

    run_command(cmd, cwd=project_root)


def main():
    parser = argparse.ArgumentParser(description="Setup sindarin-libs dependencies")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    parser.add_argument("--check", action="store_true", help="Only check dependencies")
    parser.add_argument("--triplet", help="Override vcpkg triplet")
    parser.add_argument("--vcpkg-root", help="Path to existing vcpkg installation")
    args = parser.parse_args()

    # Get project root (parent of scripts directory)
    script_dir = Path(__file__).parent.resolve()
    project_root = script_dir.parent

    print(f"Project root: {project_root}")
    print(f"Platform: {get_platform()}")

    # Check dependencies
    if not check_dependencies():
        return 1

    if args.check:
        print("All required tools are available.")
        return 0

    # Determine triplet
    triplet = args.triplet or get_triplet()
    print(f"Using triplet: {triplet}")

    # Setup vcpkg
    if args.vcpkg_root:
        vcpkg_dir = Path(args.vcpkg_root)
        if not vcpkg_dir.exists():
            print(f"Error: Specified vcpkg root does not exist: {vcpkg_dir}")
            return 1
    else:
        vcpkg_dir = setup_vcpkg(project_root, args.verbose)

    # Install dependencies
    install_dependencies(vcpkg_dir, project_root, triplet, args.verbose)

    print("\nSetup complete!")
    print(f"Dependencies installed to: {project_root / 'vcpkg_installed' / triplet}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
