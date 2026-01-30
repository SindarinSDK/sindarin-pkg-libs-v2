# Sindarin Libs

Pre-built static libraries for Sindarin projects. This repository provides cross-platform static libraries built with vcpkg, automatically compiled and committed via GitHub Actions.

## Quick Install

**Linux/macOS:**
```bash
curl -fsSL https://raw.githubusercontent.com/SindarinSDK/sindarin-pkg-libs-v2/main/scripts/install.sh | bash
```

**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/SindarinSDK/sindarin-pkg-libs-v2/main/scripts/install.ps1 | iex
```

These commands download and extract the latest libraries to `./libs` in your current directory.

## Overview

This repository builds and maintains static libraries for:
- **Linux** (x64-linux triplet)
- **macOS** (x64-osx / arm64-osx triplets)
- **Windows** (x64-mingw-static triplet)

## Included Libraries

| Library | Description |
|---------|-------------|
| zlib | Compression library |
| yyjson | High-performance JSON parser |
| libxml2 | XML parsing library |
| libyaml | YAML parsing library |
| OpenSSL | SSL/TLS cryptography |
| ngtcp2 | QUIC protocol implementation |
| libssh | SSH library |
| libgit2 | Git implementation |
| curl | HTTP client library |

## Directory Structure

```
sindarin-libs/
├── libs/
│   ├── linux/
│   │   ├── lib/          # Static libraries (.a files)
│   │   ├── include/      # Header files
│   │   ├── share/        # CMake config files
│   │   └── VERSION       # Build version
│   ├── macos/
│   │   ├── lib/
│   │   ├── include/
│   │   ├── share/
│   │   └── VERSION
│   └── windows/
│       ├── lib/
│       ├── include/
│       ├── share/
│       └── VERSION
├── vcpkg.json            # Dependency manifest
├── CMakeLists.txt        # Build configuration
├── CMakePresets.json     # Build presets
├── Makefile              # Build wrapper
└── .github/workflows/    # CI/CD pipelines
```

## Usage as a Submodule

Add this repository as a submodule to your project:

```bash
git submodule add https://github.com/your-org/sindarin-libs.git libs/sindarin-libs
git submodule update --init --recursive
```

Then in your CMakeLists.txt:

```cmake
# Determine platform
if(WIN32)
    set(SINDARIN_LIBS_PLATFORM "windows")
elseif(APPLE)
    set(SINDARIN_LIBS_PLATFORM "macos")
else()
    set(SINDARIN_LIBS_PLATFORM "linux")
endif()

# Set paths
set(SINDARIN_LIBS_DIR "${CMAKE_SOURCE_DIR}/libs/sindarin-libs/libs/${SINDARIN_LIBS_PLATFORM}")
set(SINDARIN_LIBS_INCLUDE "${SINDARIN_LIBS_DIR}/include")
set(SINDARIN_LIBS_LIB "${SINDARIN_LIBS_DIR}/lib")

# Add include path
include_directories(${SINDARIN_LIBS_INCLUDE})

# Link libraries
target_link_libraries(your_target
    "${SINDARIN_LIBS_LIB}/libcurl.a"
    "${SINDARIN_LIBS_LIB}/libgit2.a"
    "${SINDARIN_LIBS_LIB}/libssh.a"
    "${SINDARIN_LIBS_LIB}/libssl.a"
    "${SINDARIN_LIBS_LIB}/libcrypto.a"
    "${SINDARIN_LIBS_LIB}/libz.a"
    # ... other libraries as needed
)
```

## Building Locally

### Prerequisites

- CMake 3.20+
- Ninja
- Git
- Python 3
- Platform-specific:
  - **Linux**: GCC, build-essential
  - **macOS**: Xcode Command Line Tools
  - **Windows**: LLVM-MinGW

### Build Commands

```bash
# Setup vcpkg and install dependencies
make setup

# Build and copy libraries to libs/{platform}/
make build

# Clean build artifacts
make clean

# Full rebuild
make rebuild

# Show configuration
make info
```

## GitHub Actions

The repository includes automated workflows that:

1. Build libraries on all three platforms (Linux, macOS, Windows)
2. Cache vcpkg installations for faster builds
3. Create releases with platform-specific archives

### Triggering a Rebuild

- Push to `main` or `master` branch
- Create a pull request
- Manually trigger via GitHub Actions UI with "Force rebuild" option

## Updating Dependencies

1. Edit `vcpkg.json` to add/modify dependencies
2. Commit and push to trigger a rebuild
3. GitHub Actions will build and commit the new libraries

## License

The build system is provided as-is. Individual libraries retain their original licenses:
- zlib: zlib license
- yyjson: MIT
- libxml2: MIT
- libyaml: MIT
- OpenSSL: Apache 2.0
- ngtcp2: MIT
- libssh: LGPL 2.1
- libgit2: GPL 2.0 with linking exception
- curl: MIT/X derivate
